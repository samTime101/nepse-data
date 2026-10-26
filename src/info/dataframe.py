from pathlib import Path
import pandas as pd

from definitions import KEY_COLUMNS

def dataframe(dataset):
    files = sorted(Path(dataset).glob("*.csv"))
    if not files:
        raise FileNotFoundError(f"No CSV files found in {dataset}")

    all_data = []
    for file in files:
        company_df = pd.read_csv(file)
        company_df["symbol"] = file.stem # NABIL.csv -> NABIL
        all_data.append(company_df)

    # fresh indexing
    df = pd.concat(all_data, ignore_index=True)
    df["published_date"] = pd.to_datetime(df["published_date"])

    # reset index and sort by symbol and published_date
    df = df.sort_values(KEY_COLUMNS).reset_index(drop=True)
    return df
