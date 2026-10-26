from checks import invalid_price_mask

def drop_invalid_prices(df):
    # drop rows with invalid prices
    return df[~invalid_price_mask(df)].copy()