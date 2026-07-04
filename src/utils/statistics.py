import re
import pandas as pd


def interpret_cohens_d(d):
    d = abs(d)

    if d < 0.2:
        return "Negligible"

    elif d < 0.5:
        return "Small"

    elif d < 0.8:
        return "Medium"

    return "Large"


def normalize_year(value):
    """
    Normalize Persian construction year values.

    Examples
    --------
    '۱۴۰۲' -> 1402
    'قبل از ۱۳۷۰' -> 1370
    NaN -> None
    """

    if pd.isna(value):
        return None

    value = str(value)

    # Convert Persian digits to English digits
    value = value.translate(str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789"))

    match = re.search(r"\d{4}", value)

    if match:
        return int(match.group())

    return None


def normalize_integer(value, replacements=None):
    if pd.isna(value):
        return pd.NA

    value = str(value).strip()

    if replacements and value in replacements:
        return replacements[value]

    try:
        return int(float(value))
    except (ValueError, TypeError):
        return pd.NA


def missing_by_group(df, feature, group_by):
    return (
        df.groupby(group_by, observed=True)[feature]
        .apply(lambda s: round(s.isna().mean() * 100, 2))
        .sort_values()
        .rename("missing_pct")
        .to_frame()
    )


import pandas as pd


def hierarchical_impute(
    df: pd.DataFrame,
    column: str,
    groups: list[str],
    strategy: str = "median",
    verbose: bool = True,
) -> pd.Series:
    """
    Hierarchical missing value imputation.

    Parameters
    ----------
    df : pd.DataFrame
    column : str
        Target column.
    groups : list[str]
        Ordered grouping columns.
    strategy : {"median", "mean", "mode"}
    verbose : bool
    """

    before = df[column].isna().sum()

    s = df[column].copy()

    for group in groups:

        if strategy == "median":
            fill_values = df.groupby(group)[column].transform("median")

        elif strategy == "mean":
            fill_values = df.groupby(group)[column].transform("mean")

        elif strategy == "mode":

            fill_values = df.groupby(group)[column].transform(
                lambda x: x.mode().iloc[0] if not x.mode().empty else pd.NA
            )

        else:
            raise ValueError("strategy must be 'median', 'mean', or 'mode'")

        s = s.fillna(fill_values)

    # Final fallback
    if strategy == "median":
        s = s.fillna(s.median())

    elif strategy == "mean":
        s = s.fillna(s.mean())

    else:
        mode = s.mode()
        if not mode.empty:
            s = s.fillna(mode.iloc[0])

    after = s.isna().sum()

    if verbose:
        print(
            f"{column}: {before:,} -> {after:,} missing " f"({before-after:,} filled)"
        )

    return s
