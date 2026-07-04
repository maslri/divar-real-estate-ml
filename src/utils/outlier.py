import pandas as pd


def iqr_bounds(series: pd.Series, k: float = 1.5) -> tuple[float, float]:
    """
    Calculate lower and upper bounds using the IQR method.

    Parameters
    ----------
    series : pd.Series
        Numeric pandas Series.
    k : float, default=1.5
        IQR multiplier.

    Returns
    -------
    (lower_bound, upper_bound)
    """
    s = series.dropna()

    q1 = s.quantile(0.25)
    q3 = s.quantile(0.75)

    iqr = q3 - q1

    lower = q1 - k * iqr
    upper = q3 + k * iqr

    return lower, upper


def detect_outliers_iqr(series: pd.Series, k: float = 1.5) -> pd.Series:
    """
    Return a boolean mask of outliers using the IQR rule.
    """
    lower, upper = iqr_bounds(series, k)

    return (series < lower) | (series > upper)


def remove_outliers_iqr(series: pd.Series, k: float = 1.5) -> pd.Series:
    """
    Replace outliers with NA.
    """
    mask = detect_outliers_iqr(series, k)

    return series.mask(mask)


def outlier_report(series: pd.Series, k: float = 1.5) -> dict:
    """
    Return a simple summary of detected outliers.
    """
    mask = detect_outliers_iqr(series, k)

    return {
        "feature": series.name,
        "count": int(mask.sum()),
        "percent": round(mask.mean() * 100, 2),
        "lower_bound": iqr_bounds(series, k)[0],
        "upper_bound": iqr_bounds(series, k)[1],
    }
