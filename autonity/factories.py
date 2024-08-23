from functools import lru_cache
from warnings import warn

from eth_typing import ChecksumAddress
from web3 import Web3

from .__version__ import __version__
from .constants import AUTONITY_CONTRACT_ADDRESS, AUTONITY_CONTRACT_VERSION
from .contracts import (
    accountability,
    acu,
    autonity,
    inflation_controller,
    liquid,
    non_stakable_vesting,
    oracle,
    stabilization,
    supply_control,
    upgrade_manager,
)


@lru_cache()
def _config(w3: Web3) -> autonity.Config:
    if w3.client_version.split("/")[1] != autonity.__version__:
        warn(
            f"Protocol version mismatch: autonity.py {__version__} supports "
            f"version {autonity.__version__}, the RPC node is running "
            f"version {w3.client_version}"
        )

    config = autonity.Autonity(w3, AUTONITY_CONTRACT_ADDRESS).config()
    if config.contract_version != AUTONITY_CONTRACT_VERSION:
        raise RuntimeError(
            f"Contract version mismatch: autonity.py {__version__} supports "
            f"version {AUTONITY_CONTRACT_VERSION}, the Autonity contract is "
            f"version {config.contract_version}"
        )

    return config


def Accountability(w3: Web3) -> accountability.Accountability:
    return accountability.Accountability(
        w3, _config(w3).contracts.accountability_contract
    )


def ACU(w3: Web3) -> acu.ACU:
    return acu.ACU(w3, _config(w3).contracts.acu_contract)


def Autonity(w3: Web3) -> autonity.Autonity:
    assert _config(w3)
    return autonity.Autonity(w3, AUTONITY_CONTRACT_ADDRESS)


def InflationController(w3: Web3) -> inflation_controller.InflationController:
    return inflation_controller.InflationController(
        w3, _config(w3).contracts.inflation_controller_contract
    )


def Liquid(w3: Web3, address: ChecksumAddress) -> liquid.Liquid:
    assert _config(w3)
    return liquid.Liquid(w3, address)


def NonStakableVesting(w3: Web3) -> non_stakable_vesting.NonStakableVesting:
    return non_stakable_vesting.NonStakableVesting(
        w3, _config(w3).contracts.non_stakable_vesting_contract
    )


def Oracle(w3: Web3) -> oracle.Oracle:
    return oracle.Oracle(w3, _config(w3).contracts.oracle_contract)


def Stabilization(w3: Web3) -> stabilization.Stabilization:
    return stabilization.Stabilization(w3, _config(w3).contracts.stabilization_contract)


def SupplyControl(w3: Web3) -> supply_control.SupplyControl:
    return supply_control.SupplyControl(
        w3, _config(w3).contracts.supply_control_contract
    )


def UpgradeManager(w3: Web3) -> upgrade_manager.UpgradeManager:
    return upgrade_manager.UpgradeManager(
        w3, _config(w3).contracts.upgrade_manager_contract
    )
