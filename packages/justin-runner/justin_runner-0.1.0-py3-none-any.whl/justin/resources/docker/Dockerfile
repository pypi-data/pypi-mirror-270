ARG FROM_IMAGE
ARG FROM_TAG
FROM ${FROM_IMAGE}:${FROM_TAG}

ARG FLAVOR
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /tmp

COPY ./flavors/${FLAVOR}/install /install
RUN chmod +x /install/install.sh && /install/install.sh
RUN rm -rf /install

# sanity check that minimum necessary programs are installed
ARG JUST_EXECUTABLE=just
RUN type just /usr/bin/tini /usr/local/bin/entrypoint

ENTRYPOINT ["/usr/bin/tini", "--", "/usr/local/bin/entrypoint"]

# autoset
ARG VENDOR
ARG AUTHORS
ARG ARCH
ARG DESCRIPTION="justin image, flavor ${FLAVOR}"

# https://github.com/opencontainers/image-spec/blob/main/annotations.md
LABEL org.opencontainers.image.vendor="${VENDOR}"
LABEL org.opencontainers.image.authors="${AUTHORS}"
LABEL org.opencontainers.image.version="${VERSION}"
LABEL org.opencontainers.image.title="justin-${FLAVOR}-${ARCH}"
LABEL org.opencontainers.image.description="${DESCRIPTION}"
LABEL org.opencontainers.image.url="https://git.goral.net.pl/justin.git"

ARG VERSION
LABEL org.opencontainers.image.revision="${VERSION}"

ARG BUILD_DATE  
LABEL org.opencontainers.image.created="${BUILD_DATE}"
