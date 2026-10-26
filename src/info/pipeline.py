from info.dimension import dimension
from info.duplicates import duplicate_group_rows, duplicate_rows, duplicates
from info.null import missing_rows
from info.prices import invalid_prices, ohlc_violations


def info(df):
    print(f"Missing rows: {missing_rows(df)}")
    print(f"Exact duplicate rows: {duplicates(df)}")
    print(f"Duplicate group rows: {duplicate_group_rows(df)}")
    print(f"Duplicate rows to drop: {duplicate_rows(df)}")
    print(f"Non-positive price rows: {invalid_prices(df)}")
    print(f"OHLC issue rows: {ohlc_violations(df)}")

    rows, columns = dimension(df)
    print(f"Rows: {rows}, Columns: {columns}")
