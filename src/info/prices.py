from checks import invalid_price_mask, ohlc_violation_mask

def invalid_prices(df):
    return invalid_price_mask(df).sum()

def ohlc_violations(df):
    return ohlc_violation_mask(df).sum()