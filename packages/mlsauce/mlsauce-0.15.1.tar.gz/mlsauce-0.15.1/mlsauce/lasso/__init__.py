try:
    from ._lasso import LassoRegressor
except ModuleNotFoundError:
    pass

__all__ = ["LassoRegressor"]
