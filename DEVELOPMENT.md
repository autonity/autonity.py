# Development Guide

## Setting up the dev environment

The package uses the [Hatch](https://hatch.pypa.io) Python project manager. It
is recommended to [install Hatch](https://hatch.pypa.io/latest/install/#pipx)
using [pipx](https://pipx.pypa.io/):

```sh
pipx install hatch
```

### Installing Python interpreters (optional)

This project aims to be compatible with all the officially-supported versions of
Python. Check python.org
[Status of Python versions](https://devguide.python.org/versions/) for more
info.

To run the tests against all supported Python versions, it is necessary to
install the relevant distributions of Python. Hatch is able to download these
Python binaries into the home directory:

```console
$ hatch python install all
Installed 3.7 @ /home/develop/.local/share/hatch/pythons/3.7
Installed 3.8 @ /home/develop/.local/share/hatch/pythons/3.8
Installed 3.9 @ /home/develop/.local/share/hatch/pythons/3.9
Installed 3.10 @ /home/develop/.local/share/hatch/pythons/3.10
Installed 3.11 @ /home/develop/.local/share/hatch/pythons/3.11
Installed 3.12 @ /home/develop/.local/share/hatch/pythons/3.12
Installed pypy2.7 @ /home/develop/.local/share/hatch/pythons/pypy2.7
Installed pypy3.9 @ /home/develop/.local/share/hatch/pythons/pypy3.9
Installed pypy3.10 @ /home/develop/.local/share/hatch/pythons/pypy3.10
```

⚠️ Note that Hatch will then modify your shell configuration to add these paths
to your `$PATH`.

## Building and testing

To launch the tests across all supported Python versions, run:

```sh
hatch run test:all
```

To limit the tests to a specific Python version, add a
[`hatch run`](https://hatch.pypa.io/latest/cli/reference/#hatch-run) `+`
argument:

```sh
hatch run +py=3.12 test:all
```

To lint the code base, use the command:

```sh
hatch run lint:check
```

## Updating the contract ABIs

The script `script/update_abi.sh [AUTONITY_COMMIT]` builds the contract ABIs
using AGC at the specified Git commit ID or tag. Keys are ordered via the `jq`
tool, in order to produce deterministic output, and the results written to the
`autonity/abi` directory. Further, it normalizes the commit ID that was used.

After executing the script against a new version of the code, the diffs can be
reviewed to determine which methods have been modified, removed or added.

## Release checklist for maintainers

Prepare the release (any contributor):

- [ ] _Merge the changes_. All changes must be merged into `master` so that they
      can have stable commit IDs, which can be referenced from the Changelog.
- [ ] _Determine the next version number_. Follow the
      [Semantic Versioning](https://semver.org/) standard to determine the
      `$NEXT_VERSION` number.
- [ ] _Prepare the Changelog_. Create a new `CHANGELOG.md` section following
      [Common Changelog](https://common-changelog.org/). Don't hard wrap lines
      as it is less readable in plaintext. Remember to add the Github Release
      link at the bottom.

Make the release (maintainers only):

- [ ] _Bump the version_. Run `hatch version $NEXT_VERSION` to bump the version.
      Commit the changes with `$NEXT_VERSION` as the commit message.
- [ ] _Tag the version commit_. Tag this version bump Git commit with the
      version number: `git tag $NEXT_VERSION master`.
- [ ] _Push the tag_. As Git tags are not pushed by default, it needs an
      explicit push: `git push origin $NEXT_VERSION`.
- [ ] _Build the release artifacts_. Build in a clean environment by recreating
      it with `hatch env prune`. Then `hatch build --clean`.
- [ ] _Publish to PyPI_. Push the release artifacts to the
      [Python Package Index](https://pypi.org/) with `hatch publish`. You will
      be prompted for credentials. See also the Hatch guide:
      [How to authenticate for index publishing](https://hatch.pypa.io/latest/how-to/publish/auth/).
- [ ] _Create the Github Release_.
      [Create a new Github Release](https://github.com/autonity/autonity.py/releases/new).
      When completing the form, select the `$NEXT_VERSION` tag, add relevant
      content from the `CHANGELOG.md` entry, and mark this as the "latest
      release".
- [ ] _Announce the release_. Notify relevant chat and social channels about the
      release. Reach out to community managers to promote it.
