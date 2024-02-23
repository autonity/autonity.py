#!/usr/bin/bash -eu

REPO_DIR="$(realpath "$(dirname "$0")/..")"
ABI_DIR="${REPO_DIR}/autonity/abi"
WORKING_DIR="$(mktemp -d)"

AUTONITY_COMMIT="${1:-$(cat ${ABI_DIR}/autonity-commit.txt)}"
AUTONITY_REPO_URL='https://github.com/autonity/autonity.git'

if [[ $# -gt 1 ]]; then
    echo "usage: $0 [AUTONITY_COMMIT]"
    exit 1
fi

git clone ${AUTONITY_REPO_URL} "${WORKING_DIR}"
cd "${WORKING_DIR}"
git checkout ${AUTONITY_COMMIT}
make contracts
for abi_file in ./params/generated/*.abi; do
	jq --sort-keys <${abi_file} >"${ABI_DIR}/${abi_file##*/}"
done
git -C ${WORKING_DIR} log --no-decorate --pretty='format:%H' -n 1 >${ABI_DIR}/autonity-commit.txt
rm -rf ${WORKING_DIR}
