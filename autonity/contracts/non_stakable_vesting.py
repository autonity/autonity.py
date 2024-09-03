"""NonStakableVesting contract binding and data structures."""

# This module has been generated using pyabigen v0.2.5

import typing

import eth_typing
import web3
from web3.contract import contract

__version__ = "v0.14.0"


class Contract(typing.NamedTuple):
    """Port of `struct Contract` on the ContractBase contract."""

    current_ntn_amount: int
    withdrawn_value: int
    start: int
    cliff_duration: int
    total_duration: int
    can_stake: bool


class Schedule(typing.NamedTuple):
    """Port of `struct Schedule` on the NonStakableVesting contract."""

    start: int
    cliff_duration: int
    total_duration: int
    amount: int
    unsubscribed_amount: int
    total_unlocked: int
    total_unlocked_unsubscribed: int
    last_unlock_time: int


class NonStakableVesting:
    """NonStakableVesting contract binding.

    Parameters
    ----------
    w3 : web3.Web3
    address : eth_typing.ChecksumAddress
        The address of a deployed NonStakableVesting contract.
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

    def can_stake(
        self,
        _beneficiary: eth_typing.ChecksumAddress,
        _id: int,
    ) -> bool:
        """Binding for `canStake` on the NonStakableVesting contract.

        returns if beneficiary can stake from his contract

        Parameters
        ----------
        _beneficiary : eth_typing.ChecksumAddress
            beneficiary address
        _id : int

        Returns
        -------
        bool
        """
        return_value = self._contract.functions.canStake(
            _beneficiary,
            _id,
        ).call()
        return bool(return_value)

    def change_contract_beneficiary(
        self,
        _beneficiary: eth_typing.ChecksumAddress,
        _id: int,
        _recipient: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `changeContractBeneficiary` on the NonStakableVesting contract.

        changes the beneficiary of some contract to the _recipient address. _recipient
        can release tokens from the contract only operator is able to call the function

        Parameters
        ----------
        _beneficiary : eth_typing.ChecksumAddress
            beneficiary address whose contract will be canceled
        _id : int
            contract id numbered from 0 to (n-1); n = total contracts entitled to the
            beneficiary (excluding canceled ones)
        _recipient : eth_typing.ChecksumAddress
            whome the contract is transferred to

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.changeContractBeneficiary(
            _beneficiary,
            _id,
            _recipient,
        )

    def create_schedule(
        self,
        _amount: int,
        _start_time: int,
        _cliff_duration: int,
        _total_duration: int,
    ) -> contract.ContractFunction:
        """Binding for `createSchedule` on the NonStakableVesting contract.

        creates a new schedule, restricted to operator the schedule has totalAmount = 0
        initially. As new contracts are subscribed to the schedule, its totalAmount
        increases At any point, totalAmount of schedule is the sum of totalValue all the
        contracts that are subscribed to the schedule. totalValue of a contract can be
        calculated via _calculateTotalValue function

        Parameters
        ----------
        _amount : int
            total amount of the schedule
        _start_time : int
        _cliff_duration : int
        _total_duration : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.createSchedule(
            _amount,
            _start_time,
            _cliff_duration,
            _total_duration,
        )

    def get_contract(
        self,
        _beneficiary: eth_typing.ChecksumAddress,
        _id: int,
    ) -> Contract:
        """Binding for `getContract` on the NonStakableVesting contract.

        returns a contract entitled to _beneficiary

        Parameters
        ----------
        _beneficiary : eth_typing.ChecksumAddress
            beneficiary address
        _id : int
            contract id numbered from 0 to (n-1); n = total contracts entitled to the
            beneficiary (excluding canceled ones)

        Returns
        -------
        Contract
        """
        return_value = self._contract.functions.getContract(
            _beneficiary,
            _id,
        ).call()
        return Contract(
            int(return_value[0]),
            int(return_value[1]),
            int(return_value[2]),
            int(return_value[3]),
            int(return_value[4]),
            bool(return_value[5]),
        )

    def get_contracts(
        self,
        _beneficiary: eth_typing.ChecksumAddress,
    ) -> typing.List[Contract]:
        """Binding for `getContracts` on the NonStakableVesting contract.

        returns the list of current contracts assigned to a beneficiary

        Parameters
        ----------
        _beneficiary : eth_typing.ChecksumAddress
            address of the beneficiary

        Returns
        -------
        typing.List[Contract]
        """
        return_value = self._contract.functions.getContracts(
            _beneficiary,
        ).call()
        return [
            Contract(
                int(elem[0]),
                int(elem[1]),
                int(elem[2]),
                int(elem[3]),
                int(elem[4]),
                bool(elem[5]),
            )
            for elem in return_value
        ]

    def get_schedule(
        self,
        _id: int,
    ) -> Schedule:
        """Binding for `getSchedule` on the NonStakableVesting contract.

        Parameters
        ----------
        _id : int

        Returns
        -------
        Schedule
        """
        return_value = self._contract.functions.getSchedule(
            _id,
        ).call()
        return Schedule(
            int(return_value[0]),
            int(return_value[1]),
            int(return_value[2]),
            int(return_value[3]),
            int(return_value[4]),
            int(return_value[5]),
            int(return_value[6]),
            int(return_value[7]),
        )

    def max_allowed_duration(
        self,
    ) -> int:
        """Binding for `maxAllowedDuration` on the NonStakableVesting contract.

        The maximum duration of any schedule or contract

        Returns
        -------
        int
        """
        return_value = self._contract.functions.maxAllowedDuration().call()
        return int(return_value)

    def new_contract(
        self,
        _beneficiary: eth_typing.ChecksumAddress,
        _amount: int,
        _schedule_id: int,
    ) -> contract.ContractFunction:
        """Binding for `newContract` on the NonStakableVesting contract.

        creates a new non-stakable contract, restricted to only operator

        Parameters
        ----------
        _beneficiary : eth_typing.ChecksumAddress
            address of the beneficiary
        _amount : int
            total amount of NTN to be vested
        _schedule_id : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.newContract(
            _beneficiary,
            _amount,
            _schedule_id,
        )

    def release_all_funds(
        self,
        _id: int,
    ) -> contract.ContractFunction:
        """Binding for `releaseAllFunds` on the NonStakableVesting contract.

        used by beneficiary to transfer all unlocked NTN of some contract to his own
        address

        Parameters
        ----------
        _id : int
            id of the contract numbered from 0 to (n-1) where n = total contracts
            entitled to the beneficiary (excluding canceled ones). So any beneficiary
            can number their contracts from 0 to (n-1). Beneficiary does not need to
            know the unique global contract id which can be retrieved via
            _getUniqueContractID function

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.releaseAllFunds(
            _id,
        )

    def release_fund(
        self,
        _id: int,
        _amount: int,
    ) -> contract.ContractFunction:
        """Binding for `releaseFund` on the NonStakableVesting contract.

        used by beneficiary to transfer some amount of unlocked NTN of some contract to
        his own address

        Parameters
        ----------
        _id : int
        _amount : int
            amount of NTN to release

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.releaseFund(
            _id,
            _amount,
        )

    def set_max_allowed_duration(
        self,
        _new_max_duration: int,
    ) -> contract.ContractFunction:
        """Binding for `setMaxAllowedDuration` on the NonStakableVesting contract.

        Sets the max allowed duration of any schedule or contract

        Parameters
        ----------
        _new_max_duration : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setMaxAllowedDuration(
            _new_max_duration,
        )

    def set_total_nominal(
        self,
        _total_nominal: int,
    ) -> contract.ContractFunction:
        """Binding for `setTotalNominal` on the NonStakableVesting contract.

        Sets the totalNominal to create new contract

        Parameters
        ----------
        _total_nominal : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setTotalNominal(
            _total_nominal,
        )

    def total_contracts(
        self,
        _beneficiary: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `totalContracts` on the NonStakableVesting contract.

        returns the number of schudeled entitled to some beneficiary

        Parameters
        ----------
        _beneficiary : eth_typing.ChecksumAddress
            address of the beneficiary

        Returns
        -------
        int
        """
        return_value = self._contract.functions.totalContracts(
            _beneficiary,
        ).call()
        return int(return_value)

    def total_nominal(
        self,
    ) -> int:
        """Binding for `totalNominal` on the NonStakableVesting contract.

        The total amount of funds to create new locked non-stakable schedules. The
        balance is not immediately available at the vault. Rather the unlocked amount of
        schedules is minted at epoch end. The balance tells us the max size of a newly
        created schedule. See createSchedule()

        Returns
        -------
        int
        """
        return_value = self._contract.functions.totalNominal().call()
        return int(return_value)

    def unlocked_funds(
        self,
        _beneficiary: eth_typing.ChecksumAddress,
        _id: int,
    ) -> int:
        """Binding for `unlockedFunds` on the NonStakableVesting contract.

        returns the amount of unlocked but not yet released funds in NTN for some
        contract

        Parameters
        ----------
        _beneficiary : eth_typing.ChecksumAddress
        _id : int

        Returns
        -------
        int
        """
        return_value = self._contract.functions.unlockedFunds(
            _beneficiary,
            _id,
        ).call()
        return int(return_value)


