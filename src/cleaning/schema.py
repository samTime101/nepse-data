from definitions import REQUIRED_COLUMNS

def validate_schema(df):
    # Check if all required columns are present in the dataframe
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    return df
