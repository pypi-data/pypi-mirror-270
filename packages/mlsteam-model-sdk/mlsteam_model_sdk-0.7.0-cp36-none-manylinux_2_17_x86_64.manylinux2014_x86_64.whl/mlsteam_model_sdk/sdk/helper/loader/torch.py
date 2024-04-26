"""High-level loader interface for PyTorch"""
import contextlib
import io
import pathlib
import re
from collections.abc import Iterable, Sequence
from typing import Optional

import torch
from torch.nn import Module

from . import BuiltInLoaderBase, ModelFileLoaderBase, PathTypes


class Loader:
    """PyTorch loader"""

    @classmethod
    def from_state_dicts(cls, model_obj: Module, state_dict_paths: Sequence, device: Optional[str] = None) -> Module:
        """Loads a PyTorch model from state-dict files.

        Args:
          model_obj: a PyTorch model object to load model weights
          state_dict_paths: a list of PyTorch state-dict files with the model weights
          device: destination device of loaded state tensor and model (E.g., 'cpu', 'cuda', 'cuda:0')

        Returns:
          the PyTorch model object with loaded model weights
        """

        if 'n_dicts' not in dir():
            n_dicts = NotImplemented

        def _walrus_wrapper_n_dicts_ef36bd638cc243a589aa7d617882ec7b(expr):
            """Wrapper function for assignment expression."""
            nonlocal n_dicts
            n_dicts = expr
            return n_dicts

        if (_walrus_wrapper_n_dicts_ef36bd638cc243a589aa7d617882ec7b(len(state_dict_paths))) == 0:
            raise ValueError('No state dicts specified')
        load_strict = n_dicts == 1
        for _path in state_dict_paths:
            try:
                with _path.open('rb') as fp:
                    model_obj.load_state_dict(torch.load(fp, map_location=device), strict=load_strict)
            except ValueError:
                with contextlib.ExitStack() as stack:
                    if 'fp' not in dir():
                        fp = NotImplemented

                    def _walrus_wrapper_fp_8bf38cf33b434dbb88f88bbe3d9d925b(expr):
                        """Wrapper function for assignment expression."""
                        nonlocal fp
                        fp = expr
                        return fp

                    stack.enter_context(_walrus_wrapper_fp_8bf38cf33b434dbb88f88bbe3d9d925b(_path.open('r')))  # zipfile.Path does not support 'b' before Python 3.9
                    if not fp.seekable():
                        # ZipExtFile is not seekable before Python 3.7

                        if '_data' not in dir():
                            _data = NotImplemented
                        if 'buf' not in dir():
                            buf = NotImplemented

                        def _walrus_wrapper__data_20ceec2436e4441fb12207041024ac66(expr):
                            """Wrapper function for assignment expression."""
                            nonlocal _data
                            _data = expr
                            return _data

                        def _walrus_wrapper_buf_29a55a46db074095aa962413ba84e731(expr):
                            """Wrapper function for assignment expression."""
                            nonlocal buf
                            buf = expr
                            return buf

                        stack.enter_context(_walrus_wrapper_buf_29a55a46db074095aa962413ba84e731(io.BytesIO()))
                        while (_walrus_wrapper__data_20ceec2436e4441fb12207041024ac66(fp.read(1_048_576))):  # read 1 MB at a time
                            buf.write(_data)
                        buf.seek(0)
                        fp = buf
                    model_obj.load_state_dict(torch.load(fp, map_location=device), strict=load_strict)
        return model_obj.to(device=device) if device else model_obj

    @classmethod
    def from_submodel(cls, model_obj: Module, model_file_loader: ModelFileLoaderBase, subm_name: str,
                      device: Optional[str] = None) -> Module:
        """A convenient function for loading a PyTorch model under a submodel directory.

        Args:
          model_obj: a PyTorch model object to load model weights
          model_file_loader: the file loader passed by SDK in loader hooks
          subm_name: submodel name
          device: destination device of loaded model (E.g., 'cpu', 'cuda', 'cuda:0')

        Returns:
          the PyTorch model object with loaded model weights
        """
        return cls.from_submodel_state_dicts(model_obj, model_file_loader, subm_name, device=device)

    @classmethod
    def from_submodel_state_dicts(cls, model_obj: Module,
                                  model_file_loader: ModelFileLoaderBase, subm_name: str,
                                  file_iter: Optional[Iterable] = None,
                                  device: Optional[str] = None) -> Module:
        """Loads a PyTorch model from state-dict files under a submodel directory.

        Args:
          model_obj: a PyTorch model object to load model weights
          model_file_loader: the file loader passed by SDK in loader hooks
          subm_name: submodel name
          file_iter: an iterator for the state-dict files. By default, it calls `iter_state_dicts_simple()`
            to iterate all files with the `.pt` or `.pth` extension names.
          device: destination device of loaded state tensor and model (E.g., 'cpu', 'cuda', 'cuda:0')

        Returns:
          the PyTorch model object with loaded model weights
        """
        if file_iter:
            sdict_paths = list(file_iter)
        else:
            sdict_paths = list(iter_state_dicts_simple(model_file_loader.get_submodel_dir(subm_name)))
        return cls.from_state_dicts(model_obj, sdict_paths, device=device)


