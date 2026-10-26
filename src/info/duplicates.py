from checks import duplicate_group_mask, duplicate_row_mask

def duplicates(df):
    # returns the number of duplicate rows
    return df.duplicated().sum()

def duplicate_rows(df):
    # returns the number of duplicate rows based on KEY_COLUMNS
    return duplicate_row_mask(df).sum()


def duplicate_group_rows(df):
    # returns the number of rows that are part of a duplicate group based on KEY_COLUMNS
    return duplicate_group_mask(df).sum()