ABI = [
    {
        "inputs": [
            {"internalType": "address payable", "name": "_autonity", "type": "address"},
            {"internalType": "address", "name": "_operator", "type": "address"},
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_beneficiary", "type": "address"},
            {"internalType": "uint256", "name": "_id", "type": "uint256"},
        ],
        "name": "canStake",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_beneficiary", "type": "address"},
            {"internalType": "uint256", "name": "_id", "type": "uint256"},
            {"internalType": "address", "name": "_recipient", "type": "address"},
        ],
        "name": "changeContractBeneficiary",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            {"internalType": "uint256", "name": "_startTime", "type": "uint256"},
            {"internalType": "uint256", "name": "_cliffDuration", "type": "uint256"},
            {"internalType": "uint256", "name": "_totalDuration", "type": "uint256"},
        ],
        "name": "createSchedule",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_beneficiary", "type": "address"},
            {"internalType": "uint256", "name": "_id", "type": "uint256"},
        ],
        "name": "getContract",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "currentNTNAmount",
                        "type": "uint256",
                    },
                    {
                        "internalType": "uint256",
                        "name": "withdrawnValue",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "start", "type": "uint256"},
                    {
                        "internalType": "uint256",
                        "name": "cliffDuration",
                        "type": "uint256",
                    },
                    {
                        "internalType": "uint256",
                        "name": "totalDuration",
                        "type": "uint256",
                    },
                    {"internalType": "bool", "name": "canStake", "type": "bool"},
                ],
                "internalType": "struct ContractBase.Contract",
                "name": "",
                "type": "tuple",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_beneficiary", "type": "address"}
        ],
        "name": "getContracts",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "currentNTNAmount",
                        "type": "uint256",
                    },
                    {
                        "internalType": "uint256",
                        "name": "withdrawnValue",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "start", "type": "uint256"},
                    {
                        "internalType": "uint256",
                        "name": "cliffDuration",
                        "type": "uint256",
                    },
                    {
                        "internalType": "uint256",
                        "name": "totalDuration",
                        "type": "uint256",
                    },
                    {"internalType": "bool", "name": "canStake", "type": "bool"},
                ],
                "internalType": "struct ContractBase.Contract[]",
                "name": "",
                "type": "tuple[]",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_id", "type": "uint256"}],
        "name": "getSchedule",
        "outputs": [
            {
                "components": [
                    {"internalType": "uint256", "name": "start", "type": "uint256"},
                    {
                        "internalType": "uint256",
                        "name": "cliffDuration",
                        "type": "uint256",
                    },
                    {
                        "internalType": "uint256",
                        "name": "totalDuration",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "amount", "type": "uint256"},
                    {
                        "internalType": "uint256",
                        "name": "unsubscribedAmount",
                        "type": "uint256",
                    },
                    {
                        "internalType": "uint256",
                        "name": "totalUnlocked",
                        "type": "uint256",
                    },
                    {
                        "internalType": "uint256",
                        "name": "totalUnlockedUnsubscribed",
                        "type": "uint256",
                    },
                    {
                        "internalType": "uint256",
                        "name": "lastUnlockTime",
                        "type": "uint256",
                    },
                ],
                "internalType": "struct NonStakableVesting.Schedule",
                "name": "",
                "type": "tuple",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "maxAllowedDuration",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_beneficiary", "type": "address"},
            {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            {"internalType": "uint256", "name": "_scheduleID", "type": "uint256"},
        ],
        "name": "newContract",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_id", "type": "uint256"}],
        "name": "releaseAllFunds",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_id", "type": "uint256"},
            {"internalType": "uint256", "name": "_amount", "type": "uint256"},
        ],
        "name": "releaseFund",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_newMaxDuration", "type": "uint256"}
        ],
        "name": "setMaxAllowedDuration",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_totalNominal", "type": "uint256"}
        ],
        "name": "setTotalNominal",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_beneficiary", "type": "address"}
        ],
        "name": "totalContracts",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "totalNominal",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "unlockTokens",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "_newUnlockedSubscribed",
                "type": "uint256",
            },
            {
                "internalType": "uint256",
                "name": "_newUnlockedUnsubscribed",
                "type": "uint256",
            },
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_beneficiary", "type": "address"},
            {"internalType": "uint256", "name": "_id", "type": "uint256"},
        ],
        "name": "unlockedFunds",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
]
