import pandas as pd
from datetime import datetime
import pickle
import numpy as np
from volstreet.config import logger
from volstreet.historical_info import historical_expiry_dates
from volstreet.backtests.database import DataBaseConnection


class UnderlyingInfo:
    def __init__(self, name):
        self.name = name.upper()
        self.base = self._get_base()
        self.expiry_dates = filter_expiry_dates_for_index(self.name)

    def _get_base(self):
        if self.name in ["NIFTY", "FINNIFTY"]:
            return 50
        elif self.name == "BANKNIFTY":
            return 100
        elif self.name == "MIDCPNIFTY":
            return 25
        else:
            raise ValueError("Invalid index name")


def filter_expiry_dates_for_index(underlying: str) -> pd.DatetimeIndex:
    index_expiry_dates = historical_expiry_dates[underlying.upper()]
    return pd.DatetimeIndex(sorted(index_expiry_dates))


def fetch_historical_expiry(
    underlying: str,
    date_time: str | datetime,
    threshold_days: int = 0,
    n_exp: int = 1,
) -> pd.DatetimeIndex | pd.Timestamp | None:
    if isinstance(date_time, str):
        date_time = pd.to_datetime(date_time)

    filtered_dates = filter_expiry_dates_for_index(underlying)
    delta_days = (filtered_dates - date_time.replace(hour=00, minute=00)).days
    valid_indices = np.where(delta_days < threshold_days, np.inf, delta_days).argsort()[
        :n_exp
    ]

    nearest_exp_dates = filtered_dates[valid_indices].sort_values()

    if n_exp == 1:
        return nearest_exp_dates[0] if len(nearest_exp_dates) != 0 else None
    else:
        return nearest_exp_dates
