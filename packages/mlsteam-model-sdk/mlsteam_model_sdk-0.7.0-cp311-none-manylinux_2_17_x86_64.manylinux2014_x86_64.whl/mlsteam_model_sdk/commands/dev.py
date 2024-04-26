import enum
import json
import os
import pathlib
import shutil
import sys
from datetime import datetime
from typing import List, Optional, Sequence

import click
from click.exceptions import BadParameter

from mlsteam_model_sdk.core.dev.archive import (ENC_PKG_FILE, SubmodelInfo, build_archive, extract_archive)
from mlsteam_model_sdk.core.dev.manifest import ManifestSchema, gen_manifest, read_manifest
from mlsteam_model_sdk.core.exceptions import ModelVersionExistsException, MultipleModelVersionsException
from mlsteam_model_sdk.core.registry import Registry
from mlsteam_model_sdk.utils.config import get_config_path

DEFAULT_EXCLUDE_PATTERNS = ('__pycache__', '*.py[cod]', '*$py.class', '.ipynb_checkpoints')


class ManifestGen(enum.Enum):
    NEVER = 'never'
    WHEN_NOT_EXISTS = 'when-not-exists'
    ALWAYS = 'always'


def _get_submodels() -> List[SubmodelInfo]:
    submodels: List[SubmodelInfo] = []
    while True:
        name = click.prompt('Submodel name (empty input to stop)', default='')
        if not name:
            if submodels:
                if click.confirm('Stop adding new submodels?'):
                    break
            else:
                if click.confirm('No submodels have been specified. Abort directly?'):
                    sys.exit(1)
            continue
        path = click.prompt(
            'Submodel path (a file or a directory, relative to the current directory or an absolute path)'
        )
        path = pathlib.Path(path).resolve()
        if not path.exists():
            click.echo('[' + click.style('x', fg='red') + '] ', nl=False)
            click.echo(f'{path} does not exist')
            continue
        submodels.append((name, str(path)))
    return submodels


def _val_and_norm_submodels(submodels: List[SubmodelInfo]) -> List[SubmodelInfo]:
    if not submodels:
        raise ValueError('no submodels are specified')
    ret = []
    for name, path in submodels:
        if not name:
            raise ValueError('empty submodel name')
        if not path:
            raise ValueError('empty submodel path')

        if 'norm_path' not in dir():
            norm_path = NotImplemented

        def _walrus_wrapper_norm_path_9d5ac292701d4eb1bf4cb96369be7e9c(expr):
            """Wrapper function for assignment expression."""
            nonlocal norm_path
            norm_path = expr
            return norm_path

        if not (_walrus_wrapper_norm_path_9d5ac292701d4eb1bf4cb96369be7e9c(pathlib.Path(path).resolve())).exists():
            raise ValueError(f'submodel path {norm_path} does not exist')
        ret.append((name, str(norm_path)))
    return ret


def _val_optional_dir(ctx, param, value) -> Optional[str]:
    if not value:
        return None
    path = click.Path(exists=True, file_okay=False, resolve_path=True).convert(value, param, ctx)
    return str(path)


def _gen_archive(reg: Registry, vuuid: str, submodels: List[SubmodelInfo], manifest_file: str,
                 src_dir: Optional[str], hooks_dir: Optional[str], encrypted: bool,
                 preserve_model_files_in_src: bool, preserve_hooks_dir_in_src: bool,
                 default_exclude_patterns: Optional[Sequence[str]]):
    archive_file = str(reg.get_download_file(vuuid, packaged=True, encrypted=encrypted, create_dir=True))
    click.echo(f'Generating archive at {archive_file}...')
    build_archive(
        archive_file=archive_file, submodels=submodels, manifest_file=manifest_file,
        src_dir=src_dir, hooks_dir=hooks_dir,
        preserve_model_files_in_src=preserve_model_files_in_src,
        preserve_hooks_dir_in_src=preserve_hooks_dir_in_src,
        default_exclude_patterns=default_exclude_patterns
    )
    extr_dir_path = reg.get_extract_dir(vuuid, create_dir=True, cleanup=True)
    click.echo(f'Extracting archive at {str(extr_dir_path)}...')
    if encrypted:
        extr_pkg_file = str(extr_dir_path / ENC_PKG_FILE)
        shutil.move(archive_file, extr_pkg_file)
    else:
        extract_archive(archive_file, str(extr_dir_path))
        os.remove(archive_file)


