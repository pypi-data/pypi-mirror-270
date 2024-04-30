#!/usr/bin/bash

set -o errexit
set -o nounset
set -o pipefail

echo "Installing packages"
packages=(
    apt-transport-https
    ca-certificates
    curl
    gawk
    git
    git-lfs
    gnupg-agent
    jq
    just
    libyaml-0-2
    pipx
    python3-pip
    python3-venv
    rsync
    software-properties-common
    ssh
    sudo
    tini
    unzip
    wget
    xz-utils
    yq
    zip
    zstd
)

apt-get update
apt-get install -y --no-install-recommends --no-install-suggests "${packages[@]}"

rm -rf /var/cache/* /var/log/* /var/lib/apt/lists/* /tmp/* || echo "Failed to delete directories"

echo "Installing CI scripts"
# special care, because Python resources don't preserve permissions
chmod +x /install/ci-scripts/*
mv /install/ci-scripts/* /usr/local/bin
rmdir /install/ci-scripts

echo "Installing entrypoint"
# special care, because Python resources don't preserve permissions
chmod +x /install/entrypoint
mv /install/entrypoint /usr/local/bin/entrypoint
