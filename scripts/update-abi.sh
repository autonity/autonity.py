#!/usr/bin/bash -eu

REPO_DIR="$(realpath "$(dirname "$0")/..")"
WORKING_DIR="$(mktemp -d)"

AUTONITY_DIR="${WORKING_DIR}/autonity"
ABI_DIR="${AUTONITY_DIR}/abi"

AUTONITY_COMMIT="$(cat ${ABI_DIR}/autonity-commit.txt)"
AUTONITY_REPO_URL='https://github.com/autonity/autonity.git'

git clone ${AUTONITY_REPO_URL} "${AUTONITY_DIR}"
cd "${AUTONITY_DIR}"
git checkout ${AUTONITY_COMMIT}
make contracts
for abi_file in ./params/generated/*.abi; do
	jq --sort-keys <${abi_file} >"${ABI_DIR}/${abi_file##*/}"
done
git -C ${AUTONITY_DIR} log --no-decorate --pretty='format:%H' -n 1 >${ABI_DIR}/autonity-commit.txt
rm -rf ${WORKING_DIR}
