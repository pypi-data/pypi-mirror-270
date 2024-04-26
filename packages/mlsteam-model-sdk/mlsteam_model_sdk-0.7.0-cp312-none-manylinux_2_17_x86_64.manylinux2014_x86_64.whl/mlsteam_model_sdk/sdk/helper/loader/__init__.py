"""Model archive loader interface"""
import importlib
import pathlib
import zipfile
from abc import ABC, abstractmethod
from types import ModuleType
from typing import Generic, TypeVar, Union

from mlsteam_model_sdk.sdk.helper.patch.zipfile import patch_zip_path


patch_zip_path()
PathTypes = Union[pathlib.Path, zipfile.Path]
PathT = TypeVar('PathT', bound=PathTypes)


class ModelFileLoaderBase(ABC, Generic[PathT]):
    """A low-level model file loader base class"""

    @abstractmethod
    def get_submodel_base_dir(self) -> PathT:
        """Gets base directory path for submodels."""

    @abstractmethod
    def get_submodel_dir(self, subm_name: str) -> PathT:
        """Gets the directory for a submodel"""


class FileSystemModelFileLoader(ModelFileLoaderBase[pathlib.Path]):
    """A low-level model file loader for file system"""

    def __init__(self, root: pathlib.Path) -> None:
        self.__root = root

    def get_submodel_base_dir(self) -> pathlib.Path:
        return self.__root / 'models'

    def get_submodel_dir(self, subm_name: str) -> pathlib.Path:
        return self.__root / 'models' / subm_name


class ArchiveModelFileLoader(ModelFileLoaderBase[zipfile.Path]):
    """A low-level model file loader for model archive"""

    def __init__(self, root: zipfile.ZipFile) -> None:
        self.__root = root

    def get_submodel_base_dir(self) -> zipfile.Path:
        return zipfile.Path(self.__root, 'models')

    def get_submodel_dir(self, subm_name: str) -> zipfile.Path:
        return zipfile.Path(self.__root, 'models') / subm_name


class BuiltInLoaderHub:
    """Built-in loader access hub

    It loads a loader until requested to avoid undesired runtime dependency (E.g., torch, tensorflow).
    """

    __reg = {
        'PyTorchLoader': ('.torch', 'TorchBuiltInLoader')
    }

    @classmethod
    def __get_loader(cls, mod_path: str, callable_path: str) -> 'BuiltInLoaderBase':
        loader = importlib.import_module(mod_path, package='mlsteam_model_sdk.sdk.helper.loader')
        for callable_part in callable_path.split('.'):
            loader = getattr(loader, callable_part)
        return loader

    @classmethod
    def get(cls, loader_name: str) -> 'BuiltInLoaderBase':
        """Gets a built-in loader by name"""
        try:
            loader_meta = cls.__reg[loader_name]
        except KeyError:
            raise ValueError(f'Invalid loader name: {loader_name}') from None

        return cls.__get_loader(loader_meta[0], loader_meta[1])


class BuiltInLoaderBase:
    """Built-in loader base class"""

    def __init__(self, pkg_module_path: str):
        self._pkg_module_path = pkg_module_path

    @classmethod
    def validate(cls, **kwargs):
        """Validates loader args"""

    @classmethod
    def validate_src_module_args(cls, src_module_path: pathlib.PurePath):
        """Validates source module loading args"""
        if src_module_path.is_absolute():
            raise ValueError(f'Invalid src module path {src_module_path}: should be a path relative to src directory')
        if '.' in src_module_path.parts or '..' in src_module_path.parts:
            raise ValueError(f'Invalid src module path {src_module_path}: should not contain "." or ".."')

    def _load_src_module(self, src_module_path: pathlib.PurePath) -> ModuleType:
        self.validate_src_module_args(src_module_path)
        mod_path = '.'.join([self._pkg_module_path, 'src', *(src_module_path.parts[:-1]), src_module_path.stem])
        mod = importlib.import_module(mod_path)
        return mod
