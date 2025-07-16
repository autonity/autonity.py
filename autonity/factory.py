"""Factory functions that return instances of contract binding classes.

They retrieve the contract address and ensure that there is no version mismatch between
the contract and the bindings.

For convenience, the functions of this module are also available as top-level
`autonity` module variables.
"""

from functools import lru_cache
from warnings import warn

from eth_typing import ChecksumAddress
from semver import Version
from web3 import Web3

from .__version__ import __version__
from .constants import AUTONITY_CONTRACT_ADDRESS, AUTONITY_CONTRACT_VERSION
from .contracts import (
    accountability,
    acu,
    auctioneer,
    autonity,
    inflation_controller,
    liquid_logic,
    omission_accountability,
    oracle,
    stabilization,
    supply_control,
    upgrade_manager,
)


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


def Auctioneer(w3: Web3) -> auctioneer.Auctioneer:
    """Auctioneer contract binding factory.

    Parameters
    ----------
    w3 : web3.Web3
        A `web3.Web3` instance with a provider connected to an Autonity network.

    Returns
    -------
    autonity.contracts.auctioneer.Auctioneer
        A contract binding instance.
    """
    return auctioneer.Auctioneer(w3, _config(w3).contracts.auctioneer_contract)


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


def LiquidLogic(w3: Web3, address: ChecksumAddress) -> liquid_logic.LiquidLogic:
    """LiquidLogic contract binding factory.

    Parameters
    ----------
    w3 : web3.Web3
        A `web3.Web3` instance with a provider connected to an Autonity network.
    address : eth_typing.ChecksumAddress
        The address of a deployed Liquid contract.

    Returns
    -------
    autonity.contracts.liquid.LiquidLogic
        A contract binding instance.
    """
    assert _config(w3)
    return liquid_logic.LiquidLogic(w3, address)


def OmissionAccountability(w3: Web3) -> omission_accountability.OmissionAccountability:
    """OmissionAccountability contract binding factory.

    Parameters
    ----------
    w3 : web3.Web3
        A `web3.Web3` instance with a provider connected to an Autonity network.

    Returns
    -------
    autonity.contracts.non_stakable_vesting.OmissionAccountability
        A contract binding instance.
    """
    return omission_accountability.OmissionAccountability(
        w3, _config(w3).contracts.omission_accountability_contract
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


@lru_cache()
def _config(w3: Web3) -> autonity.Config:
    try:
        client_version = Version.parse(w3.client_version.split("/")[1])
        binding_version = Version.parse(autonity.__version__)
    except ValueError:
        pass
    else:
        if (
            client_version.major != binding_version.major
            or client_version.minor != binding_version.minor
        ):
            warn(
                f"Protocol version mismatch: autonity.py {__version__} supports "
                f"version {autonity.__version__}, the RPC node is running "
                f"version {w3.client_version}"
            )

    config = autonity.Autonity(w3, AUTONITY_CONTRACT_ADDRESS).get_config()
    if config.contract_version != AUTONITY_CONTRACT_VERSION:
        raise RuntimeError(
            f"Contract version mismatch: autonity.py {__version__} supports "
            f"version {AUTONITY_CONTRACT_VERSION}, the Autonity contract is "
            f"version {config.contract_version}"
        )

    return config
