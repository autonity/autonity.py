"""Parameters of the available Autonity networks."""

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


bakerloo = Network(
    chain_id=65010003,
    network_name="Autonity Bakerloo (Yamuna) Testnet",
    http_provider=HTTPProvider("https://rpc1.bakerloo.autonity.org/"),
)
"""Network : Autonity Bakerloo (Yamuna) Testnet parameters."""

piccadilly = Network(
    chain_id=65100003,
    network_name="Autonity Piccadilly (Yamuna) Testnet",
    http_provider=HTTPProvider("https://rpc1.piccadilly.autonity.org/"),
)
"""Network : Autonity Piccadilly (Yamuna) Testnet parameters."""
