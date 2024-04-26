"""Model archive operations"""
import zipfile
from pathlib import Path
from typing import Iterator, Optional, Sequence, Tuple


ENC_PKG_FILE = 'model-enc.mlarchive'

SubmodelInfo = Tuple[str, str]


def build_archive(archive_file: str, submodels: Sequence[SubmodelInfo], manifest_file: str,
                  src_dir: Optional[str], hooks_dir: Optional[str],
                  preserve_model_files_in_src: bool, preserve_hooks_dir_in_src: bool,
                  default_exclude_patterns: Optional[Sequence[str]]):
    """Creates a model archive"""
    submodels_paths = [(subm[0], Path(subm[1])) for subm in submodels]
    hooks_dir_path = Path(hooks_dir) if hooks_dir else None
    src_dir_path = Path(src_dir) if src_dir else None
    default_exclude_patterns = default_exclude_patterns or []

    with zipfile.ZipFile(archive_file, mode='w', compression=zipfile.ZIP_DEFLATED) as archive:
        # manifest
        archive.write(manifest_file, 'manifest.json')

        # models/
        for subm_name, subm_path in submodels_paths:
            arc_base_path = Path('models') / subm_name
            if subm_path.is_file():
                archive.write(subm_path, arcname=arc_base_path / subm_path.name)
            else:
                for _path in _iter_dir(subm_path, default_exclude_patterns, []):
                    archive.write(_path, arcname=arc_base_path / _path.relative_to(subm_path))

        # hooks/
        if hooks_dir_path:
            arc_base_path = Path('hooks')
            for _path in _iter_dir(hooks_dir_path, default_exclude_patterns, []):
                archive.write(_path, arcname=arc_base_path / _path.relative_to(hooks_dir_path))

        # src/
        if src_dir_path:
            src_exclude_paths = []
            if not preserve_hooks_dir_in_src and hooks_dir_path:
                if _is_same_or_parent(src_dir_path, hooks_dir_path):
                    src_exclude_paths.append(hooks_dir_path)
            if not preserve_model_files_in_src:
                for _, subm_path in submodels_paths:
                    if _is_same_or_parent(src_dir_path, subm_path):
                        src_exclude_paths.append(subm_path)

            if not _contains_path(src_exclude_paths, src_dir_path):
                arc_base_path = Path('src')
                for _path in _iter_dir(src_dir_path, default_exclude_patterns, src_exclude_paths):
                    archive.write(_path, arcname=arc_base_path / _path.relative_to(src_dir_path))


def extract_archive(archive_file, extract_dir):
    """Extracts a model archive to a directory"""
    with zipfile.ZipFile(archive_file, mode='r') as package_zip:
        package_zip.extractall(path=extract_dir)


def _iter_dir(base_dir: Path, exclude_patterns: Sequence[str], exclude_paths: Sequence[Path]) -> Iterator[Path]:
    for ite in base_dir.iterdir():
        if any((ite.match(_pattern) for _pattern in exclude_patterns)):
            continue
        if any((ite.samefile(_path) for _path in exclude_paths)):
            continue
        if ite.is_dir():
            yield from _iter_dir(ite, exclude_patterns, exclude_paths)
        yield ite


def _is_same_or_parent(path_dir: Path, path_x: Path):
    return path_x.samefile(path_dir) or _contains_path(path_x.parents, path_dir)


def _contains_path(path_collection: Sequence[Path], path_x: Path):
    for _path in path_collection:
        if _path.samefile(path_x):
            return True
    return False
