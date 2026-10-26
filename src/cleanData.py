# FROM https://github.com/samTime101/nepse-ml

from pathlib import Path
from cleaning.export import export_cleaned_data
from cleaning.pipeline import duplicates, invalid, missing, ohlcviolation, sort, standarize
from info.dataframe import dataframe
from info.pipeline import info

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data" / "company-wise"
CLEANED_DIR = ROOT_DIR / "cleaned"

if CLEANED_DIR == DATA_DIR or DATA_DIR in CLEANED_DIR.parents:
    raise ValueError("CLEANED_DIR must be outside the raw data directory")


def main():
    df = dataframe(DATA_DIR)
    info(df)

    clean_df = standarize(df)
    clean_df = missing(clean_df, CLEANED_DIR)
    clean_df = duplicates(clean_df, CLEANED_DIR)
    clean_df = invalid(clean_df, CLEANED_DIR)
    clean_df = ohlcviolation(clean_df, CLEANED_DIR)
    clean_df = sort(clean_df)
    info(clean_df)

    export_cleaned_data(clean_df, CLEANED_DIR)


if __name__ == "__main__":
    main()
