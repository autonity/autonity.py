# Maintainers Guide

## Development and release process

The projects needs a source tree for continuous development towards the next
version of Autonity, while still being able to publish unplanned releases
containing only hotfixes and no other changes. To make this posssible, the repo
makes use of Git branches, Git tags, and well-defined development and release
processes. The development process can be found in the
[Contributing](/README.md#contributing) section of the README, while the release
process is described in the rest of this document, including a step-by-step
checklist.

There are two long-lived Git branches:

- `master`: The latest state of the code base, containing new features and bug
  fixes for the upcoming version of Autonity. All pull requests will normally
  merged into this branch.
- `stable`: The state of the code base as of the most recent release, and
  compatible with the current live version of Autonity. Only hotfixes that meet
  the criteria in the [README](/README.md#contributing-a-hotfix) can be merged
  into this branch with a pull request. After release, any hotfixes are ported
  back to `master`.

Each release has a Git tag with the release version, which reflects the state of
the code base that was used to build the corresponding release artifacts.

## Creating and publishing a new release

The release process is based on [release branching](http://releaseflow.org)
(also known as
"[branch for release](https://trunkbaseddevelopment.com/branch-for-release/)")
with the main differences being:

- all releases are made from `stable`, both planned and unplanned hotfix
  releases
- all hotfixes are always merged to `stable` first, and only later are ported
  back to `master`

Before proceeding, copy and paste the following checklist into a new Github
issue, and then self-assign the issue. Set the issue title to the
`$RELEASE_NAME` determined below.

**Pre-requisites**:

- [ ] _Determine the release type_. A _hotfix_ release must meet the hotfix
      criteria listed in the [README](/README.md). All other releases are
      _feature_ releases.
- [ ] _Merge all changes to the appropriate branch_. Ensure all changes for the
      release are merged to the appropriate branch on the remote: _hotfix_
      changes have been merged in `stable`, and _feature_ changes have been
      merged in `master`.
- [ ] _Sync with remote `master`_. Update your local copy of `master` to match
      the remote: `git checkout master && git pull`.
- [ ] _Sync with remote `stable`_. Update your local copy of `stable` to match
      the remote: `git checkout stable && git pull`.

**Feature Release Preparation**:

- [ ] _Reset `stable` to match the state of `master`_. Reset the state of your
      local copy of `stable` to point to `master` branch, and then force-push
      the new reference:
      `git checkout stable && git reset --hard origin/master && git push --force origin stable:stable`.

**Release Checklist**:

- [ ] _Switch to the `stable` branch_. All releases are made from the `stable`
      branch.
- [ ] _Determine the `$RELEASE_NAME`_. First follow
      [Semantic Versioning](https://semver.org) to determine the appropriate
      `RELEASE_VERSION` (without a `v` prefix). Then prefix `$RELEASE_VERSION`
      with a `v` to determine the `RELEASE_NAME`, ie. `v${RELEASE_VERSION}`.
- [ ] _Prepare the Changelog_. Insert a new `CHANGELOG.md` section following
      [Common Changelog](https://common-changelog.org/). Use a dedicated commit
      so it can be cherry-picked easily to `master`. Don't hard wrap lines as it
      is less readable in plaintext. Remember to add the Github Release URL link
      at the bottom, even though the release hasn't been created yet.
- [ ] _Create the `$RELEASE_COMMIT`_. In your checkout of `stable`, run
      `hatch version $RELEASE_NAME` to bump the version. Commit the changes with
      `$RELEASE_NAME` as the commit message. This is the `RELEASE_COMMIT`.
- [ ] _Tag the `$RELEASE_COMMIT`_. Add a Git tag to the `$RELEASE_COMMIT` with
      the release name: `git tag $RELEASE_NAME stable`.
- [ ] _Push the Git tag_. As Git tags are not pushed by default, it needs an
      explicit push: `git push origin stable:$RELEASE_NAME`.
- [ ] _Build the release artifacts_. Build in a clean environment by recreating
      it with `hatch env prune`. Then `hatch build --clean`.
- [ ] _Publish to PyPI_. Push the release artifacts to the
      [Python Package Index](https://pypi.org/) with `hatch publish`. You will
      be prompted for credentials. See the Hatch guide for more info:
      [How to authenticate for index publishing](https://hatch.pypa.io/latest/how-to/publish/auth/).
- [ ] _Create the Github Release_.
      [Create a new Github Release](https://github.com/autonity/autonity.py/releases/new).
      When completing the form, select `$RELEASE_NAME` tag, add relevant content
      from the `CHANGELOG.md` entry, and mark this as the "latest release".
- [ ] _Announce the release_. Notify relevant chat and social channels about the
      release. Reach out to community managers to promote it.

**Post-release Checklist**:

- [ ] _Switch to the `master` branch_. It is necessary to update `master` with
      the changes rolled out in `stable`.
- [ ] _Port the changes back to `master`_. This includes any hotfixes as well as
      the `CHANGELOG.md` commit. If hotfixes don't apply cleanly to `master`,
      and there are significant changes required, open a pull request if the
      changes may benefit from review.
