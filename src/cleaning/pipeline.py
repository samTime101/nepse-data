from checks import duplicate_group_mask,invalid_price_mask,missing_row_mask,ohlc_violation_mask
from cleaning.columns import standardize_columns, standardize_symbols
from cleaning.duplicates import drop_duplicate_rows
from cleaning.export import export_rejected_data
from cleaning.missing import drop_missing_rows
from cleaning.prices import drop_invalid_prices
from cleaning.schema import validate_schema
from cleaning.sorting import sort_rows
from cleaning.types import convert_types


def standarize(df):
    df = standardize_columns(df)
    df = standardize_symbols(df)
    validate_schema(df)
    return convert_types(df)


def missing(df, output_dir="cleaned"):
    rejected_df = df[missing_row_mask(df)]
    export_rejected_data(rejected_df, output_dir, "missing_rows")
    return drop_missing_rows(df)


def duplicates(df, output_dir="cleaned"):
    rejected_df = df[duplicate_group_mask(df)]
    export_rejected_data(sort_rows(rejected_df), output_dir, "duplicate_rows")
    return drop_duplicate_rows(df)


def invalid(df, output_dir="cleaned"):
    rejected_df = df[invalid_price_mask(df)]
    export_rejected_data(rejected_df, output_dir, "invalid_prices")
    return drop_invalid_prices(df)


def ohlcviolation(df, output_dir="cleaned"):
    rejected_df = df[ohlc_violation_mask(df)]
    export_rejected_data(sort_rows(rejected_df), output_dir, "ohlc_violations")
    return df


def sort(df):
    return sort_rows(df).reset_index(drop=True)
