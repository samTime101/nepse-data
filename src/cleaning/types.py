import pandas as pd
from definitions import NUMERIC_COLUMNS

def convert_types(df):
    df = df.copy()
    df["published_date"] = pd.to_datetime(df["published_date"], errors="coerce") # coerce invalid dates to NaT

    for column in NUMERIC_COLUMNS:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce") # coerce invalid numbers to NaN
    return df
