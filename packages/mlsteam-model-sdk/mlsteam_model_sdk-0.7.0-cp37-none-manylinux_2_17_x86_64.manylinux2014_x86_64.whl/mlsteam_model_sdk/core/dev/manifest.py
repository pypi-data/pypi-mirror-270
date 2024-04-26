"""Manifest file operations"""
import dataclasses
import enum
import functools
import json
import pathlib
from dataclasses import dataclass
from typing import BinaryIO, List, NamedTuple, Optional, Sequence, Tuple, TextIO, Union

import jsonschema
import jsonschema.exceptions

from mlsteam_model_sdk.core.exceptions import InvalidManifestException


@functools.total_ordering
class ManifestSchema(enum.Enum):
    """Manifest version"""
    V2023_1 = 'v2023.1'
    V2024_1 = 'v2024.1'
    LATEST = V2024_1

    @classmethod
    def from_manifest(cls, manifest: dict) -> 'ManifestSchema':
        """Gets version from manifest"""
        schema_val = manifest.get('schema', cls.V2023_1.value)
        try:
            return ManifestSchema(schema_val)
        except ValueError:
            if cls.may_be_future(schema_val):
                raise InvalidManifestException(
                    f'invalid schema {schema_val},' +
                    ' may be a future schema not support by the current installation of SDK'
                ) from None
            raise InvalidManifestException(f'invalid schema {schema_val}') from None

    @property
    def parts(self) -> Tuple[int, int]:
        """Gets version parts (year_part, sub_part)"""
        return self.get_parts(self.value)

    def __lt__(self, other: 'ManifestSchema'):
        if self.__class__ is other.__class__:
            return self.parts < other.parts
        return NotImplemented

    @classmethod
    def may_be_future(cls, val: str) -> bool:
        """Tests whether the given schema value may indicate a future schema not understood by the current SDK"""
        try:
            other_parts = cls.get_parts(val)
            return cls.LATEST.parts < other_parts
        except (IndexError, ValueError):
            return False

    @classmethod
    def get_parts(cls, val: str) -> Tuple[int, int]:
        """Gets version parts (year_part, sub_part) from a given value"""
        _parts = val[1:].split('.', maxsplit=1)
        return int(_parts[0]), int(_parts[1])


class Manifest(NamedTuple):
    """Manifest reading result"""
    manifest: dict
    schema: ManifestSchema


@dataclass
class ModelLoaderDictSpec:
    """Specifies a submodel loader hook (dict format) in manifest."""
    built_in: Optional[str] = None
    file: Optional[str] = None
    function: Optional[str] = None

    def to_dict(self) -> dict:
        if self.built_in:
            return {'built-in': self.built_in}
        if not self.file:
            raise ValueError(f'Neither built-in nor file is specified: {repr(self)}')
        ret = {'file': self.file}
        if self.function:
            ret['function'] = self.function
        return ret


@dataclass
class SubmodelSpec:
    """Specifies a submodel in manifest."""
    name: str
    description: Optional[str] = None
    loader: Union[str, ModelLoaderDictSpec, None] = None
    in_memory_model_extraction: Optional[bool] = None
    enc_model_cleanup: Optional[str] = None
    enc_model_cleanup_files: Optional[Sequence[str]] = None

    def to_dict(self) -> dict:
        ret = {}
        for f in dataclasses.fields(self):
            if 'val' not in dir():
                val = NotImplemented

            def _walrus_wrapper_val_edb2799e3cca45f796036c6fc33e3877(expr):
                """Wrapper function for assignment expression."""
                nonlocal val
                val = expr
                return val

            if (_walrus_wrapper_val_edb2799e3cca45f796036c6fc33e3877(getattr(self, f.name))) is None:
                continue
            if f.name == 'loader':
                if isinstance(val, ModelLoaderDictSpec):
                    val = val.to_dict()
            ret[f.name] = val
        return ret


@dataclass
class ServicePredictorDictSpec:
    """Specifies an inference service predictor hook (dict format) in manifest."""
    built_in: Optional[str] = None
    file: Optional[str] = None
    function: Optional[str] = None

    def to_dict(self) -> dict:
        if self.built_in:
            return {'built-in': self.built_in}
        if not self.file:
            raise ValueError(f'Neither built-in nor file is specified: {repr(self)}')
        ret = {'file': self.file}
        if self.function:
            ret['function'] = self.function
        return ret


