# import required library and required constants
import time
import requests
import pandas as pd
from pathlib import Path
from bs4 import BeautifulSoup
from utils.status import getStatus
from utils.symbols import file_stem
from utils.session import TIMEOUT
from constants.url import dailyPriceUrl

html = requests.get(dailyPriceUrl, timeout=TIMEOUT).text
bs = BeautifulSoup(html, "lxml")

# today date in yyyy-mm-dd format
today = bs.find("span", {"class": "text-org"}).text

# get html tables
tables = pd.read_html(html)

# select the first table i.e. the stock price table
dataTable = tables[0]

# Normalize symbols once so slash-containing debentures match their
# underscores-instead-of-slashes CSV filenames (GBILD84/85 -> GBILD84_85).
dataTable["Symbol"] = dataTable["Symbol"].map(file_stem)

fileDir = Path("../data/company-wise/")
for file in fileDir.glob("*.csv"):
    # first check if data already exist for this date
    existingDf = pd.read_csv(file)
    lastRow = existingDf.iloc[-1]
    lastDate = lastRow["published_date"]
    if str(lastDate) != str(today):
        symbol = file.stem
        data = dataTable.loc[dataTable["Symbol"] == symbol]
        if len(data) == 1:
            status = getStatus(float(data["Open"]), float(data["Close"]))
            dataRow = [
                [
                    today,
                    float(data["Open"]),
                    float(data["High"]),
                    float(data["Low"]),
                    float(data["Close"]),
                    float(data["Diff %"]),
                    float(data["Vol"]),
                    float(data["Turnover"]),
                    status,
                ]
            ]
            dataframe = pd.DataFrame(dataRow)
            dataframe.to_csv(file, mode="a", header=False, index=False)