@click.group(help='model developer kit')
def dev():
    pass


@dev.group(help='manifest under development')
def manifest():
    pass


@manifest.command(name='check', help='validate a manifest file')
@click.option('--manifest', '-M', 'manifest_file',
              type=click.Path(exists=True, dir_okay=False, resolve_path=True), default='manifest.json',
              help='manifest file')
@click.option('--deep', is_flag=True,
              help='deep validation (including built-in hook argument validation; ' +
              'it requires relavent ML-framework libraries)')
def check_manifest(manifest_file, deep):
    from mlsteam_model_sdk.sdk.helper.loader import BuiltInLoaderHub
    from mlsteam_model_sdk.sdk.helper.predictor import BuiltInPredictorHub

    try:
        manif = read_manifest(manifest_file=manifest_file, validate=True)
        if deep and manif.schema >= ManifestSchema.V2024_1:
            submodels = [m['name'] for m in manif.manifest['models']]
            for subm in manif.manifest['models']:
                if 'builtin_hook' not in dir():
                    builtin_hook = NotImplemented

                def _walrus_wrapper_builtin_hook_4c94f98d1b644866ba3985a4cfa2a6d3(expr):
                    """Wrapper function for assignment expression."""
                    nonlocal builtin_hook
                    builtin_hook = expr
                    return builtin_hook

                if (_walrus_wrapper_builtin_hook_4c94f98d1b644866ba3985a4cfa2a6d3(subm.get('loader', {}).get('built-in'))):
                    BuiltInLoaderHub.get(builtin_hook).validate(
                        **{k: v for k, v in subm['loader'].items() if k != 'built-in'}
                    )
            for svc in manif.manifest.get('services', []):
                if 'builtin_hook' not in dir():
                    builtin_hook = NotImplemented

                def _walrus_wrapper_builtin_hook_70917254a4e44962a858b34cc7752610(expr):
                    """Wrapper function for assignment expression."""
                    nonlocal builtin_hook
                    builtin_hook = expr
                    return builtin_hook

                if (_walrus_wrapper_builtin_hook_70917254a4e44962a858b34cc7752610(svc.get('predictor', {}).get('built-in'))):
                    BuiltInPredictorHub.get(builtin_hook).validate(
                        _submodels=submodels,
                        **{k: v for k, v in svc['predictor'].items() if k != 'built-in'}
                    )
        click.echo('[' + click.style('v', fg='green') + '] ', nl=False)
        click.echo(f'{manifest_file} passes validation')
    except Exception as err:  # pylint: disable=broad-exception-caught
        click.echo('[' + click.style('x', fg='red') + '] ', nl=False)
        click.echo(f'Validation for {manifest_file} fails')
        click.echo('\n' + str(err))
        sys.exit(1)


@dev.group(help='model versions under development')
def mv():
    pass


@mv.command(name='add-local', help='add a model version under development')
@click.option('--model-name', type=str, required=True, prompt=True, help='model name')
@click.option('--version-name', type=str, required=True, prompt=True, help='version name')
@click.option('--hooks-dir', type=click.UNPROCESSED, callback=_val_optional_dir,
              prompt=True, default='',
              help='hooks directory (a path relative to the current directory or an absolute path)')
@click.option('--src-dir', type=click.UNPROCESSED, callback=_val_optional_dir,
              prompt=True, default='',
              help='src directory (a path relative to the current directory or an absolute path)')
@click.option('--submodel', 'submodels', type=(str, str), multiple=True,
              help='submodel name & its source path (separated by a space), could be specified multiple times.' +
              ' Source path could be a file or a directory, relative to the current directory or an absolute path.')
@click.option('--manifest', 'manifest_file',
              type=click.Path(dir_okay=False, writable=True, resolve_path=True), prompt=True,
              help='path of manifest file to read or generate')
