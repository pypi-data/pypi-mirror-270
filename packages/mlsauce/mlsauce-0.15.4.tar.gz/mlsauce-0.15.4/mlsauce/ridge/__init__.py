try:
    from ._ridge import RidgeRegressor
except ModuleNotFoundError:
    pass

__all__ = ["RidgeRegressor"]
