try:
    from ._stump_classifier import StumpClassifier
except ModuleNotFoundError:
    pass

__all__ = ["StumpClassifier"]
