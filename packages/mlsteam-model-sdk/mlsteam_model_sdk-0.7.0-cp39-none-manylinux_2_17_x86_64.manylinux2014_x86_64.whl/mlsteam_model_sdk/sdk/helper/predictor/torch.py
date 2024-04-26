"""High-level predictor interface for PyTorch"""
from typing import Any, Optional

import jsonschema
import jsonschema.exceptions
import torch

from . import BuiltInPredictorBase


class TorchBuiltInClassifier(BuiltInPredictorBase):
    """PyTorch built-in multi-class classifier

    It supports making (batched) prediction from a Tortch tensor by a single model.
    """

    def __init__(self, _submodels: list, submodel: str, classes: Optional[list] = None,
                 batch=True, output_class_dim: Optional[int] = None, **_):
        """Constructor

        Args:
          _submodels: names of all submodels
          submodel: name of submodel to use
          classes: a list of class names.
            The predictor will return class names when `classes` is provided.
          batch: enable batch prediction
          output_class_dim: class probability dimension in the output tensor.
            It defaults to `0` when batch is disabled and `1` otherwise.
        """
        self.validate(_submodels, submodel=submodel, classes=classes, output_class_dim=output_class_dim)
        self.submodel = submodel
        self.classes = classes
        self.batch = batch
        self.output_class_dim = output_class_dim if output_class_dim is not None else (1 if batch else 0)

    @classmethod
    def validate(cls, _submodels: list, **kwargs):
        err_prefix = f'{cls.__name__} validation error:'

        if 'classes' not in dir():
            classes = NotImplemented
        if 'output_class_dim' not in dir():
            output_class_dim = NotImplemented
        if 'submodel' not in dir():
            submodel = NotImplemented

        def _walrus_wrapper_classes_2d9d474af9e84247874a44111c939f0e(expr):
            """Wrapper function for assignment expression."""
            nonlocal classes
            classes = expr
            return classes

        def _walrus_wrapper_output_class_dim_dbce2adfd8a842e0a9c2f746d3e59b57(expr):
            """Wrapper function for assignment expression."""
            nonlocal output_class_dim
            output_class_dim = expr
            return output_class_dim

        def _walrus_wrapper_submodel_fac838a363ec4f00b3abf95e2cadcc51(expr):
            """Wrapper function for assignment expression."""
            nonlocal submodel
            submodel = expr
            return submodel
        if not (_walrus_wrapper_submodel_fac838a363ec4f00b3abf95e2cadcc51(kwargs.get('submodel'))):
            raise ValueError(f'{err_prefix} Missing submodel')
        if submodel not in _submodels:
            raise ValueError(f'{err_prefix} Unrecognized submodel: {submodel}')

        if (_walrus_wrapper_classes_2d9d474af9e84247874a44111c939f0e(kwargs.get('classes'))):
            try:
                jsonschema.validate(classes, {'type': 'array', 'items': {'type': 'string'}})
            except jsonschema.exceptions.ValidationError as err:
                raise ValueError(f'{err_prefix} Invalid classes: {classes}') from err

        if (_walrus_wrapper_output_class_dim_dbce2adfd8a842e0a9c2f746d3e59b57(kwargs.get('output_class_dim'))) is not None:
            if not isinstance(output_class_dim, int) or output_class_dim < 0:
                raise ValueError(f'{err_prefix} Invalid output_class_dim: {output_class_dim}; should be 0 or a number')

    def __call__(self, env, model, inputs, service_name: str, **kwargs: Any) -> dict:
        """Makes (batched) classification

        Returns:
          The classification results as a dict with the following fields:
          - class_ids: classification class ids
          - class_names: classification class names (exists when `classes` was provided)
          - probs: classification probabilities

          The field values are lists when batch is enabled.
        """
        outputs = model[self.submodel](inputs)
        probs, class_ids = torch.max(outputs, self.output_class_dim)
        results = {
            'class_ids': class_ids,
            'probs': probs
        }
        if self.classes:
            results['class_names'] = [self.classes[_id] for _id in class_ids] \
                if self.batch else self.classes[class_ids]

        return results
