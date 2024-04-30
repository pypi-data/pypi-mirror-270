#!/usr/bin/env python3

# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2021 Michał Góral.

from typing import List, ClassVar, Any, Dict, Self

import os
import sys
import subprocess
import tempfile
import shutil
import tomllib
import re
from datetime import datetime as dt
from dataclasses import dataclass, field
from pathlib import Path
import functools
import weakref
import importlib.resources
from importlib.resources.abc import Traversable
from collections import deque

import click


def eecho(*a, **kw):
    kw["err"] = True
    kw["fg"] = "red"
    return click.secho(*a, **kw)


def echo(*a, **kw):
    return click.secho(*a, **kw)


@dataclass
class DockerCommand:
    prog: ClassVar = None
    args: List[Any] = field(default_factory=list)

    def add_option(
        self, name: str, option: str | bool | None, *, allow_empty: bool = False
    ) -> Self:
        if option is True:
            self.args.append(name)
        elif option is False or option is None:
            pass
        elif option or allow_empty:
            self.args.extend((name, str(option)))

        return self

    def add_argument(self, arg) -> Self:
        if arg:
            self.args.append(arg)
        return self

    def add_assignment_options(
        self, arg: str, options: Dict[str, str], delim: str
    ) -> Self:
        assert len(delim) == 1, "invalid delimiter"
        for name, value in options.items():
            if name and value:
                self.add_option(arg, f"{name}{delim}{value}")
        return self

    def run(self, capture=True, exit_on_error=False) -> subprocess.CompletedProcess:
        cmd: List[str] = [DockerCommand.prog] + [str(a) for a in self.args]

        kw: dict[str, Any] = {"text": True}
        if capture:
            kw["stdout"] = subprocess.PIPE

        cp = subprocess.run(cmd, **kw)

        if exit_on_error and cp.returncode != 0:
            sys.exit(cp.returncode)
        return cp


def engine(*args, **run_kw):
    return DockerCommand(list(args)).run(**run_kw)


def purge_container(id: str):
    cp = engine("rm", "--force", "--volumes", id, capture=True, exit_on_error=False)
    if cp.returncode != 0:
        eecho(f"Failed to remove container {id}")


@dataclass
class Flavor:
    path: Traversable
    name: str = field(default="", init=False)
    _config: dict | None = field(default=None, init=False)

    def __post_init__(self):
        self.name = self.path.name

    @property
    def config(self):
        if self._config is None:
            self._config = load_toml(self.path.joinpath("flavor.toml"))
        return self._config

    @property
    def tag(self):
        tagname = re.sub(r"\s+", "-", self.name)
        return f"justin:{self.name}"

    @property
    def args(self) -> Dict[str, Any]:
        return self.config.get("build", {}).get("args", {})


def context() -> Traversable:
    return importlib.resources.files("justin.resources.docker")


# This function must support Traversables (subset of Paths), because context
# might not exist on a file system.
@functools.singledispatch
def copy_traversable(source: Traversable, destination: Path):
    if source.is_dir():
        destination.mkdir()
        for elem in source.iterdir():
            copy_traversable(elem, destination / elem.name)
    else:
        destination.open("wb").write(source.read_bytes())


@copy_traversable.register(Path)
def _(source: Path, destination: Path):
    if source.is_dir():
        shutil.copytree(source, destination)
    else:
        shutil.copy(source, destination)


def is_flavor(path: Traversable) -> bool:
    flavor_toml = path.joinpath("flavor.toml")
    install = path.joinpath("install")
    install_sh = install.joinpath("install.sh")

    return (
        path.is_dir()
        and flavor_toml.is_file()
        and install.is_dir()
        and install_sh.is_file()
    )


def find_flavor(flavor: str, search_paths: List[Traversable]) -> Flavor:
    if "/" in flavor or "\\" in flavor:
        eecho(f"{flavor}: flavor name musn't contain a slash or backslash")
        sys.exit(1)

    for path in search_paths:
        flavorpath = path.joinpath(flavor)
        if is_flavor(flavorpath):
            return Flavor(flavorpath)

    eecho(f"Couldn't find flavor '{flavor}'")
    sys.exit(1)


def list_flavors(search_paths: List[Traversable]) -> Dict[str, Traversable]:
    flavors = {}
    for path in search_paths:
        for child in path.iterdir():
            if is_flavor(child) and child.name not in flavors:
                flavors[child.name] = child
    return flavors


def load_toml(path: Traversable) -> dict:
    try:
        return tomllib.loads(path.read_text("utf-8"))
    except (NotADirectoryError, FileNotFoundError):
        eecho(f"error: {path} doesn't exist")
        sys.exit(1)
    except tomllib.TOMLDecodeError as te:
        eecho(f"error: {path}: {str(te)}")
        sys.exit(1)


