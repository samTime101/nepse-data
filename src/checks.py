from definitions import DAILY_ROW_COLUMNS, KEY_COLUMNS, PRICE_COLUMNS

def missing_row_mask(df):
    # if any of the daily row columns is NaN, return True for that row
    return df[DAILY_ROW_COLUMNS].isna().any(axis=1)

def duplicate_row_mask(df, keep="last"):
    # returns a boolean mask indicating which rows are duplicates based on KEY_COLUMNS
    return df.duplicated(subset=KEY_COLUMNS, keep=keep)

def duplicate_group_mask(df):
    # returns a boolean mask indicating which rows are part of a duplicate group based on KEY_COLUMNS
    return df.duplicated(subset=KEY_COLUMNS, keep=False)

# axis 1 -> columns for each row
def invalid_price_mask(df):
    # if any of the price columns is less than or equal to 0, return True for that row
    # returns a boolean mask indicating which rows have invalid prices based on PRICE_COLUMNS
    return (df[PRICE_COLUMNS] <= 0).any(axis=1)


def ohlc_violation_mask(df):
    # if high < low or high < max(open, close) or low > min(open, close), return True for that row
    # returns a boolean mask indicating which rows have OHLC violations
    open_close = df[["open", "close"]]
    return ((df["high"] < df["low"])| (df["high"] < open_close.max(axis=1))| (df["low"] > open_close.min(axis=1)))
