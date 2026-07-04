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