def parse_str_asignments(
    elements: List[str], delim: str, ignore_errors=False
) -> Dict[str, str]:
    assert len(delim) == 1, "invalid delimiter"
    parsed = {}
    for elem in elements:
        argname, _, argval = elem.partition(delim)
        if not argname or not argval:
            eecho(f"Invalid format of build arg: {elem}")
            if ignore_errors:
                continue
            sys.exit(1)
        parsed[argname] = argval
    return parsed


def validate_config_paths(ctx, param, value) -> tuple[Path, Path]:
    host, _, container = value.partition(":")
    host = Path(host)

    if container:
        container = Path(container)
    else:
        args = ctx.obj
        if not args.workspace:
            raise click.BadParameter("workspace and coontainer path are both not set")

        hostabs = host.absolute()
        workspaceabs = args.workspace.absolute()

        try:
            container = Path("/workspace") / hostabs.relative_to(workspaceabs)
        except ValueError:
            raise click.BadParameter(
                "TOML configuration isn't relative to the workspace"
            )

    return host, container


@dataclass
class Args:
    flavor: Flavor
    flavor_search_paths: List[Traversable]
    env: Dict[str, str]
    user: str | None
    workspace: Path | None
    read_only: bool
    copy_workspace: bool
    volumes: Dict[str, str]
    copy_back: Dict[str, str]
    engine: str
    cmd: str | None


@click.group()
@click.option(
    "-C",
    "--change-dir",
    default=".",
    help="change directory before executing any command",
)
@click.option(
    "-E",
    "--engine",
    default="docker",
    show_default=True,
    help="command to run container engine (e.g. docker, podman)",
)
@click.option(
    "-a",
    "--additional-flavors",
    multiple=True,
    default=[],
    help="directories which contain additional flavors",
)
@click.option(
    "-F",
    "--flavor",
    default="minimal",
    show_default=True,
    help="flavor of image which should be built.",
)
@click.option(
    "-e",
    "--env",
    multiple=True,
    metavar="VAR=VALUE",
    default=[],
    help="set environment variables",
)
@click.option("-u", "--user", help="run as a user")
@click.option(
    "-w",
    "--workspace",
    help="host directory to mount as a /workspace within a container",
)
@click.option(
    "--read-only", is_flag=True, default=False, help="mount volume in read-only mode"
)
@click.option(
    "--copy-workspace",
    is_flag=True,
    default=False,
    help="copy contents of a workspace instead of bind-mounting",
)
@click.option(
    "-v", "--volume", "volumes", multiple=True, default=[], help="bind-mount volumes"
)
@click.option(
    "-b",
    "--copy-back",
    metavar="CONTAINER:HOST",
    multiple=True,
    default=[],
    help="copy files and directories from the container to the host.",
)
@click.option("-c", "--cmd", help="just executable within a container")
def cli(
    change_dir,
    engine,
    flavor,
    additional_flavors,
    env,
    user,
    workspace,
    read_only,
    copy_workspace,
    volumes,
    copy_back,
    cmd,
):
    """Run just (a justfile command runner) inside a OCI container.

    justin provides a simple way to create and run customised images with
    installed 'just' program. It uses a concept of build "flavors", which is a
    way to inject customizations into image build process. You can then select
    between different flavors

    justin provides the following built-in flavors: minimal (default), ci.
    """
    additional_flavors = [Path(af) for af in additional_flavors]
    flavor_search_paths = additional_flavors + [context().joinpath("flavors")]

    # Some parameters are not passed to args on purpose: subcommands don't need
    # to know about them
    args = Args(
        flavor=find_flavor(flavor, flavor_search_paths),
        flavor_search_paths=flavor_search_paths,
        env=parse_str_asignments(env, "="),
        user=user,
        workspace=Path(workspace) if workspace else None,
        read_only=read_only,
        copy_workspace=copy_workspace,
        volumes=parse_str_asignments(volumes, ":"),
        copy_back=parse_str_asignments(copy_back, ":"),
        engine=engine,
        cmd=cmd,
    )

    if change_dir:
        os.chdir(change_dir)

    DockerCommand.prog = engine

    ctx = click.get_current_context()
    ctx.obj = args


