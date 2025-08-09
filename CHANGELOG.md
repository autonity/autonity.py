# Changelog

<!--
----------------------------
      Common Changelog
----------------------------
https://common-changelog.org
----------------------------

Template:

## [vX.Y.Z] - YYYY-MM-DD

### Changed

### Added

### Removed

### Fixed
-->

## [v5.1.0] - 2024-12-12

### Changed

- Ignore patch releases when checking protocol version ([#78](https://github.com/autonity/autonity.py/pull/78))

### Removed

- Remove the `networks` module ([#79](https://github.com/autonity/autonity.py/pull/79))

## [v5.0.0] - 2024-12-11

### Changed

- **Breaking:** rework Autonity contract bindings ([#59](https://github.com/autonity/autonity.py/pull/59))
- Support the Autonity Tiber protocol ([#72](https://github.com/autonity/autonity.py/pull/72))
- Update web3.py version to `7.6.0` ([`d5c75b2`](https://github.com/autonity/autonity.py/commit/d5c75b2))

### Added

- Add bindings for all remaining protocol contracts ([#73](https://github.com/autonity/autonity.py/issues/73))
- Add constants for Piccadilly (Tiber) Testnet ([`12e71d8`](https://github.com/autonity/autonity.py/commit/12e71d8))
- Support Python 3.13 ([`6046cfc`](https://github.com/autonity/autonity.py/commit/6046cfc))

### Removed

- Remove the binding for ERC20 tokens ([`8cb1ed4`](https://github.com/autonity/autonity.py/commit/8cb1ed4bdb1665dd9efb7b39ba3f504f9ebc04a1))
- Drop support for Python 3.8 ([`6046cfc`](https://github.com/autonity/autonity.py/commit/6046cfc))

## [v4.0.0] - 2024-07-02

### Changed

- Support the Autonity Yamuna protocol ([#53](https://github.com/autonity/autonity.py/issues/53))
- Update web3.py to `6.19.0` ([`1a2ca6b`](https://github.com/autonity/autonity.py/commit/1a2ca6b))

### Fixed

- Fix error in code example in the README ([`2600363`](https://github.com/autonity/autonity.py/commit/2600363))

## [v3.0.0] - 2024-03-05

### Changed

- Support the Autonity Sumida protocol ([`bb982c6`](https://github.com/autonity/autonity.py/commit/bb982c6))
- Update web3.py to `6.14.0` and support Python 3.12 ([`35965fb`](https://github.com/autonity/autonity.py/commit/35965fb))

### Fixed

- Fix `AssertionError` when contract call returns multiple values ([#45](https://github.com/autonity/autonity.py/pull/45))

## [v2.0.0] - 2024-01-11

### Changed

- Support the Autonity Barada protocol ([`0c2d3c4`](https://github.com/autonity/autonity.py/commit/0c2d3c4))
- Rename LNEW -> LNTN consistent with protocol ([`42398e7`](https://github.com/autonity/autonity.py/commit/42398e7))

### Added

### Fixed

- Fix import failure due to `ModuleNotFoundError` from eth-rlp ([#41](https://github.com/autonity/autonity.py/issues/41))

## [v1.0.1] - 2023-06-07

### Fixed

- Update README install instructions to use PyPI not Github ([`409dc98`](https://github.com/autonity/autonity.py/commit/409dc98))

## [v1.0.0] - 2023-05-26

### Changed

- Support the Autonity Contract matching `v0.10.1` ([#26](https://github.com/autonity/autonity.py/issues/26))
- Migrate code base to use web3.py `v6` ([#22](https://github.com/autonity/autonity.py/issues/22))
- Switch to the Hatch project framework ([`ed26b9f`](https://github.com/autonity/autonity.py/commit/ed26b9f))

### Added

- Add ABI Parser to convert between string<->ABI types ([#17](https://github.com/autonity/autonity.py/pull/17))
- Support Python 3.11 ([#22](https://github.com/autonity/autonity.py/issues/22))

## [v0.1.0] - 2023-01-24

_First release._

<!-- [vX.Y.Z]: https://github.com/autonity/autonity.py/releases/tag/vX.Y.Z -->
[v5.1.0]: https://github.com/autonity/autonity.py/releases/tag/v5.1.0
[v5.0.0]: https://github.com/autonity/autonity.py/releases/tag/v5.0.0
[v4.0.0]: https://github.com/autonity/autonity.py/releases/tag/v4.0.0
[v3.0.0]: https://github.com/autonity/autonity.py/releases/tag/v3.0.0
[v2.0.0]: https://github.com/autonity/autonity.py/releases/tag/v2.0.0
[v1.0.1]: https://github.com/autonity/autonity.py/releases/tag/v1.0.1
[v1.0.0]: https://github.com/autonity/autonity.py/releases/tag/v1.0.0
[v0.1.0]: https://github.com/autonity/autonity.py/releases/tag/v0.1.0
