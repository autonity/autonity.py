from types import SimpleNamespace

from web3 import HTTPProvider

bakerloo = SimpleNamespace(
    chain_id=65010003,
    network_name="Autonity Bakerloo (Yamuna) Testnet",
    http_provider=HTTPProvider("https://rpc1.bakerloo.autonity.org/"),
    symbol="ATN",
)

piccadilly = SimpleNamespace(
    chain_id=65100003,
    network_name="Autonity Piccadilly (Yamuna) Testnet",
    http_provider=HTTPProvider("https://rpc1.piccadilly.autonity.org/"),
    symbol="ATN",
)