def iter_state_dicts_simple(base_dir_path: PathTypes,
                            file_extensions: Sequence = ('.pt', '.pth')) -> Iterable:
    """Iterates the state-dict files under the current directory.

    Args:
      base_dir_path: the directory to scan state-dict files
      file_extensions: file extensions for matching state-dict files.
        If a file extension does not start with a dot, a dot will be added.
        By default, it matches only ('.pt', '.pth') files.

    Returns:
      an iterator for the matched files
    """
    file_extensions = [fext if fext.startswith('.') else f'.{fext}'
                       for fext in file_extensions]

    try:
        base_dir_path.suffix  # test .suffix support; pylint: disable=pointless-statement
        state_dict_paths = (_path for _path in base_dir_path.iterdir()
                            if _path.is_file() and _path.suffix in file_extensions)
    except AttributeError:
        # zipfile.Path does not have .suffix until Python 3.11
        def _suffix(pth: PathTypes):
            if 'pos' not in dir():
                pos = NotImplemented

            def _walrus_wrapper_pos_0b18ce55075c44529e06b829748ecbda(expr):
                """Wrapper function for assignment expression."""
                nonlocal pos
                pos = expr
                return pos

            if (_walrus_wrapper_pos_0b18ce55075c44529e06b829748ecbda(pth.name.rfind('.'))) >= 0:
                return pth.name[pos:]
            return ''
        state_dict_paths = (_path for _path in base_dir_path.iterdir()
                            if _path.is_file() and _suffix(_path) in file_extensions)
    return state_dict_paths


class TorchBuiltInLoader(BuiltInLoaderBase):
    """PyTorch built-in loader"""

    @classmethod
    def validate(cls, **kwargs):
        err_prefix = f'{cls.__name__} validation error:'

        if 'device' not in dir():
            device = NotImplemented
        if 'model_cls_file' not in dir():
            model_cls_file = NotImplemented
        if 'model_cls_name' not in dir():
            model_cls_name = NotImplemented

        def _walrus_wrapper_device_1d147c1387a847ef9690233c30307a47(expr):
            """Wrapper function for assignment expression."""
            nonlocal device
            device = expr
            return device

        def _walrus_wrapper_model_cls_file_e6789f08c84a48ae875eafd94df63ac4(expr):
            """Wrapper function for assignment expression."""
            nonlocal model_cls_file
            model_cls_file = expr
            return model_cls_file

        def _walrus_wrapper_model_cls_name_88943c934dd449a48bd73dd53a40a849(expr):
            """Wrapper function for assignment expression."""
            nonlocal model_cls_name
            model_cls_name = expr
            return model_cls_name
        if not (_walrus_wrapper_model_cls_file_e6789f08c84a48ae875eafd94df63ac4(kwargs.get('model_cls_file'))):
            raise ValueError(f'{err_prefix} Missing model_cls_file')
        try:
            cls.validate_src_module_args(pathlib.PurePath(model_cls_file))
        except ValueError as err:
            raise ValueError(f'{err_prefix} Invalid model_cls_file: {model_cls_file}') from err

        if not (_walrus_wrapper_model_cls_name_88943c934dd449a48bd73dd53a40a849(kwargs.get('model_cls_name'))):
            raise ValueError(f'{err_prefix} Missing model_cls_name')
        if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', model_cls_name) is None:
            raise ValueError(f'{err_prefix} Invalid model_cls_name: {model_cls_name}')

        if (_walrus_wrapper_device_1d147c1387a847ef9690233c30307a47(kwargs.get('device'))):
            try:
                torch.device(device)
            except RuntimeError as err:
                raise ValueError(f'{err_prefix} Invalid device: {device}') from err

    def __call__(self, submodels: list, model_file_loader: ModelFileLoaderBase,
                 model_cls_file: str, model_cls_name: str, device: Optional[str] = None, **kwargs) -> Module:
        self.validate(model_cls_file=model_cls_file, model_cls_name=model_cls_name)
        model_cls_mod = self._load_src_module(pathlib.PurePath(model_cls_file))
        model_cls = getattr(model_cls_mod, model_cls_name)
        return Loader.from_submodel(
            model_obj=model_cls(),
            model_file_loader=model_file_loader,
            subm_name=submodels[0],
            device=device
        )
