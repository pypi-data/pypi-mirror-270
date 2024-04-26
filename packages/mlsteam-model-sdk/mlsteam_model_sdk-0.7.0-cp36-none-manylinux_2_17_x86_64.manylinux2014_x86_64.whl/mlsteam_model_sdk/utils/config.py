"""Configuration utilities"""
import configparser
import contextlib
import os
from pathlib import Path
from typing import Optional, overload

from typing_extensions import Literal

from mlsteam_model_sdk.core.exceptions import MissingConfigException


__config_path = None
__config = None
CFG_DIR = '.mlsteam-model-sdk'
CFG_FILE = 'cfg.ini'
CFG_SECTION = 'mlsteam_model_sdk'

OPTION_API_TOKEN = 'api_token'
OPTION_API_ENDPOINT = 'api_endpoint'
OPTION_DEFAULT_PUUID = 'default_puuid'
OPTION_DEFAULT_PROJECT_NAME = 'default_project_name'
OPTION_DEFAULT_MUUID = 'default_muuid'
OPTION_DEFAULT_MODEL_NAME = 'default_model_name'
OPTION_DEFAULT_ENC_MODEL_CLEANUP = 'default_enc_model_cleanup'


@overload
def get_config_path(check: Literal[True]) -> Path:
    ...


def get_config_path(check: bool = False) -> Optional[Path]:
    """Gets SDK configuration file path.

    It performs configuration discovery if such a path has not been initialized. Discovery order:
    1. current working directory
    2. home directory
    3. working directory upward

    Args:
      check: whether to check configuation existence

    Returns:
      path to the configuration file, or `None` if the file is not found and check is `False`

    Raises:
      MissingConfigException: configuration is not found (when check is `True`)
    """
    if __config_path:
        return __config_path

    # current working dir
    curr_dir = Path().absolute()

    if 'curr_file' not in dir():
        curr_file = NotImplemented

    def _walrus_wrapper_curr_file_9433b4253dd54772af5ba1856a8d2145(expr):
        """Wrapper function for assignment expression."""
        nonlocal curr_file
        curr_file = expr
        return curr_file

    if (_walrus_wrapper_curr_file_9433b4253dd54772af5ba1856a8d2145(curr_dir / CFG_DIR / CFG_FILE)).is_file():
        return curr_file

    # home dir
    with contextlib.suppress(RuntimeError):
        if 'curr_file' not in dir():
            curr_file = NotImplemented

        def _walrus_wrapper_curr_file_d3ade22ea0794e6da9a3505e12165806(expr):
            """Wrapper function for assignment expression."""
            nonlocal curr_file
            curr_file = expr
            return curr_file

        if (_walrus_wrapper_curr_file_d3ade22ea0794e6da9a3505e12165806(Path.home() / CFG_DIR / CFG_FILE)).is_file():
            return curr_file

    # working dir upward
    for _dir in curr_dir.parents:
        if 'curr_file' not in dir():
            curr_file = NotImplemented

        def _walrus_wrapper_curr_file_97457df9aec7438c8103c5cacb6dc1ca(expr):
            """Wrapper function for assignment expression."""
            nonlocal curr_file
            curr_file = expr
            return curr_file

        if (_walrus_wrapper_curr_file_97457df9aec7438c8103c5cacb6dc1ca(_dir / CFG_DIR / CFG_FILE)).is_file():
            return curr_file

    if check:
        raise MissingConfigException()

    return None


def init_config(path=None, check: bool = False):
    """Initializes SDK configuration file path.

    This function is only effective at first time. It is NOP in subsequent calls.

    NOTE: Some SDK functions initialize SDK configuration implicitly when it has not been done.
    To use a custom configuration path, it is adviced to call this function before any other SDK call.

    Args:
      path: SDK configuration file path to set. When it is not given, configuration discovery is performed.
      check: raises an exception when configuration discovery fails

    Raises:
      MissingConfigException: configuration discovery fails (when check is `True`)
    """
    global __config_path, __config

    if not __config:
        __config = configparser.ConfigParser(allow_no_value=True)

        if not path:
            path = get_config_path(check=check)
        __config_path = path
        if path:
            __config.read(path)
        else:
            __config.read_dict({})


def get_value(option: str, section: Optional[str] = None):
    """Gets configuration value.

    It initializes configuration implicitly if it has not been done.
    """
    init_config()
    try:
        if section is None:
            section = CFG_SECTION
        env_key = '_'.join([section.upper(), option.upper()])
        return os.environ[env_key]
    except KeyError:
        return __config.get(section, option, fallback=None)
