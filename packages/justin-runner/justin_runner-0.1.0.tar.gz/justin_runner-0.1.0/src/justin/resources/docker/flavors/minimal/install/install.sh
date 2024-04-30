#!/usr/bin/bash

set -o errexit
set -o nounset
set -o pipefail

echo "Installing packages"
packages=(
    just
    tini
)

apt-get update
apt-get install -y --no-install-recommends --no-install-suggests "${packages[@]}"

rm -rf /var/cache/* /var/log/* /var/lib/apt/lists/* /tmp/* || echo "Failed to delete directories"

echo "Installing entrypoint"
# special care, because Python resources don't preserve permissions
chmod +x /install/entrypoint
mv /install/entrypoint /usr/local/bin/entrypoint
