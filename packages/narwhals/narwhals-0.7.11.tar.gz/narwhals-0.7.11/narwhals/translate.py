from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Any

from narwhals.dependencies import get_cudf
from narwhals.dependencies import get_modin
from narwhals.dependencies import get_pandas
from narwhals.dependencies import get_polars

if TYPE_CHECKING:
    from narwhals.dataframe import DataFrame
    from narwhals.dataframe import LazyFrame
    from narwhals.series import Series


def to_native(narwhals_object: LazyFrame | DataFrame | Series) -> Any:
    """
    Convert Narwhals object to native one.

    Arguments:
        narwhals_object: Narwhals object.

    Returns:
        Object of class that user started with.
    """
    from narwhals.dataframe import BaseFrame
    from narwhals.series import Series

    if isinstance(narwhals_object, BaseFrame):
        return (
            narwhals_object._dataframe
            if narwhals_object._is_polars
            else narwhals_object._dataframe._dataframe
        )
    if isinstance(narwhals_object, Series):
        return (
            narwhals_object._series
            if narwhals_object._is_polars
            else narwhals_object._series._series
        )

    msg = f"Expected Narwhals object, got {type(narwhals_object)}."  # pragma: no cover
    raise TypeError(msg)  # pragma: no cover


def from_native(
    native_dataframe: Any, *, strict: bool = False
) -> DataFrame | LazyFrame | Series:
    """
    Convert dataframe to Narwhals DataFrame or LazyFrame.

    Arguments:
        native_dataframe: Raw dataframe from user.
            Input object can be:

            - pandas.DataFrame
            - polars.DataFrame
            - polars.LazyFrame
            - modin.DataFrame
            - cudf.DataFrame
            - anything with a `__narwhals_dataframe__` or `__narwhals_lazyframe__` method
        strict: Whether to raise if object can't be converted (default) or
            to just leave it as-is.

    Returns:
        narwhals.DataFrame or narwhals.LazyFrame
    """
    from narwhals.dataframe import DataFrame
    from narwhals.dataframe import LazyFrame
    from narwhals.series import Series

    if (pl := get_polars()) is not None and isinstance(native_dataframe, pl.DataFrame):
        return DataFrame(native_dataframe)
    elif (pl := get_polars()) is not None and isinstance(native_dataframe, pl.LazyFrame):
        return LazyFrame(native_dataframe)  # pragma: no cover (todo)
    elif (
        (pd := get_pandas()) is not None
        and isinstance(native_dataframe, pd.DataFrame)
        or (mpd := get_modin()) is not None
        and isinstance(native_dataframe, mpd.DataFrame)
        or (cudf := get_cudf()) is not None
        and isinstance(native_dataframe, cudf.DataFrame)
    ):
        return DataFrame(native_dataframe)
    elif hasattr(native_dataframe, "__narwhals_dataframe__"):  # pragma: no cover
        return DataFrame(native_dataframe.__narwhals_dataframe__())
    elif hasattr(native_dataframe, "__narwhals_lazyframe__"):  # pragma: no cover
        return LazyFrame(native_dataframe.__narwhals_lazyframe__())
    elif (
        (pl := get_polars()) is not None
        and isinstance(native_dataframe, pl.Series)
        or (pl := get_polars()) is not None
        and isinstance(native_dataframe, pl.Series)
        or (
            (pd := get_pandas()) is not None
            and isinstance(native_dataframe, pd.Series)
            or (mpd := get_modin()) is not None
            and isinstance(native_dataframe, mpd.Series)
            or (cudf := get_cudf()) is not None
            and isinstance(native_dataframe, cudf.Series)
        )
    ):
        return Series(native_dataframe)
    elif hasattr(native_dataframe, "__narwhals_series__"):  # pragma: no cover
        return Series(native_dataframe.__narwhals_series__())
    elif strict:  # pragma: no cover
        msg = f"Expected pandas-like dataframe, Polars dataframe, or Polars lazyframe, got: {type(native_dataframe)}"
        raise TypeError(msg)
    return native_dataframe  # type: ignore[no-any-return]  # pragma: no cover (todo)


