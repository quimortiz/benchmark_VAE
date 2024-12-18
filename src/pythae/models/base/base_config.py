from typing import Tuple, Union

from pydantic.dataclasses import dataclass
from dataclasses import asdict

from pythae.config import BaseConfig


@dataclass
class BaseAEConfig(BaseConfig):
    """This is the base configuration instance of the models deriving from
    :class:`~pythae.config.BaseConfig`.

    Parameters:
        input_dim (tuple): The input_data dimension (channels X x_dim X y_dim)
        latent_dim (int): The latent space dimension. Default: None.
    """

    input_dim: Union[Tuple[int, ...], None] = None
    latent_dim: int = 10
    uses_default_encoder: bool = True
    uses_default_decoder: bool = True

    @classmethod
    def from_dict(cls, config_dict):
        return cls(**config_dict)
    
    def to_dict(self):
        return asdict(self)


@dataclass
class EnvironmentConfig(BaseConfig):
    python_version: str = "3.8"
