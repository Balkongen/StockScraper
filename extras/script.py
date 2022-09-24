import pandas as pd
from bs4 import BeautifulSoup
import requests
import sys
import os

COLUMNS = ["Ticker", "Name", "Price", "P/E"]

def getStockInfo(url):
    res = requests.get(url).text
    doc = BeautifulSoup(res, "html.parser")

    container = doc.find(class_="list list--kv list--col50")

    ticker = doc.find(class_="company__ticker").text
    name = doc.find(class_="company__name").text
    price = doc.findChild(class_="intraday__price").text.replace("kr", "").strip()
    items = container.findChildren(class_="kv__item")
    pe = items[8].find(class_="primary").text
    
    return ticker, name, price, pe

def main():
    input_ticker = sys.argv[1]
    url = "https://www.marketwatch.com/investing/stock/" + input_ticker
    info = getStockInfo(url=url)

    data = None
    stockInfo = [info]
    stockName = info[1]

    if os.path.getsize("stocks.csv") == 0:
        data = pd.DataFrame(data=stockInfo, columns= COLUMNS)
    else:
        data = pd.read_csv("stocks.csv")
        if stockName not in data["Name"].values:
            data.loc[len(data)] = stockInfo[0]
        else:
            print("Stock already in list")
    data.to_csv("stocks.csv",index=False)
    print(data)

if __name__ == "__main__":
    main()