@dataclass
class ServiceSpec:
    """Specifies an inference service in manifest."""
    name: str
    predictor: Union[str, ServicePredictorDictSpec, None] = None

    def to_dict(self) -> dict:
        ret = {'name': self.name}
        if self.predictor:
            if isinstance(self.predictor, ServicePredictorDictSpec):
                ret['predictor'] = self.predictor.to_dict()
        return ret


class ManifestValidator:
    """Manifest validator"""

    @classmethod
    def validate(cls, manifest: dict, schema: Optional[ManifestSchema] = None):
        """Validates manifest"""
        if schema is None:
            schema = ManifestSchema.from_manifest(manifest)

        if schema >= ManifestSchema.V2024_1:
            for subm in manifest['models']:
                subm_name = subm['name']

                if 'subm_loader' not in dir():
                    subm_loader = NotImplemented

                def _walrus_wrapper_subm_loader_93767d8d9e68475db01bc56bdabed623(expr):
                    """Wrapper function for assignment expression."""
                    nonlocal subm_loader
                    subm_loader = expr
                    return subm_loader

                if (_walrus_wrapper_subm_loader_93767d8d9e68475db01bc56bdabed623(subm.get('loader'))):
                    if isinstance(subm_loader, str):
                        cls._val_relative_path(subm_loader)
                    elif 'built-in' in subm_loader:
                        continue
                    elif 'file' in subm_loader:
                        cls._val_relative_path(subm_loader['file'])
                    else:
                        raise InvalidManifestException(
                            f'Invalid submodel {subm_name}:' +
                            ' should be a path or a dict with "built-in" or "file" propeerties'
                        )

    @classmethod
    def _val_relative_path(cls, path: Union[str, pathlib.Path]):
        if isinstance(path, str):
            path = pathlib.Path(path)
        if path.is_absolute() or '..' in path.parts:
            raise InvalidManifestException(f'{str(path)} should be a relative path not targeting parent directories')


def read_manifest(manifest: Union[TextIO, BinaryIO, None] = None,
                  manifest_file: str = 'manifest.json', validate=False) -> Manifest:
    """Reads (and optionally validates) manifest.

    Returns:
      (manifest, schema)
    """
    if manifest:
        manifest_dict = json.load(manifest)
    else:
        with open(manifest_file, 'rt', encoding='utf8') as fp:
            manifest_dict = json.load(fp)
    schema = ManifestSchema.from_manifest(manifest_dict)
    try:
        schema_file = pathlib.Path(__file__).parent.parent / 'mlarchive_manifest_schema' / (schema.value + '.json')
        with schema_file.open('rt', encoding='utf8') as fp:
            schema_obj = json.load(fp)
        jsonschema.validate(manifest_dict, schema_obj)
        if validate:
            ManifestValidator.validate(manifest_dict, schema)
        return Manifest(manifest_dict, schema)
    except jsonschema.exceptions.ValidationError as err:
        # NOTE: more user-friendly error messages
        # https://python-jsonschema.readthedocs.io/en/stable/errors/
        # https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/validators/
        # jsonschema.validators.validator_for(), iter_errors()...
        raise ValueError(f'manifest schema validation error: {err.message}') from err


