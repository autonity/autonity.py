"""LiquidLogic contract binding and data structures."""

# This module has been generated using pyabigen v0.2.15

import typing

import eth_typing
import web3
from web3.contract import contract


class LiquidLogic:
    """LiquidLogic contract binding.

    Parameters
    ----------
    w3 : web3.Web3
    address : eth_typing.ChecksumAddress
        The address of a deployed LiquidLogic contract.
    """

    _contract: contract.Contract

    def __init__(
        self,
        w3: web3.Web3,
        address: eth_typing.ChecksumAddress,
    ):
        self._contract = w3.eth.contract(
            address=address,
            abi=ABI,
        )

    @property
    def Approval(self) -> contract.ContractEvent:
        """Binding for `event Approval` on the LiquidLogic contract."""
        return self._contract.events.Approval

    @property
    def Transfer(self) -> contract.ContractEvent:
        """Binding for `event Transfer` on the LiquidLogic contract."""
        return self._contract.events.Transfer

    @property
    def UnbondingApproval(self) -> contract.ContractEvent:
        """Binding for `event UnbondingApproval` on the LiquidLogic contract.

        Emitted when the unbond-allowance (LNTN) of a `_caller` for an `_owner` is set
        by a call to `approveUnbonding`. `_value` is the new unbond-allowance (LNTN).
        """
        return self._contract.events.UnbondingApproval

    def commission_rate_decimals(
        self,
    ) -> int:
        """Binding for `COMMISSION_RATE_DECIMALS` on the LiquidLogic contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.COMMISSION_RATE_DECIMALS().call()
        return int(return_value)

    def commission_rate_scale_factor(
        self,
    ) -> int:
        """Binding for `COMMISSION_RATE_SCALE_FACTOR` on the LiquidLogic contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.COMMISSION_RATE_SCALE_FACTOR().call()
        return int(return_value)

    def fee_factor_unit_recip(
        self,
    ) -> int:
        """Binding for `FEE_FACTOR_UNIT_RECIP` on the LiquidLogic contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.FEE_FACTOR_UNIT_RECIP().call()
        return int(return_value)

    def fee_factor_unit_recip_decimals(
        self,
    ) -> int:
        """Binding for `FEE_FACTOR_UNIT_RECIP_DECIMALS` on the LiquidLogic contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.FEE_FACTOR_UNIT_RECIP_DECIMALS().call()
        return int(return_value)

    def allowance(
        self,
        _owner: eth_typing.ChecksumAddress,
        _spender: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `allowance` on the LiquidLogic contract.

        See {IERC20-allowance}.

        Parameters
        ----------
        _owner : eth_typing.ChecksumAddress
        _spender : eth_typing.ChecksumAddress

        Returns
        -------
        int
        """
        return_value = self._contract.functions.allowance(
            _owner,
            _spender,
        ).call()
        return int(return_value)

    def approve(
        self,
        _spender: eth_typing.ChecksumAddress,
        _amount: int,
    ) -> contract.ContractFunction:
        """Binding for `approve` on the LiquidLogic contract.

        Parameters
        ----------
        _spender : eth_typing.ChecksumAddress
        _amount : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.approve(
            _spender,
            _amount,
        )

    def approve_unbonding(
        self,
        _caller: eth_typing.ChecksumAddress,
        _amount: int,
    ) -> contract.ContractFunction:
        """Binding for `approveUnbonding` on the LiquidLogic contract.

        Sets `_amount` as the unbond-allowance (LNTN) of `_caller` over the caller's
        tokens. Returns a boolean value indicating whether the operation succeeded.
        Emits an {UnbondingApproval} event.

        Parameters
        ----------
        _caller : eth_typing.ChecksumAddress
        _amount : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.approveUnbonding(
            _caller,
            _amount,
        )

    def balance_of(
        self,
        _delegator: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `balanceOf` on the LiquidLogic contract.

        Returns the amount of liquid newtons held by the account (ERC-20).

        Parameters
        ----------
        _delegator : eth_typing.ChecksumAddress

        Returns
        -------
        int
        """
        return_value = self._contract.functions.balanceOf(
            _delegator,
        ).call()
        return int(return_value)

    def claim_rewards(
        self,
    ) -> contract.ContractFunction:
        """Binding for `claimRewards` on the LiquidLogic contract.

        Withdraws all fees earned so far by the caller.

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.claimRewards()

    def claim_treasury_atn(
        self,
    ) -> contract.ContractFunction:
        """Binding for `claimTreasuryATN` on the LiquidLogic contract.

        Send the unclaimed ATN entitled to treasury account

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.claimTreasuryATN()

    def decimals(
        self,
    ) -> int:
        """Binding for `decimals` on the LiquidLogic contract.

        Returns
        -------
        int
            uint8 the number of decimals the LNTN token uses.
        """
        return_value = self._contract.functions.decimals().call()
        return int(return_value)

    def get_commission_rate(
        self,
    ) -> int:
        """Binding for `getCommissionRate` on the LiquidLogic contract.

        Returns the current commission rate

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getCommissionRate().call()
        return int(return_value)

    def get_treasury(
        self,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `getTreasury` on the LiquidLogic contract.

        Returns the treasury of the validator associated with this liquid contract

        Returns
        -------
        eth_typing.ChecksumAddress
        """
        return_value = self._contract.functions.getTreasury().call()
        return eth_typing.ChecksumAddress(return_value)

    def get_treasury_unclaimed_atn(
        self,
    ) -> int:
        """Binding for `getTreasuryUnclaimedATN` on the LiquidLogic contract.

        Returns the ATN amount that is yet to claim by treasury. Call function
        `claimTreasuryATN()` to claim.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getTreasuryUnclaimedATN().call()
        return int(return_value)

    def get_validator(
        self,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `getValidator` on the LiquidLogic contract.

        Returns the validator associated with this liquid contract

        Returns
        -------
        eth_typing.ChecksumAddress
        """
        return_value = self._contract.functions.getValidator().call()
        return eth_typing.ChecksumAddress(return_value)

    def locked_balance_of(
        self,
        _delegator: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `lockedBalanceOf` on the LiquidLogic contract.

        Returns the amount of locked liquid newtons held by the account.

        Parameters
        ----------
        _delegator : eth_typing.ChecksumAddress

        Returns
        -------
        int
        """
        return_value = self._contract.functions.lockedBalanceOf(
            _delegator,
        ).call()
        return int(return_value)

    def name(
        self,
    ) -> str:
        """Binding for `name` on the LiquidLogic contract.

        Returns the name of this liquid contract token

        Returns
        -------
        str
        """
        return_value = self._contract.functions.name().call()
        return str(return_value)

    def symbol(
        self,
    ) -> str:
        """Binding for `symbol` on the LiquidLogic contract.

        Returns the symbol of this liquid contract token

        Returns
        -------
        str
        """
        return_value = self._contract.functions.symbol().call()
        return str(return_value)

    def total_supply(
        self,
    ) -> int:
        """Binding for `totalSupply` on the LiquidLogic contract.

        Returns the total amount of stake token issued.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.totalSupply().call()
        return int(return_value)

    def transfer(
        self,
        _to: eth_typing.ChecksumAddress,
        _amount: int,
    ) -> contract.ContractFunction:
        """Binding for `transfer` on the LiquidLogic contract.

        Moves `_amount` LNEW tokens from the caller's account to the recipient `_to`.

        Parameters
        ----------
        _to : eth_typing.ChecksumAddress
        _amount : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.transfer(
            _to,
            _amount,
        )

    def transfer_from(
        self,
        _sender: eth_typing.ChecksumAddress,
        _recipient: eth_typing.ChecksumAddress,
        _amount: int,
    ) -> contract.ContractFunction:
        """Binding for `transferFrom` on the LiquidLogic contract.

        Parameters
        ----------
        _sender : eth_typing.ChecksumAddress
        _recipient : eth_typing.ChecksumAddress
        _amount : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.transferFrom(
            _sender,
            _recipient,
            _amount,
        )

    def unbonding_allowance(
        self,
        _owner: eth_typing.ChecksumAddress,
        _caller: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `unbondingAllowance` on the LiquidLogic contract.

        Returns the remaining number of LNTN that `_caller` will be allowed to unbond on
        behalf of `_owner` through `unbondFrom`. This is zero by default.

        Parameters
        ----------
        _owner : eth_typing.ChecksumAddress
        _caller : eth_typing.ChecksumAddress

        Returns
        -------
        int
        """
        return_value = self._contract.functions.unbondingAllowance(
            _owner,
            _caller,
        ).call()
        return int(return_value)

    def unclaimed_rewards(
        self,
        _account: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `unclaimedRewards` on the LiquidLogic contract.

        Calculates the total claimable fees (ATN) earned by the delegator to-date.

        Parameters
        ----------
        _account : eth_typing.ChecksumAddress
            Delegator account.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.unclaimedRewards(
            _account,
        ).call()
        return int(return_value)

    def unlocked_balance_of(
        self,
        _delegator: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `unlockedBalanceOf` on the LiquidLogic contract.

        Returns the amount of unlocked liquid newtons held by the account.

        Parameters
        ----------
        _delegator : eth_typing.ChecksumAddress

        Returns
        -------
        int
        """
        return_value = self._contract.functions.unlockedBalanceOf(
            _delegator,
        ).call()
        return int(return_value)


ABI = typing.cast(
    eth_typing.ABI,
    [
        {"inputs": [], "stateMutability": "nonpayable", "type": "constructor"},
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "owner",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "spender",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "value",
                    "type": "uint256",
                },
            ],
            "name": "Approval",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "from",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "to",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "value",
                    "type": "uint256",
                },
            ],
            "name": "Transfer",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "_owner",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "_caller",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "_value",
                    "type": "uint256",
                },
            ],
            "name": "UnbondingApproval",
            "type": "event",
        },
        {"stateMutability": "payable", "type": "fallback"},
        {
            "inputs": [],
            "name": "COMMISSION_RATE_DECIMALS",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "COMMISSION_RATE_SCALE_FACTOR",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "FEE_FACTOR_UNIT_RECIP",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "FEE_FACTOR_UNIT_RECIP_DECIMALS",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_owner", "type": "address"},
                {"internalType": "address", "name": "_spender", "type": "address"},
            ],
            "name": "allowance",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_spender", "type": "address"},
                {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            ],
            "name": "approve",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_caller", "type": "address"},
                {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            ],
            "name": "approveUnbonding",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_delegator", "type": "address"}
            ],
            "name": "balanceOf",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_account", "type": "address"},
                {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            ],
            "name": "burn",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "claimRewards",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "claimTreasuryATN",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "decimals",
            "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getCommissionRate",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getTreasury",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getTreasuryUnclaimedATN",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getValidator",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_account", "type": "address"},
                {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            ],
            "name": "lock",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_account", "type": "address"},
                {"internalType": "address", "name": "_caller", "type": "address"},
                {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            ],
            "name": "lockFrom",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_delegator", "type": "address"}
            ],
            "name": "lockedBalanceOf",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_account", "type": "address"},
                {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            ],
            "name": "mint",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "name",
            "outputs": [{"internalType": "string", "name": "", "type": "string"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "_ntnReward", "type": "uint256"}
            ],
            "name": "redistribute",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "_rate", "type": "uint256"}],
            "name": "setCommissionRate",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "symbol",
            "outputs": [{"internalType": "string", "name": "", "type": "string"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "totalSupply",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_to", "type": "address"},
                {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            ],
            "name": "transfer",
            "outputs": [{"internalType": "bool", "name": "_success", "type": "bool"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_sender", "type": "address"},
                {"internalType": "address", "name": "_recipient", "type": "address"},
                {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            ],
            "name": "transferFrom",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_owner", "type": "address"},
                {"internalType": "address", "name": "_caller", "type": "address"},
            ],
            "name": "unbondingAllowance",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_account", "type": "address"}
            ],
            "name": "unclaimedRewards",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_account", "type": "address"},
                {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            ],
            "name": "unlock",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_delegator", "type": "address"}
            ],
            "name": "unlockedBalanceOf",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {"stateMutability": "payable", "type": "receive"},
    ],
)