@cli.command()
@click.option(
    "--build-arg",
    "build_args",
    multiple=True,
    default=[],
    help="build args in form of ARGNAME=value",
)
@click.option(
    "--pull",
    is_flag=True,
    default=False,
    help="always try to pull a newer version of the image",
)
@click.option(
    "--compress", is_flag=True, default=False, help="compress the build context"
)
@click.option("--no-cache", is_flag=True, default=False, help="do not use cache")
@click.option("-q", "--quiet", is_flag=True, default=False, help="be quiet")
@click.pass_obj
def build(args: Args, build_args, pull, compress, no_cache, quiet) -> None:
    """Build justin image flavor.

    Image will be built according to the chosen flavor and it will be tagged as
    'justin:<flavor>'. Although it's possible to pass non-standard build
    arguments, the best practice is to keep all of build arguments in
    flavor.toml.
    """
    parsed_build_args = parse_str_asignments(build_args, "=")

    for argname, argval in args.flavor.args.items():
        parsed_build_args.setdefault(argname, argval)

    parsed_build_args["FLAVOR"] = args.flavor.name
    parsed_build_args["BUILD_DATE"] = dt.now().isoformat()

    with tempfile.TemporaryDirectory() as tmpd:
        echo(f"Composing build context in {tmpd}")

        tmpdp = Path(tmpd)
        tmp_context = tmpdp / "context"
        flavordir = tmp_context / "flavors" / args.flavor.name

        # We'll remove all of the flavors from the copied context and copy back
        # the one selected by the user. This has a desired side-effect that
        # users may overwrite built-in flavors.
        copy_traversable(context(), tmp_context)
        try:
            shutil.rmtree(flavordir)
        except FileNotFoundError:
            pass
        except Exception as e:
            eecho(str(e))
            sys.exit(1)
        copy_traversable(args.flavor.path, flavordir)

        dc = DockerCommand(["build", "--rm", "--tag", args.flavor.tag])

        for argname, argval in parsed_build_args.items():
            dc.add_option("--build-arg", f"{argname}={argval}")

        dc.add_option("--pull", pull)
        dc.add_option("--compress", compress)
        dc.add_option("--no-cache", no_cache)
        dc.add_option("--quiet", quiet)

        cp = dc.add_argument(tmp_context).run(capture=False)
        if cp.returncode != 0:
            eecho("Build failed.")
            sys.exit(cp.returncode)


@cli.command(context_settings={"ignore_unknown_options": True})
@click.argument("justargs", nargs=-1, type=click.UNPROCESSED)
@click.pass_obj
def just(args: Args, justargs) -> None:
    """Run just container.

    All options passed to 'just' subcommand are passed directly to the just
    program within a container.

    By default no workspace or volumes are mounted inside the container.
    """
    start = DockerCommand(["start", "--attach"])
    cont = DockerCommand(["container", "create"])

    if args.workspace:
        workpath = args.workspace.absolute()
        workpath.mkdir(parents=True, exist_ok=True)

    if args.copy_workspace and not args.workspace:
        eecho("--copy-workspace requires a workspace set with --workspace")
        sys.exit(1)

    if args.workspace and not args.copy_workspace:
        ro = ":ro" if args.read_only else ""
        cont.add_option("--volume", f"{workpath}:/workspace{ro}")

    cont.add_option("--user", args.user)

    cont.add_assignment_options("--volume", args.volumes, ":")
    cont.add_assignment_options("--env", args.env, "=")

    cmd = args.cmd or args.flavor.args.get("JUST_EXECUTABLE", "just")
    cont.add_argument(args.flavor.tag).add_argument(cmd)
    cont.args.extend(justargs)

    cont_cp = cont.run()
    if cont_cp.returncode != 0:
        eecho("Failed to create a container")
        sys.exit(cont_cp.returncode)

    container_id = cont_cp.stdout.strip()
    if not container_id:  # sanity check
        eecho("Invalid ID of new container")
        sys.exit(1)

    weakref.finalize(cont, purge_container, container_id)

    if args.workspace and args.copy_workspace:
        copy_cp = DockerCommand(["cp", workpath, f"{container_id}:/workspace"]).run()
        if copy_cp.returncode != 0:
            eecho("Couldn't copy {workpath} into container")
            DockerCommand(["rm", "--force", container_id]).run()
            sys.exit(copy_cp.returncode)

    cp = start.add_argument(container_id).run(capture=False)
    retcode = cp.returncode

    for cont_path, host_path in args.copy_back.items():
        copy_cp = engine(
            "cp",
            f"{container_id}:{cont_path}",
            host_path,
            capture=False,
            exit_on_error=False,
        )
        if copy_cp.returncode > 0:
            eecho(f"Failed to copy back '{cont_path}'.")
            if retcode == 0:
                retcode = 1

    sys.exit(retcode)


@cli.command(context_settings={"ignore_unknown_options": True})
@click.argument("justargs", nargs=-1, type=click.UNPROCESSED)
@click.pass_context
def justw(ctx, justargs) -> None:
    """Run just container with current directory mounted as a workspace.

    This is shorthand for 'justin --workspace . just ...'"""
    args: Args = ctx.obj
    if not args.workspace:
        args.workspace = Path()

    return ctx.forward(just)