def gen_manifest(name: str, version: str,
                 bare_models: Optional[Sequence[str]] = None,
                 models: Optional[Sequence[SubmodelSpec]] = None,
                 services: Optional[Sequence[ServiceSpec]] = None,
                 schema: Optional[ManifestSchema] = None,
                 in_memory_model_extraction: Optional[bool] = None,
                 file_integrity_check_models: Optional[str] = None,
                 file_integrity_check_hooks: Optional[str] = None,
                 file_integrity_check_src: Optional[str] = None,
                 file_integrity_check_manifest: Optional[str] = None,
                 orig_manifest: Optional[dict] = None,
                 hooks_dir: Optional[str] = None,
                 validate=False) -> Tuple[dict, List[str]]:
    """Generates a manifest skeleton.

    Returns:
      A tuple (manifest, hints)
    """
    hints = []
    orig_manifest = orig_manifest or {}

    if not schema:
        schema = ManifestSchema(orig_manifest.get('schema', ManifestSchema.V2024_1.value))

    model_dicts = [m.to_dict() for m in (models or [])]
    if bare_models:
        orig_models = orig_manifest.get('models', [])
        hint_enc_model_cleanup = False
        for subm_name in bare_models:
            if 'orig_model_match' not in dir():
                orig_model_match = NotImplemented

            def _walrus_wrapper_orig_model_match_2b83187fe1074da4bb5531de715aa6b2(expr):
                """Wrapper function for assignment expression."""
                nonlocal orig_model_match
                orig_model_match = expr
                return orig_model_match

            if (_walrus_wrapper_orig_model_match_2b83187fe1074da4bb5531de715aa6b2([m for m in orig_models if m['name'] == subm_name])):
                model_dicts.append(orig_model_match[0])
            else:
                model_dicts.append(SubmodelSpec(name=subm_name, enc_model_cleanup='after-load').to_dict())
                hint_enc_model_cleanup = True
        if hint_enc_model_cleanup:
            hints.append('enc-model-cleanup is enabled for added submodels.' +
                         ' You may adjust the submodel-specific settings.')

    service_dicts = [s.to_dict() for s in (services or [])]
    if not service_dicts:
        if 'orig_services' not in dir():
            orig_services = NotImplemented

        def _walrus_wrapper_orig_services_d66670b930cc4987a11bbc7412699d64(expr):
            """Wrapper function for assignment expression."""
            nonlocal orig_services
            orig_services = expr
            return orig_services

        if (_walrus_wrapper_orig_services_d66670b930cc4987a11bbc7412699d64(orig_manifest.get('services'))):
            service_dicts = orig_services
        else:
            service_dicts = [ServiceSpec(name='main').to_dict()]
            hints.append('A default service "main" is defined. You will need to adjust the settings later.')
            if not (hooks_dir and (pathlib.Path(hooks_dir) / 'load.py').exists()):
                hints.append('No loader hooks found. You may need to add them later.')
            if not (hooks_dir and (pathlib.Path(hooks_dir) / 'predict.py').exists()):
                hints.append('No predictor hooks found. You may need to add them later.')

    if in_memory_model_extraction is None:
        if 'in_memory_model_extraction' not in dir():
            in_memory_model_extraction = NotImplemented

        def _walrus_wrapper_in_memory_model_extraction_e5683ec2790546d5a336d2088b317b48(expr):
            """Wrapper function for assignment expression."""
            nonlocal in_memory_model_extraction
            in_memory_model_extraction = expr
            return in_memory_model_extraction

        if (_walrus_wrapper_in_memory_model_extraction_e5683ec2790546d5a336d2088b317b48(orig_manifest.get('in_memory_model_extraction'))) is None:
            in_memory_model_extraction = False
            hints.append('in-memory-model-extraction is disabled.' +
                         ' You may adjust the top-level or submodel-specific settings.')
    orig_fic = orig_manifest.get('file_integrity_check', {})

    def _get_fic_field(field_name, curr_val):
        if curr_val is None:
            if 'curr_val' not in dir():
                curr_val = NotImplemented

            def _walrus_wrapper_curr_val_3319e500e6a84ebbb7f67f8cbd6722c8(expr):
                """Wrapper function for assignment expression."""
                nonlocal curr_val
                curr_val = expr
                return curr_val

            if (_walrus_wrapper_curr_val_3319e500e6a84ebbb7f67f8cbd6722c8(orig_fic.get(field_name))) is None:
                curr_val = 'skip'
                hints.append(f'file-integrity-check for {field_name} is skipped.' +
                             ' You may adjust the top-level settings.')
        return curr_val

    file_integrity_check_models = _get_fic_field('models', file_integrity_check_models)
    file_integrity_check_hooks = _get_fic_field('hooks', file_integrity_check_hooks)
    file_integrity_check_src = _get_fic_field('src', file_integrity_check_src)
    file_integrity_check_manifest = _get_fic_field('manifest', file_integrity_check_manifest)

    manifest = {
        'schema': schema.value,
        'name': name,
        'version': version,
        'in_memory_model_extraction': in_memory_model_extraction,
        'file_integrity_check': {
            'models': file_integrity_check_models,
            'hooks': file_integrity_check_hooks,
            'src': file_integrity_check_src,
            'manifest': file_integrity_check_manifest
        },
        'models': model_dicts,
        'services': service_dicts
    }
    if validate:
        ManifestValidator.validate(manifest, schema)
    return manifest, hints
