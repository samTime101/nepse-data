from definitions import KEY_COLUMNS

def sort_rows(df):
    # return a copy of the dataframe sorted by KEY_COLUMNS and reset the index
    # stable le chai duplicated KEY_COLUMNS ko order maintain garna help garcha, used in export
    # if there is no duplicate KEY_COLUMNS, stable sorting will not affect the order of rows
    return df.sort_values(KEY_COLUMNS, kind="stable").reset_index(drop=True)
