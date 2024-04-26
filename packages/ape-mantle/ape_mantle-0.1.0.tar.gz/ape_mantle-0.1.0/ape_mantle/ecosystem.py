from typing import ClassVar, Dict, Tuple, cast

from ape_ethereum.ecosystem import (
    BaseEthereumConfig,
    Ethereum,
    NetworkConfig,
    create_network_config,
)

NETWORKS = {
    # chain_id, network_id
    "mainnet": (5000, 5000),
    "testnet": (5001, 5001),
}


class MantleConfig(BaseEthereumConfig):
    NETWORKS: ClassVar[Dict[str, Tuple[int, int]]] = NETWORKS
    mainnet: NetworkConfig = create_network_config(block_time=2, required_confirmations=1)
    testnet: NetworkConfig = create_network_config(block_time=2, required_confirmations=1)


class Mantle(Ethereum):
    fee_token_symbol: str = "MNT"

    @property
    def config(self) -> MantleConfig:  # type: ignore[override]
        return cast(MantleConfig, self.config_manager.get_config("mantle"))