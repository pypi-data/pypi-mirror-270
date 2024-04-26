"""Local model registry"""
import json
import shutil
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Union, overload

from typing_extensions import Literal

from mlsteam_model_sdk.core.exceptions import (ModelVersionExistsException,
                                               ModelVersionNotFoundException, MultipleModelVersionsException)
from mlsteam_model_sdk.utils.log import logger


class Registry:
    """Local model registry operator"""

    LOCAL_PUUID = '__local__'
    LOCAL_MUUID = '__local__'

    def __init__(self, config_dir: Path) -> None:
        """Initializes a local model registry operator.

        Args:
          config_dir: SDK configuration base directory
        """
        self._models_dir = config_dir / 'models'
        self._download_base_dir = self._models_dir / 'download'
        self._extract_base_dir = self._models_dir / 'extract'
        self._registry_file = self._models_dir / 'reg.json'

    def get_new_local_vuuid(self, dev: bool = False) -> str:
        """Generates a new local vuuid.

        NOTE: This method is not thread-safe.
        """
        prefix = 'dev-' if dev else 'local-'
        while True:
            local_vuuid = prefix + str(uuid.uuid4())[:8]
            if self.get_model_version_info(vuuid=local_vuuid) is None:
                return local_vuuid

    def get_download_base_dir(self, create: bool = False) -> Path:
        """Gets base path to download model version files or packages."""
        if create:
            self._download_base_dir.mkdir(parents=True, exist_ok=True)
        return self._download_base_dir

    def get_download_file(self, vuuid: str, packaged: bool, encrypted: bool,
                          create_dir: bool = False) -> Path:
        """Gets path to save a downloaded model version file or package."""
        download_dir = self.get_download_base_dir(create=create_dir)
        if encrypted:
            download_name = f'{vuuid}-enc.mlarchive'
        elif packaged:
            download_name = f'{vuuid}.mlarchive'
        else:
            download_name = f'{vuuid}.zip'
        return download_dir / download_name

    def get_extract_base_dir(self, create: bool = False) -> Path:
        """Gets base path to extract non-encrypted model version packages."""
        if create:
            self._extract_base_dir.mkdir(parents=True, exist_ok=True)
        return self._extract_base_dir

    def get_extract_dir(self, vuuid: str, create_dir: bool = False, cleanup: bool = False) -> Path:
        """Gets path to extract a downloaded model version package.

        Args:
          vuuid: model version uuid
          create_dir: create extraction directory if not exists
          cleanup: delete extraction directory if it exists already (only effective when create_dir is enabled)
        """
        extract_dir = self.get_extract_base_dir(create=create_dir) / vuuid
        if create_dir:
            if cleanup and extract_dir.exists():
                shutil.rmtree(str(extract_dir))
            extract_dir.mkdir(parents=True, exist_ok=True)
        return extract_dir

    def list_model_versions(self) -> Dict[str, dict]:
        """Gets information of model versions in local registry.

        Returns:
          model version dict [vuuid => model version info dict]
        """
        try:
            with self._registry_file.open('rt') as reg_file:
                reg_data = json.load(reg_file)
                return reg_data
        except FileNotFoundError as e:
            logger.warning(e)
            return {}

    @overload
    def _find_model_version(self, reg_data: dict, version_name: Optional[str],
                            muuid: Optional[str], model_name: Optional[str],
                            find_all: Literal[False]) -> str:
        ...

    @overload
    def _find_model_version(self, reg_data: dict, version_name: Optional[str],
                            muuid: Optional[str], model_name: Optional[str],
                            find_all: Literal[True]) -> List[str]:
        ...

    def _find_model_version(self, reg_data: dict, version_name: Optional[str],
                            muuid: Optional[str] = None,
                            model_name: Optional[str] = None,
                            find_all: bool = False) -> Union[str, List[str]]:
        """Gets model version uuid(s) from model and version.

        version_name is required. It has optional typing for convenience of callers.

        Returns:
          model version uuid as a string when `find_all` is not set (default);
          otherwise, model version uuids as a list of strings

        Raises:
          ModelVersionNotFoundException: required arguments are not provided,
            or no matching model is found and `find_all` is not set
        """
        if muuid:
            def model_matcher(row): return row['muuid'] == muuid
        elif model_name:
            def model_matcher(row): return row['model_name'] == model_name
        else:
            raise ModelVersionNotFoundException(muuid=muuid, model_name=model_name, version_name=version_name)
        if not version_name:
            raise ModelVersionNotFoundException(muuid=muuid, model_name=model_name, version_name=version_name)

        matches = [row['vuuid'] for row in reg_data.values() if
                   row['version_name'] == version_name and model_matcher(row)]
        if find_all:
            return matches
        try:
            return matches[0]
        except IndexError:
            raise ModelVersionNotFoundException(muuid=muuid,
                                                model_name=model_name,
                                                version_name=version_name) from None

    def get_model_version_info(self,
                               vuuid: Optional[str] = None,
                               version_name: Optional[str] = None,
                               muuid: Optional[str] = None,
                               model_name: Optional[str] = None,
                               default_muuid: Optional[str] = None,
                               suppress_warning: bool = False) -> Optional[dict]:
        """Gets information of a model version in local registry.

        A model version is specified in one of the following ways:
        - model version uuid (`vuuid`) alone
        - model (`muuid`, `model_name`, or `default_muuid`) combined with version (`version_name`)

        It returns the first matching model version.
        To get all matching model versions, call `list_model_versions()` instead.
        (It is possible to have multiple matches when a model version is specified by model name and version name.)

        Args:
          vuuid: model version uuid
          version_name: version name
          muuid: model uuid
          model_name: model name
          default_muuid: default model uuid
          suppress_warning: don't log warning message when model version is unfound

        Returns:
          model version info dict, or `None` when the model version is not found
        """
        try:
            with self._registry_file.open('rt') as reg_file:
                reg_data = json.load(reg_file)
                if not vuuid:
                    if not muuid and not model_name:
                        muuid = default_muuid
                    vuuid = self._find_model_version(
                        reg_data=reg_data, version_name=version_name,
                        muuid=muuid, model_name=model_name)
                return reg_data[vuuid]
        except (FileNotFoundError, ValueError, KeyError, ModelVersionNotFoundException) as e:
            if not suppress_warning:
                logger.warning(e)
            return None

    def set_model_version_info(self, puuid: str, muuid: str, model_name: str,
                               vuuid: str, version_name: str,
                               packaged: bool, encrypted: bool,
                               download_time: datetime,
                               dev_info: Optional[dict] = None):
        """Sets a model version record in local registry."""
        if not self._registry_file.exists():
            self._registry_file.parent.mkdir(parents=True, exist_ok=True)
            with self._registry_file.open('wt') as reg_file:
                reg_file.write('{}')
        reg_bkup_file = self._registry_file.parent / 'reg-bkup.json'
        shutil.copy2(self._registry_file, reg_bkup_file)

        try:
            with self._registry_file.open('rt+') as reg_file:
                reg_data = json.load(reg_file)
                reg_data[vuuid] = {
                    'puuid': puuid,
                    'muuid': muuid,
                    'model_name': model_name,
                    'vuuid': vuuid,
                    'version_name': version_name,
                    'packaged': packaged,
                    'encrypted': encrypted,
                    'download_time': download_time.isoformat()
                }
                if dev_info:
                    reg_data[vuuid]['dev'] = True
                    reg_data[vuuid]['dev_info'] = dev_info
                reg_file.seek(0)
                json.dump(reg_data, reg_file, indent=2)
                reg_file.write('\n')
                reg_file.truncate()
        except Exception:
            logger.error('registry update failed; attempt to restore registry')
            shutil.copy2(reg_bkup_file, self._registry_file)
            raise

    def _update_model_version_dict(self,
                                   vuuid: Optional[str] = None,
                                   version_name: Optional[str] = None,
                                   muuid: Optional[str] = None,
                                   model_name: Optional[str] = None,
                                   default_muuid: Optional[str] = None,
                                   update_dict: Optional[dict] = None):
        """Updates a model version record in registry.

        NOTE: Call this method with care to avoid breaking the registry's integrity.

        Raises:
          ModelVersionNotFoundException: no matching model is found
          MultipleModelVersionsException: there are multiple matching model versions
        """
        if not update_dict:
            return

        _vuuids = None
        with self._registry_file.open('rt+') as reg_file:
            reg_data = json.load(reg_file)
            if vuuid:
                _vuuids = [vuuid]
            else:
                if not muuid and not model_name:
                    muuid = default_muuid
                _vuuids = self._find_model_version(
                    reg_data=reg_data, version_name=version_name,
                    muuid=muuid, model_name=model_name, find_all=True)

            if len(_vuuids) == 0:
                raise ModelVersionNotFoundException(muuid=muuid, model_name=model_name, version_name=version_name)
            if len(_vuuids) > 1:
                raise MultipleModelVersionsException(muuid=muuid, model_name=model_name, version_name=version_name)
            vuuid = _vuuids[0]

            reg_data[vuuid].update(update_dict)
            reg_data[vuuid]['update_time'] = datetime.now().isoformat()
            reg_file.seek(0)
            json.dump(reg_data, reg_file, indent=2)
            reg_file.write('\n')
            reg_file.truncate()

    def delete_model_version(self,
                             vuuid: Optional[str] = None,
                             version_name: Optional[str] = None,
                             muuid: Optional[str] = None,
                             model_name: Optional[str] = None,
                             default_muuid: Optional[str] = None,
                             delete_all: bool = False):
        """Deletes one or multiple model versions from local registry.

        A model version is specified in one of the following ways:
        - model version uuid (`vuuid`) alone
        - model (`muuid`, `model_name`, or `default_muuid`) combined with version (`version_name`)

        When `vuuid` is given, it will attempt to delete the associated files
        even when the local registry is broken.

        Args:
          vuuid: model version uuid
          version_name: version name
          muuid: model uuid
          model_name: model name
          default_muuid: default model uuid
          delete_all: delete all matching model versions

        Raises:
          MultipleModelVersionsException: there are multiple matching model versions and `delete_all` is not set
        """
        _vuuids = None
        try:
            with self._registry_file.open('rt+') as reg_file:
                reg_data = json.load(reg_file)
                if vuuid:
                    _vuuids = [vuuid]
                else:
                    if not muuid and not model_name:
                        muuid = default_muuid
                    _vuuids = self._find_model_version(
                        reg_data=reg_data, version_name=version_name,
                        muuid=muuid, model_name=model_name, find_all=True)

                if _vuuids:
                    if len(_vuuids) > 1 and not delete_all:
                        raise MultipleModelVersionsException(muuid=muuid, model_name=model_name,
                                                             version_name=version_name)
                    for mv in _vuuids:
                        del reg_data[mv]
                    reg_file.seek(0)
                    json.dump(reg_data, reg_file, indent=2)
                    reg_file.write('\n')
                    reg_file.truncate()  # file could be smaller; need to truncate remaining contents
        except (FileNotFoundError, KeyError, ModelVersionNotFoundException) as e:
            logger.warning(e)

        if _vuuids:
            for mv in _vuuids:
                self._delete_model_version_files(mv)

    def rename_model_version(self,
                             vuuid: Optional[str] = None,
                             version_name: Optional[str] = None,
                             muuid: Optional[str] = None,
                             model_name: Optional[str] = None,
                             default_muuid: Optional[str] = None,
                             new_model_name: Optional[str] = None,
                             new_version_name: Optional[str] = None):
        """Rename a model version in local registry.

        A model version is specified in one of the following ways:
        - model version uuid (`vuuid`) alone
        - model (`muuid`, `model_name`, or `default_muuid`) combined with version (`version_name`)

        Args:
          vuuid: model version uuid
          version_name: version name
          muuid: model uuid
          model_name: model name
          default_muuid: default model uuid
          new_model_name: new model name
          new_version_name: new version name

        Raises:
          ModelVersionNotFoundException: no matching model is found
          ModelVersionsExistsException: a model version with the new model and version names already exists
          MultipleModelVersionsException: there are multiple matching model versions
        """
        _vuuids = None

        if not (new_model_name or new_version_name):
            return
        try:
            with self._registry_file.open('rt+') as reg_file:
                reg_data = json.load(reg_file)
                if vuuid:
                    _vuuids = [vuuid]
                else:
                    if not muuid and not model_name:
                        muuid = default_muuid
                    _vuuids = self._find_model_version(
                        reg_data=reg_data, version_name=version_name,
                        muuid=muuid, model_name=model_name, find_all=True)

                if len(_vuuids) == 0:
                    raise ModelVersionNotFoundException(muuid=muuid, model_name=model_name, version_name=version_name)
                if len(_vuuids) > 1:
                    raise MultipleModelVersionsException(muuid=muuid, model_name=model_name, version_name=version_name)
                mv = reg_data[_vuuids[0]]
                new_model_name = new_model_name or mv['model_name']
                new_version_name = new_version_name or mv['version_name']

                if new_model_name == mv['model_name'] and new_version_name == mv['version_name']:
                    return
                if self._find_model_version(reg_data=reg_data,
                                            model_name=new_model_name, version_name=new_version_name, find_all=True):
                    raise ModelVersionExistsException(model_name=new_model_name, version_name=new_version_name)

                mv['model_name'] = new_model_name
                mv['version_name'] = new_version_name
                mv['update_time'] = datetime.now().isoformat()
                reg_file.seek(0)
                json.dump(reg_data, reg_file, indent=2)
                reg_file.write('\n')
                reg_file.truncate()  # file could be smaller; need to truncate remaining contents
        except (FileNotFoundError, KeyError, ModelVersionNotFoundException) as e:
            logger.warning(e)

    def delete_model(self,
                     muuid: Optional[str] = None,
                     model_name: Optional[str] = None,
                     default_muuid: Optional[str] = None):
        """Deletes all model versions of a model from local registry.

        A model is specified by `muuid`, `model_name`, or `default_muuid`.

        Args:
          muuid: model uuid
          model_name: model name
          default_muuid: default model uuid
        """
        if muuid:
            def model_matcher(row): return row['muuid'] == muuid
        elif model_name:
            def model_matcher(row): return row['model_name'] == model_name
        elif default_muuid:
            def model_matcher(row): return row['muuid'] == default_muuid
        else:
            raise ValueError('Neither muuid nor model_name nor default_muuid is provided')

        with self._registry_file.open('rt+') as reg_file:
            reg_data = json.load(reg_file)
            for row in list(reg_data.values()):
                if model_matcher(row):
                    vuuid = row['vuuid']
                    self._delete_model_version_files(vuuid)
                    del reg_data[vuuid]
            reg_file.seek(0)
            json.dump(reg_data, reg_file, indent=2)
            reg_file.write('\n')
            reg_file.truncate()  # file could be smaller; need to truncate remaining contents

    def _delete_model_version_files(self, vuuid: str):
        """Deletes model version files.

        It attempts to delete associated files as many as possible
        even when errors occure.
        """
        if self._download_base_dir.exists():
            for _path in self._download_base_dir.iterdir():
                if (_path.is_file() and
                        _path.name.startswith(vuuid) and
                        _path.suffix in ('zip', 'mlarchive')):
                    try:
                        _path.unlink()
                    except (PermissionError,) as e:
                        logger.warning(e)

        extract_dir = self.get_extract_dir(vuuid, create_dir=False)
        if extract_dir.exists():
            self.__del_dir(extract_dir)

    @classmethod
    def __del_dir(cls, dir_path: Path):
        for _path in dir_path.iterdir():
            if _path.is_file():
                try:
                    _path.unlink()
                except (PermissionError,) as e:
                    logger.warning(e)
            else:
                cls.__del_dir(_path)

        try:
            dir_path.rmdir()
        except (PermissionError,) as e:
            logger.warning(e)