@click.option('--encrypted', is_flag=True, help='simulate an encrypted model version')
@click.option('--force-abs-paths', is_flag=True,
              help='force saving absolute paths in settings' +
              ' (By default, paths relative to SDK settings base directory are saved when applicable)')
@click.option('--preserve-model-files-in-src', is_flag=True,
              help='do not exclude submodel files from src' +
              ' (By default, submodel files are excluded from the src directory)')
@click.option('--preserve-hooks-dir-in-src', is_flag=True,
              help='do not exclude hooks directory from src' +
              ' (By default, hooks directory is excluded from the src directory)')
@click.option('--gen-manifest', 'gen_manifest_opt',
              type=click.Choice([c.value for c in ManifestGen], case_sensitive=False),
              default=ManifestGen.WHEN_NOT_EXISTS.value,
              help='when to generate manifest')
@click.option('--default-exclude-pattern', '-X', 'default_exclude_patterns',
              multiple=True, default=DEFAULT_EXCLUDE_PATTERNS,
              help=f'exclude any file matching the given pattern(s) (Default: {DEFAULT_EXCLUDE_PATTERNS})')
def add_local(model_name, version_name, hooks_dir, src_dir, submodels, manifest_file, encrypted,
              force_abs_paths, preserve_model_files_in_src, preserve_hooks_dir_in_src,
              gen_manifest_opt, default_exclude_patterns):
    def _reg_norm_path(resolved_path: Optional[str]) -> Optional[str]:
        if not resolved_path:
            return resolved_path
        if force_abs_paths:
            return str(resolved_path)
        try:
            return str(pathlib.Path(resolved_path).relative_to(reg_path))
        except ValueError:
            return resolved_path

    reg_path = get_config_path(check=True).parent
    reg = Registry(reg_path)
    if reg.get_model_version_info(model_name=model_name, version_name=version_name, suppress_warning=True):
        raise BadParameter(f'A model version with model_name={model_name} and version_name={version_name}' +
                           ' already exists')

    if 'curr_time' not in dir():
        curr_time = NotImplemented
    if 'gen_manifest_enum' not in dir():
        gen_manifest_enum = NotImplemented

    def _walrus_wrapper_curr_time_4baa4faa990a46fb875806e9042b58be(expr):
        """Wrapper function for assignment expression."""
        nonlocal curr_time
        curr_time = expr
        return curr_time

    def _walrus_wrapper_gen_manifest_enum_937baa173a1f4097b581f95e1b6bcc3a(expr):
        """Wrapper function for assignment expression."""
        nonlocal gen_manifest_enum
        gen_manifest_enum = expr
        return gen_manifest_enum
    if (_walrus_wrapper_gen_manifest_enum_937baa173a1f4097b581f95e1b6bcc3a(ManifestGen(gen_manifest_opt))) == ManifestGen.NEVER:
        if not pathlib.Path(manifest_file).exists():
            raise BadParameter(f'manifest file {manifest_file} does not exist')

    if not submodels:
        submodels = _get_submodels()
    submodels = _val_and_norm_submodels(submodels)

    hints = []

    # manifest
    if (gen_manifest_enum == ManifestGen.ALWAYS or
            gen_manifest_enum == ManifestGen.WHEN_NOT_EXISTS and not pathlib.Path(manifest_file).exists()):
        click.echo(f'Generating manifest at {manifest_file}...')
        with pathlib.Path(manifest_file).open('wt', encoding='utf8') as fp:
            manifest_dict, hints_ret = gen_manifest(
                schema=ManifestSchema.V2024_1, name=model_name, version=version_name,
                bare_models=[m for m, _ in submodels],
                hooks_dir=hooks_dir
            )
            json.dump(manifest_dict, fp, indent=2)
            hints.extend(hints_ret)

    # dev mv record
    dev_info = {
        'model_name': model_name,
        'version_name': version_name,
        'hooks_dir': _reg_norm_path(hooks_dir),
        'src_dir': _reg_norm_path(src_dir),
        'submodels': [(subm_name, _reg_norm_path(subm_path)) for subm_name, subm_path in submodels],
        'manifest_file': _reg_norm_path(manifest_file),
        'force_abs_paths': force_abs_paths,
        'preserve_model_files_in_src': preserve_model_files_in_src,
        'preserve_hooks_dir_in_src': preserve_hooks_dir_in_src,
        'gen_manifest': gen_manifest_enum.value,
        'default_exclude_patterns': default_exclude_patterns,
        'update_time': (_walrus_wrapper_curr_time_4baa4faa990a46fb875806e9042b58be(datetime.now())).isoformat()
    }
    vuuid = reg.get_new_local_vuuid(dev=True)
    click.echo(f'Generating dev mv record vuuid={vuuid}...')
    reg.set_model_version_info(
        puuid=reg.LOCAL_PUUID, muuid=reg.LOCAL_MUUID, model_name=model_name,
        vuuid=vuuid, version_name=version_name,
        packaged=True, encrypted=encrypted,
        download_time=curr_time, dev_info=dev_info
    )

    # gen archive
    _gen_archive(
        reg, vuuid, submodels=submodels, manifest_file=manifest_file,
        src_dir=src_dir, hooks_dir=hooks_dir, encrypted=encrypted,
        preserve_model_files_in_src=preserve_model_files_in_src,
        preserve_hooks_dir_in_src=preserve_hooks_dir_in_src,
        default_exclude_patterns=default_exclude_patterns
    )

    # hints
    click.echo('Done.')
    if hints:
        click.echo('\n' + click.style('Hints:', fg='green', bold=True))
        for num, msg in enumerate(hints, start=1):
            click.echo(f'{num}. {msg}')


