# ruff: noqa: F401
"""Python module to interface with Weather Data in a MySQL database."""

from __future__ import annotations

from .api import MeteobridgeSQL, MeteobridgeSQLDatabaseConnectionError, MeteobridgeSQLDataError
from .data import ForecastDaily, ForecastHourly, RealtimeData, StationData

__title__ = "pymeteobridgesql"
__version__ = "1.1.6"
__author__ = "briis"
__license__ = "MIT"
