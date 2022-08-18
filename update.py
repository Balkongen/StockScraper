import pandas as pd
from bs4 import BeautifulSoup
import requests
import os
from script import getStockInfo, COLUMNS

URL = "https://www.marketwatch.com/investing/stock/"
STOCKS = []

res = requests.get(url=URL).text
doc = BeautifulSoup(res, "html.parser")

# if os.path.getsize("stocks.csv") == 0:
#     print("File is empty")
# else:

orgData = pd.read_csv("stocks.csv")

new_data = None

for ix in range(len(orgData)):
    ticker = orgData.loc[ix, "Ticker"]
    stockInfo = getStockInfo(url=URL + ticker)
    STOCKS.append(stockInfo)

new_data = pd.DataFrame(data=STOCKS, columns=COLUMNS)
new_data.to_csv("stocks.csv")
print(new_data)