@mv.command(name='update-local', help='update a model version under development')
@click.option('--model-name', type=str, required=True, help='model name')
@click.option('--version-name', type=str, required=True, help='version name')
@click.option('--new-model-name', type=str, help='update model name')
@click.option('--new-version-name', type=str, help='update version name')
@click.option('--hooks-dir', type=click.UNPROCESSED, callback=_val_optional_dir, default='',
              help='update hooks directory (a path relative to the current directory or an absolute path).' +
              ' To clear out hooks directory, use `--no-hooks-dir` instead.')
@click.option('--no-hooks-dir', is_flag=True, help='clear out hooks directory')
@click.option('--src-dir', type=click.UNPROCESSED, callback=_val_optional_dir, default='',
              help='update src directory (a path relative to the current directory or an absolute path).' +
              ' To clear out src directory, use `--no-src-dir` instead.')
@click.option('--no-src-dir', is_flag=True, help='clear out src directory')
@click.option('--add-submodel', 'add_submodels', type=(str, str), multiple=True,
              help='add a submodel by its name & its source path (separated by a space),' +
              ' could be specified multiple times.' +
              ' Source path could be a file or a directory, relative to the current directory or an absolute path.')
@click.option('--del-submodel', 'del_submodels', type=str, multiple=True,
              help='delete a previously defined submodel by its name, could be specified multiple times.')
@click.option('--manifest', 'manifest_file',
              type=click.Path(dir_okay=False, writable=True, resolve_path=True),
              help='update path of manifest file to read or generate')
@click.option('--encrypted/--no-encrypted', default=None, help='simulate an encrypted model version')
@click.option('--force-abs-paths/--no-force-abs-paths', default=None,
              help='force saving absolute paths in settings')
@click.option('--preserve-model-files-in-src/--no-preserve-model-files-in-src', default=None,
              help='do not exclude submodel files from src')
@click.option('--preserve-hooks-dir-in-src/--no-preserve-hooks-dir-in-src', default=None,
              help='do not exclude hooks directory from src')
@click.option('--gen-manifest', 'gen_manifest_opt',
              type=click.Choice([c.value for c in ManifestGen], case_sensitive=False), default=None,
              help='when to generate manifest')
@click.option('--add-default-exclude-pattern', 'add_default_exclude_patterns', type=str, multiple=True,
              help='add a file exclusion pattern')
