import os
from typing import Optional

from pydantic import Field, model_validator

from across_client.base.schema import BaseSchema


class Config:
    DEBUG = os.environ.get("ACROSS_DEBUG", False) == "True"
    PROD_API_URL = "https://multimessenger.across.smce.nasa.gov/api/v1/"
    DEV_API_URL = "https://dev.multimessenger.across.smce.nasa.gov/api/v1/"
    API_TOKEN = os.environ.get("ACROSS_API_TOKEN", None)

    @property
    def API_URL(self):
        if self.DEBUG:
            return self.DEV_API_URL
        else:
            return self.PROD_API_URL


config = Config()


def set_api_token(api_token: str) -> None:
    """
    Set the API token.

    Parameters
    ----------
    api_token : str
        The API token.
    """
    config.API_TOKEN = api_token


def set_debug_mode(debug: bool = True) -> bool:
    """
    Set API debug mode.

    Parameters
    ----------
    debug : bool
        The debug mode.
    """
    config.DEBUG = debug
    return config.DEBUG


class ACROSSSetConfig(BaseSchema):
    """
    Mixin to set config items via parameters.
    """

    api_token: Optional[str] = Field(exclude=True, default=None)
    debug: Optional[bool] = Field(exclude=True, default=False)

    @model_validator(mode="before")
    @classmethod
    def set_config(cls, data):
        if isinstance(data, dict):
            if "api_token" in data and data["api_token"] is not None:
                set_api_token(data["api_token"])
            if "debug" in data and data["debug"] is not None:
                set_debug_mode(data["debug"])
        else:
            if data.api_token is not None:
                set_api_token(data.api_token)
            if data.debug is not None:
                set_debug_mode(data.debug)
        return data
