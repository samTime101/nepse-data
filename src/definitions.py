REQUIRED_COLUMNS = ["published_date","symbol","open","high","low","close","traded_quantity","traded_amount",]

NUMERIC_COLUMNS = ["open","high","low","close","per_change","traded_quantity","traded_amount","status",]

PRICE_COLUMNS = ["open", "high", "low", "close"]

KEY_COLUMNS = ["symbol", "published_date"]

DAILY_ROW_COLUMNS = ["published_date", "symbol", *PRICE_COLUMNS] # unpack price cols