@click.option('--del-default-exclude-pattern', 'del_default_exclude_patterns', type=str, multiple=True,
              help='delete a previously defined file exclusion pattern')
@click.option('--sync', is_flag=True,
              help='sync model version by re-building archive' +
              ' (and re-generating manifest if overwite-existing-manifest is enabled) based on changed settings.' +
              ' By default, sync is deferred until the `dev mv sync` command.')
def update_local(model_name, version_name, new_model_name, new_version_name,
                 hooks_dir, no_hooks_dir, src_dir, no_src_dir, add_submodels, del_submodels, manifest_file, encrypted,
                 force_abs_paths, preserve_model_files_in_src, preserve_hooks_dir_in_src, gen_manifest_opt,
                 add_default_exclude_patterns, del_default_exclude_patterns, sync):
    def _reg_norm_path(resolved_path: Optional[str]) -> Optional[str]:
        if not resolved_path or force_abs_paths:
            return resolved_path
        try:
            return str(pathlib.Path(resolved_path).relative_to(reg_path))
        except ValueError:
            return resolved_path

    def _reg_get_path(path_in_reg: Optional[str]) -> Optional[str]:
        if not path_in_reg:
            return path_in_reg
        return str(reg_path / path_in_reg)

    reg_path = get_config_path(check=True).parent
    reg = Registry(reg_path)

    if 'mv_info' not in dir():
        mv_info = NotImplemented

    def _walrus_wrapper_mv_info_35be0905ea3a4548af1eefa213e659a2(expr):
        """Wrapper function for assignment expression."""
        nonlocal mv_info
        mv_info = expr
        return mv_info

    if not (_walrus_wrapper_mv_info_35be0905ea3a4548af1eefa213e659a2(reg.get_model_version_info(
        model_name=model_name, version_name=version_name, suppress_warning=True))
    ):
        raise BadParameter(f'A model version with model_name={model_name} and version_name={version_name}' +
                           ' does not exist')
    if not mv_info.get('dev'):
        raise BadParameter('Not a dev model version')

    # === rename ===
    if new_model_name or new_version_name:
        new_model_name = new_model_name or model_name
        new_version_name = new_version_name or version_name

        try:
            reg.rename_model_version(model_name=model_name, version_name=version_name,
                                     new_model_name=new_model_name, new_version_name=new_version_name)
            model_name = new_model_name
            version_name = new_version_name
            mv_info = reg.get_model_version_info(
                model_name=model_name, version_name=version_name, suppress_warning=True
            )
        except (ModelVersionExistsException, MultipleModelVersionsException) as err:
            raise BadParameter(f'A model version with new_model_name={new_model_name} and' +
                               f' new_version_name={new_version_name} already exists') from err

    hints = []
    dev_info: dict = mv_info['dev_info']
    dev_info['update_time'] = datetime.now().isoformat()

    # === flags ===
    if encrypted is not None and encrypted != mv_info['encrypted']:
        mv_info['encrypted'] = encrypted
        if not sync:
            hints.append(f'encrypted is changed to {encrypted}.' +
                         ' You will need to sync model version later to make it work.')
    encrypted = mv_info['encrypted']

    if force_abs_paths is not None:
        dev_info['force_abs_paths'] = force_abs_paths
    force_abs_paths = dev_info.get('force_abs_paths', False)

    if preserve_model_files_in_src is not None:
        dev_info['preserve_model_files_in_src'] = preserve_model_files_in_src
    preserve_model_files_in_src = dev_info.get('preserve_model_files_in_src', False)

    if preserve_hooks_dir_in_src is not None:
        dev_info['preserve_hooks_dir_in_src '] = preserve_hooks_dir_in_src
    preserve_hooks_dir_in_src = dev_info.get('preserve_model_files_in_src', False)

    if gen_manifest_opt is not None:
        dev_info['gen_manifest'] = ManifestGen(gen_manifest_opt).value
    gen_manifest_enum = ManifestGen(dev_info.get('gen_manifest', ManifestGen.WHEN_NOT_EXISTS.value))

    # === exclusion patterns ===
    default_exclude_patterns = dev_info.get('default_exclude_patterns', [])
    if del_default_exclude_patterns:
        default_exclude_patterns = [p for p in default_exclude_patterns
                                    if p not in del_default_exclude_patterns]
    if add_default_exclude_patterns:
        default_exclude_patterns.extend(add_default_exclude_patterns)
    dev_info['default_exclude_patterns'] = default_exclude_patterns

    # === hooks dir ===
    if hooks_dir:
        if no_hooks_dir:
            raise BadParameter('`hooks-dir` and `no-hooks-dir` cannot be specified at the same time')
        dev_info['hooks_dir'] = _reg_norm_path(hooks_dir)
    elif no_hooks_dir:
        dev_info['hooks_dir'] = None
    hooks_dir = _reg_get_path(dev_info.get('hooks_dir'))

    # === src dir ===
    if src_dir:
        if no_src_dir:
            raise BadParameter('`src-dir` and `no-src-dir` cannot be specified at the same time')
        dev_info['src_dir'] = _reg_norm_path(src_dir)
    elif no_src_dir:
        dev_info['src_dir'] = None
    src_dir = _reg_get_path(dev_info.get('src_dir'))

    # === submodels ===
    if del_submodels:
        dev_info['submodels'] = [(subm_name, _reg_norm_path(_reg_get_path(subm_path)))
                                 for subm_name, subm_path in dev_info.get('submodels', [])
                                 if subm_name not in del_submodels]
    if add_submodels:
        submodels = _val_and_norm_submodels(add_submodels)
        dev_info['submodels'].extend(
            [(subm_name, _reg_norm_path(subm_path)) for subm_name, subm_path in submodels]
        )
    submodels = [(subm_name, _reg_get_path(subm_path)) for subm_name, subm_path in dev_info.get('submodels', [])]

    # === manifest ===
    if manifest_file:
        dev_info['manifest_file'] = _reg_norm_path(manifest_file)
    manifest_file = _reg_get_path(dev_info['manifest_file'])

    if gen_manifest_enum == ManifestGen.NEVER:
        if not pathlib.Path(manifest_file).exists():
            raise BadParameter(f'manifest file {manifest_file} does not exist')

    if (gen_manifest_enum == ManifestGen.ALWAYS or
            gen_manifest_enum == ManifestGen.WHEN_NOT_EXISTS and not pathlib.Path(manifest_file).exists()):
        click.echo(f'Generating manifest at {manifest_file}...')
        orig_manifest = None
        try:
            with pathlib.Path(manifest_file).open('rt', encoding='utf8') as fp:
                orig_manifest = json.load(fp)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            click.echo(f'The original manifest file {manifest_file} is not a valid JSON document.' +
                       ' Skip it and continue processing.', err=True)

        with pathlib.Path(manifest_file).open('wt', encoding='utf8') as fp:
            manifest_dict, hints_ret = gen_manifest(
                name=model_name, version=version_name,
                bare_models=[m for m, _ in submodels],
                orig_manifest=orig_manifest, hooks_dir=hooks_dir
            )
            json.dump(manifest_dict, fp, indent=2)
            hints.extend(hints_ret)

    # === registry ===
    vuuid = mv_info['vuuid']
    click.echo(f'Updating dev mv record vuud={vuuid}...')
    reg._update_model_version_dict(vuuid=vuuid, update_dict=mv_info)  # pylint: disable=protected-access

    # === sync ===
    if sync:
        _gen_archive(
            reg, vuuid, submodels=submodels, manifest_file=manifest_file,
            src_dir=src_dir, hooks_dir=hooks_dir, encrypted=encrypted,
            preserve_model_files_in_src=preserve_model_files_in_src,
            preserve_hooks_dir_in_src=preserve_hooks_dir_in_src,
            default_exclude_patterns=default_exclude_patterns
        )

    # === hint ===
    click.echo('Done.')
    if hints:
        click.echo('\n' + click.style('Hints:', fg='green', bold=True))
        for num, msg in enumerate(hints, start=1):
            click.echo(f'{num}. {msg}')


