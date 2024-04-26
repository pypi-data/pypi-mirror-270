"""Model archive predictor interface"""
import importlib
from typing import Any


class BuiltInPredictorHub:
    """Built-in predictor access hub

    It loads a predictor until requested to avoid undesired runtime dependency (E.g., torch, tenserflow).
    """

    __reg = {
        'PyTorchClassifier': ('.torch', 'TorchBuiltInClassifier')
    }

    @classmethod
    def __get_predictor(cls, mod_path: str, callable_path: str) -> 'BuiltInPredictorBase':
        predictor = importlib.import_module(mod_path, package='mlsteam_model_sdk.sdk.helper.predictor')
        for callable_part in callable_path.split('.'):
            predictor = getattr(predictor, callable_part)
        return predictor

    @classmethod
    def get(cls, predictor_name: str) -> 'BuiltInPredictorBase':
        """Gets a built-in predictor by name"""
        try:
            predictor_meta = cls.__reg[predictor_name]
        except KeyError:
            raise ValueError(f'Invalid predictor name: {predictor_name}') from None

        return cls.__get_predictor(predictor_meta[0], predictor_meta[1])


class BuiltInPredictorBase:
    """Built-in predictor base class"""

    @classmethod
    def validate(cls, _submodels: list, **kwargs):
        pass

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass
