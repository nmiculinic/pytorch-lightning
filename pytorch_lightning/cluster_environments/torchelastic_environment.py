import os
from pytorch_lightning import _logger as log
from pytorch_lightning.utilities import rank_zero_warn
from pytorch_lightning.cluster_environments.cluster_environment import ClusterEnvironment


class TorchElasticEnvironment(ClusterEnvironment):

    def __init__(self):
        super().__init__()

    def master_address(self):
        if "MASTER_ADDR" not in os.environ:
            rank_zero_warn(
                "MASTER_ADDR environment variable is not defined. Set as localhost"
            )
            os.environ["MASTER_ADDR"] = "127.0.0.1"
        log.debug(f"MASTER_ADDR: {os.environ['MASTER_ADDR']}")
        master_address = os.environ.get('MASTER_ADDR')
        return master_address

    def master_port(self):
        if "MASTER_PORT" not in os.environ:
            rank_zero_warn(
                "MASTER_PORT environment variable is not defined. Set as 12910"
            )
            os.environ["MASTER_PORT"] = "12910"
        log.debug(f"MASTER_PORT: {os.environ['MASTER_PORT']}")

        port = os.environ.get('MASTER_PORT')
        return port

    def world_size(self):
        return os.environ.get('WORLD_SIZE', None)
