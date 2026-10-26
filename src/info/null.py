from checks import missing_row_mask

def null(df):
    return df.isnull().sum()

def missing_rows(df):
    return missing_row_mask(df).sum()