"""Configuration file for the whole antconnect v2 python package.
"""

from urlpath import URL
from pathlib import Path


class HostUrlConfig:
    host: URL = URL("https://api-alpha.antcde.io")  # "https://api.antcde.io/"
    data_model: URL = host / "/docs/2.0/api-docs-v2.json"
    type: str = "api"
    version: str = "2.0"
    documentation: URL = host / (type + "/" + version + "/documentation")


class TokenConfig:
    endpoint: URL = URL("oauth/token")


class RequestsConfig:
    verify: bool = True
    headers: dict = {
        "Content-Type": "application/json", 
        "Accept": "application/json", 
        "Authorization": "access_token_placeholder"
        }
    _placeholder_string: str = "Bearer {}"


class AutoGenConfig:
    """config class containing variables for the auto generation of 
    the data model to python objects"""
    DEV_PATH: Path = Path(__file__).parent.parent.parent.parent / "dev"
    WRITE_JSON_PATH: Path = DEV_PATH / "testing"
    SRC_PATH: Path = DEV_PATH.parent / "src" / "ant_connect"
    TARGET_FILE: Path = SRC_PATH / "models.py"
    MODELBASECLASS_NAME: str = "ModelBaseClass"


class ThrottleConfig:
    amount: int = 120
    time_frame: int = 60