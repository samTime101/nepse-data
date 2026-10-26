from checks import duplicate_row_mask

def drop_duplicate_rows(df):
    # return a copy of the dataframe with duplicate rows based on KEY_COLUMNS dropped, keeping the last occurrence
    return df[~duplicate_row_mask(df)].copy()
