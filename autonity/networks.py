"""Connection parameters for the available Autonity networks."""

from dataclasses import dataclass

from web3 import HTTPProvider


@dataclass(frozen=True)
class Network:
    """A record of parameters of an Autonity network.

    Attributes
    ----------
    chain_id : int
        The network's chain ID.
    network_name : str
        The network's name as available on ChainList.
    http_provider : web3.HTTPProvider
        Web3 provider that connects to the default HTTPS JSON-RPC server on the network.
    """

    chain_id: int
    network_name: str
    http_provider: HTTPProvider


piccadilly = Network(
    chain_id=65010004,
    network_name="Autonity Piccadilly (Tiber) Testnet",
    http_provider=HTTPProvider("https://rpc1.piccadilly.autonity.org/"),
)
"""Network : Autonity Piccadilly (Tiber) Testnet parameters."""