@cli.command()
@click.argument("destination")
@click.pass_obj
def publish(args, destination) -> None:
    """Publish the flavor to the registry.

    This is a helper command which publishes the selected justin flavor in
    the container registry. Users usually are permitted to publish images only
    to certain namespaces which are reflected in tags of online images.

    The behavior of choosing a default registry when destination doesn't
    contain a registry URL depends on used container engine.

    Destination may contain a {tag} placeholder, which will be replaced with
    the local tag of used flavor."""

    remote_tag = destination if destination else args.flavor.tag
    remote_tag = remote_tag.format(tag=args.flavor.tag)

    # optimisation: podman supports specifying a destination without a
    # braindead re-tagging
    if args.engine == "podman":
        cp = engine("push", args.flavor.tag, remote_tag, capture=False)
        sys.exit(cp.returncode)

    engine("tag", args.flavor.tag, remote_tag, capture=False, exit_on_error=True)
    sys.exit(engine("push", remote_tag, capture=False).returncode)


@cli.command()
@click.argument("source")
@click.pass_obj
def pull(args, source) -> None:
    """Get image flavor from the registry.

    Image pulled from the registry will be locally recognised as a justin image.

    The behavior of choosing a default registry when source doesn't contain a
    registry URL depends on used container engine."""

    echo("Pulling the image (output might be suppressed)...", err=True)
    out = engine("pull", source, exit_on_error=True)
    lines = out.stdout.splitlines()
    if not lines:
        eecho(f"{args.engine} pull didn't report a downloaded image")
        sys.exit(1)

    image = lines[-1]  # hopefully...
    engine("tag", image, args.flavor.tag, exit_on_error=True)
    engine(
        "inspect",
        "--format",
        "{{index .RepoDigests 0}}",
        args.flavor.tag,
        exit_on_error=True,
        capture=False,
    )


@cli.command()
@click.option(
    "--names-only", is_flag=True, default=False, help="show only flavor names"
)
@click.pass_obj
def flavors(args, names_only) -> None:
    """List available flavors"""

    for flavor, path in list_flavors(args.flavor_search_paths).items():
        if names_only:
            echo(flavor)
        else:
            echo(f"{flavor}:{path}")


@cli.command
@click.option(
    "-c",
    "--config",
    "config_paths",
    required=True,
    metavar="HOST.TOML[:CONTAINER.TOML]",
    callback=validate_config_paths,
    help=(
        "paths to the TOML file on the host and within the container. When container "
        "part isn't set, config is assumed to be relative to the workspace."
    ),
)
@click.argument("stages", nargs=-1, type=click.UNPROCESSED)
@click.pass_context
def toml(ctx, config_paths, stages) -> None:
    """Run just on stages from a toml file.

    In this mode the rules apply:

        - if any stages are specified on a command line, justin will run these
          instead of stages specified in the configuration file

        - --flavor sets a default flavor which will be used when
          stage.<name>.flavor doesn't exist.

        - default justfile for all stages is '<config.stem>.justfile'
    """
    args: Args = ctx.obj
    config_path_host, config_path_container = config_paths

    def set_defaults(config: dict) -> dict:
        config.setdefault("justfile", f"{config_path_host.stem}.justfile")
        conf_stages = config.setdefault("stages", [""])
        subs_stage = config.setdefault("stage", {})

        additional_stages = list(stages) or []
        for stage in conf_stages + additional_stages:
            subs_stage_specific = subs_stage.setdefault(stage, {})
            subs_stage_specific.setdefault("flavor", args.flavor.name)
        return config

    config = set_defaults(load_toml(config_path_host))

    if not stages:
        stages = config["stages"]

    if len(set(stages)) != len(stages):
        eecho("error: duplicated stages")
        sys.exit(1)

    for stagename in stages:
        stageconf = config["stage"][stagename]

        args.flavor = find_flavor(stageconf["flavor"], args.flavor_search_paths)

        # justfile in is specified relative to the config's directory
        justfile = config_path_container.parent / config["justfile"]
        justargs = ["--justfile", str(justfile)]
        if stagename:
            justargs.append(stagename)

        sn = stagename or "(default)"
        echo(
            f"Running stage: {sn} [flavor: {args.flavor.name}]",
            fg="green",
            bold=True,
            err=True,
        )
        try:
            ctx.invoke(just, justargs=justargs)
        except SystemExit as se:
            if se.code != 0:
                eecho(f"Stage '{sn}' failed, code={se.code}. Pipeline stopped.")
                raise
            echo(f"Stage '{sn}' succeeded.", fg="green", err=True)
