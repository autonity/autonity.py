"""Factory functions that find the addresses of Autonity protocol contracts and return
the contract bindings.
"""

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
    """Accountability contract binding factory.

    Parameters
    ----------
    w3 : web3.Web3
        A `web3.Web3` instance with a provider connected to an Autonity network.

    Returns
    -------
    autonity.contracts.accountability.Accountability
        A contract binding instance.
    """
    return accountability.Accountability(
        w3, _config(w3).contracts.accountability_contract
    )


def ACU(w3: Web3) -> acu.ACU:
    """ACU contract binding factory.

    Parameters
    ----------
    w3 : web3.Web3
        A `web3.Web3` instance with a provider connected to an Autonity network.

    Returns
    -------
    autonity.contracts.acu.ACU
        A contract binding instance.
    """
    return acu.ACU(w3, _config(w3).contracts.acu_contract)


def Autonity(w3: Web3) -> autonity.Autonity:
    """Autonity contract binding factory.

    Parameters
    ----------
    w3 : web3.Web3
        A `web3.Web3` instance with a provider connected to an Autonity network.

    Returns
    -------
    autonity.contracts.autonity.Autonity
        A contract binding instance.
    """
    assert _config(w3)
    return autonity.Autonity(w3, AUTONITY_CONTRACT_ADDRESS)


def InflationController(w3: Web3) -> inflation_controller.InflationController:
    """InflationController contract binding factory.

    Parameters
    ----------
    w3 : web3.Web3
        A `web3.Web3` instance with a provider connected to an Autonity network.

    Returns
    -------
    autonity.contracts.inflation_controller.InflationController
        A contract binding instance.
    """
    return inflation_controller.InflationController(
        w3, _config(w3).contracts.inflation_controller_contract
    )


def Liquid(w3: Web3, address: ChecksumAddress) -> liquid.Liquid:
    """Liquid contract binding factory.

    Parameters
    ----------
    w3 : web3.Web3
        A `web3.Web3` instance with a provider connected to an Autonity network.
    address : eth_typing.ChecksumAddress
        The address of a deployed Liquid contract.

    Returns
    -------
    autonity.contracts.liquid.Liquid
        A contract binding instance.
    """
    assert _config(w3)
    return liquid.Liquid(w3, address)


def NonStakableVesting(w3: Web3) -> non_stakable_vesting.NonStakableVesting:
    """NonStakableVesting contract binding factory.

    Parameters
    ----------
    w3 : web3.Web3
        A `web3.Web3` instance with a provider connected to an Autonity network.

    Returns
    -------
    autonity.contracts.non_stakable_vesting.NonStakableVesting
        A contract binding instance.
    """
    return non_stakable_vesting.NonStakableVesting(
        w3, _config(w3).contracts.non_stakable_vesting_contract
    )


def Oracle(w3: Web3) -> oracle.Oracle:
    """Oracle contract binding factory.

    Parameters
    ----------
    w3 : web3.Web3
        A `web3.Web3` instance with a provider connected to an Autonity network.

    Returns
    -------
    autonity.contracts.oracle.Oracle
        A contract binding instance.
    """
    return oracle.Oracle(w3, _config(w3).contracts.oracle_contract)


def Stabilization(w3: Web3) -> stabilization.Stabilization:
    """Stabilization contract binding factory.

    Parameters
    ----------
    w3 : web3.Web3
        A `web3.Web3` instance with a provider connected to an Autonity network.

    Returns
    -------
    autonity.contracts.stabilization.Stabilization
        A contract binding instance.
    """
    return stabilization.Stabilization(w3, _config(w3).contracts.stabilization_contract)


def SupplyControl(w3: Web3) -> supply_control.SupplyControl:
    """SupplyControl contract binding factory.

    Parameters
    ----------
    w3 : web3.Web3
        A `web3.Web3` instance with a provider connected to an Autonity network.

    Returns
    -------
    autonity.contracts.supply_control.SupplyControl
        A contract binding instance.
    """
    return supply_control.SupplyControl(
        w3, _config(w3).contracts.supply_control_contract
    )


def UpgradeManager(w3: Web3) -> upgrade_manager.UpgradeManager:
    """UpgradeManager contract binding factory.

    Parameters
    ----------
    w3 : web3.Web3
        A `web3.Web3` instance with a provider connected to an Autonity network.

    Returns
    -------
    autonity.contracts.upgrade_manager.UpgradeManager
        A contract binding instance.
    """
    return upgrade_manager.UpgradeManager(
        w3, _config(w3).contracts.upgrade_manager_contract
    )