@mv.command(name='sync-local', help='sync a model version by re-building archive' +
            ' (and re-generating manifest if overwite-existing-manifest is enabled) based on changed settings.' +
            ' By default, sync is deferred until the `dev mv sync` command.')
@click.option('--model-name', type=str, required=True, help='model name')
@click.option('--version-name', type=str, required=True, help='version name')
def sync_local(model_name, version_name):
    def _reg_get_path(path_in_reg: Optional[str]) -> Optional[str]:
        if not path_in_reg:
            return path_in_reg
        return str(reg_path / path_in_reg)

    reg_path = get_config_path(check=True).parent
    reg = Registry(reg_path)

    if 'dev_info' not in dir():
        dev_info = NotImplemented
    if 'mv_info' not in dir():
        mv_info = NotImplemented

    def _walrus_wrapper_dev_info_cbf603b3e92443cb9e313c2c337e466c(expr):
        """Wrapper function for assignment expression."""
        nonlocal dev_info
        dev_info = expr
        return dev_info

    def _walrus_wrapper_mv_info_d4c01fbef7fd415b9ce12473ac7ef190(expr):
        """Wrapper function for assignment expression."""
        nonlocal mv_info
        mv_info = expr
        return mv_info

    if not (_walrus_wrapper_mv_info_d4c01fbef7fd415b9ce12473ac7ef190(reg.get_model_version_info(
        model_name=model_name, version_name=version_name, suppress_warning=True))
    ):
        raise BadParameter(f'A model version with model_name={model_name} and version_name={version_name}' +
                           ' does not exist')
    if not (_walrus_wrapper_dev_info_cbf603b3e92443cb9e313c2c337e466c(mv_info.get('dev_info'))):
        raise BadParameter('Not a dev model version')

    _gen_archive(
        reg, mv_info['vuuid'],
        submodels=[(subm_name, _reg_get_path(subm_path)) for subm_name, subm_path in dev_info['submodels']],
        manifest_file=_reg_get_path(dev_info['manifest_file']),
        src_dir=_reg_get_path(dev_info.get('src_dir')),
        hooks_dir=_reg_get_path(dev_info.get('hooks_dir')),
        encrypted=mv_info['encrypted'],
        preserve_model_files_in_src=dev_info.get('preserve_model_files_in_src', False),
        preserve_hooks_dir_in_src=dev_info.get('preserve_hooks_dir_in_src', False),
        default_exclude_patterns=dev_info.get('default_exclude_patterns')
    )
    click.echo('Done.')


