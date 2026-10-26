from checks import missing_row_mask

def drop_missing_rows(df):
    # drop rows with missing values in any of the daily row columns
    return df[~missing_row_mask(df)].copy()
