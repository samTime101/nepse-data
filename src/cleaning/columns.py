def standardize_columns(df):
    df = df.copy()
    df.columns = [str(column).strip().lower() for column in df.columns]
    return df


def standardize_symbols(df):
    df = df.copy()
    df["symbol"] = df["symbol"].astype(str).str.strip().str.upper()
    return df