@mv.command(name='list-local', help='list model version(s) under development')
@click.option('--model-name', type=str, help='filter by model name')
@click.option('--version-name', type=str, help='filter by version name (should be used with version-name)')
@click.option('--vuuid', type=str, help='filter by version uuid (will overwrite model-name and version-name)')
def list_local(model_name, version_name, vuuid):
    def _filter_by_model_name(mv_data: dict) -> bool:
        return mv_data['model_name'].lower() == model_name.lower()

    def _filter_by_version_name(mv_data: dict) -> bool:
        return mv_data['version_name'].lower() == version_name.lower()

    reg = Registry(get_config_path(check=True).parent)
    mvs = {_vuuid: _data for _vuuid, _data in reg.list_model_versions().items() if _data.get('dev')}
    results = {}

    if vuuid:
        if model_name or version_name:
            click.echo('model-name and version-name will be ignored when vuuid is specified', err=True)
        try:
            results[vuuid] = mvs[vuuid]
        except KeyError:
            pass
    else:
        filters = []
        if model_name:
            filters.append(_filter_by_model_name)
        if version_name:
            if not model_name:
                click.echo('version-name will be ignored when model-name is not specified', err=True)
            else:
                filters.append(_filter_by_version_name)
        if filters:
            results = {_vuuid: _data for _vuuid, _data in mvs.items() if all((f(_data) for f in filters))}
        else:
            results = mvs

    if not results:
        click.echo('No matching dev mvs are found.')
    else:
        click.echo(f'total: {len(results)}\n')
        click.echo(json.dumps(results, indent=2))