def from_native_series(native_series: Any, *, strict: bool = False) -> Series:
    """
    Convert dataframe to Narwhals DataFrame or LazyFrame.

    Arguments:
        native_dataframe: Raw dataframe from user.
            Input object can be:

            - pandas.DataFrame
            - polars.DataFrame
            - polars.LazyFrame
            - modin.DataFrame
            - cudf.DataFrame
            - anything with a `__narwhals_dataframe__` or `__narwhals_lazyframe__` method
        strict: Whether to raise if object can't be converted (default) or
            to just leave it as-is.

    Returns:
        narwhals.DataFrame or narwhals.LazyFrame
    """
    from narwhals.series import Series

    if (
        (pl := get_polars()) is not None
        and isinstance(native_series, pl.Series)
        or (pl := get_polars()) is not None
        and isinstance(native_series, pl.Series)
        or (
            (pd := get_pandas()) is not None
            and isinstance(native_series, pd.Series)
            or (mpd := get_modin()) is not None
            and isinstance(native_series, mpd.Series)
            or (cudf := get_cudf()) is not None
            and isinstance(native_series, cudf.Series)
        )
    ):
        return Series(native_series)
    elif hasattr(native_series, "__narwhals_series__"):  # pragma: no cover
        return Series(native_series.__narwhals_series__())
    elif strict:  # pragma: no cover
        msg = f"Expected pandas-like series or Polars series, got: {type(native_series)}"
        raise TypeError(msg)
    return native_series  # type: ignore[no-any-return]  # pragma: no cover (todo)


def from_native_dataframe(
    native_dataframe: Any, *, strict: bool = False
) -> DataFrame | LazyFrame:
    """
    Convert dataframe to Narwhals DataFrame or LazyFrame.

    Arguments:
        native_dataframe: Raw dataframe from user.
            Input object can be:

            - pandas.DataFrame
            - polars.DataFrame
            - polars.LazyFrame
            - modin.DataFrame
            - cudf.DataFrame
            - anything with a `__narwhals_dataframe__` or `__narwhals_lazyframe__` method
        strict: Whether to raise if object can't be converted (default) or
            to just leave it as-is.

    Returns:
        narwhals.DataFrame or narwhals.LazyFrame
    """
    from narwhals.dataframe import DataFrame
    from narwhals.dataframe import LazyFrame

    if (pl := get_polars()) is not None and isinstance(native_dataframe, pl.DataFrame):
        return DataFrame(native_dataframe)
    elif (pl := get_polars()) is not None and isinstance(native_dataframe, pl.LazyFrame):
        return LazyFrame(native_dataframe)
    elif (
        (pd := get_pandas()) is not None
        and isinstance(native_dataframe, pd.DataFrame)
        or (mpd := get_modin()) is not None
        and isinstance(native_dataframe, mpd.DataFrame)
        or (cudf := get_cudf()) is not None
        and isinstance(native_dataframe, cudf.DataFrame)
    ):
        return DataFrame(native_dataframe)
    elif hasattr(native_dataframe, "__narwhals_dataframe__"):  # pragma: no cover
        return DataFrame(native_dataframe.__narwhals_dataframe__())
    elif hasattr(native_dataframe, "__narwhals_lazyframe__"):  # pragma: no cover
        return LazyFrame(native_dataframe.__narwhals_lazyframe__())
    elif strict:  # pragma: no cover
        msg = f"Expected pandas-like dataframe, Polars dataframe, or Polars lazyframe, got: {type(native_dataframe)}"
        raise TypeError(msg)
    return native_dataframe  # type: ignore[no-any-return]  # pragma: no cover


__all__ = [
    "get_pandas",
    "get_polars",
    "get_modin",
    "get_cudf",
    "to_native",
]
