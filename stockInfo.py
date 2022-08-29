# get all stock info

import pandas as pd
from bs4 import BeautifulSoup
import requests
import sys
import re

COLUMNS = ["Ticker", "Name", "Price", "P/E", "EPS", "FCF-PS"]
URL = "https://www.marketwatch.com/investing/stock/"

res = requests.get(url="https://www.marketwatch.com/investing/stock/shb.a/financials/cash-flow?countrycode=se").text
doc = BeautifulSoup(res, "html.parser")

tables = doc.find("table",{"class": "table table--overflow align--right"})

table_row = tables.find("tr")

years = table_row.findChildren("div")

print(years)

arr = []
for x in years:
    arr.append(x.text)

r = re.compile(r'[0-9]{4}')
actual_years = list(filter(r.match, arr))


print(actual_years)
# if re.match(r'Item', years):
#     print("yes")

# for x in years:
#     if 
#     print(x.text)

# for x in yearO:
#     print(x)
# print(yearO)

# def getStockInfo(url):
#     res = requests.get(url).text
#     doc = BeautifulSoup(res, "html.parser")

#     container = doc.find(class_="list list--kv list--col50")

#     ticker = doc.find(class_="company__ticker").text
#     name = doc.find(class_="company__name").text
#     price = doc.findChild(class_="intraday__price").text.replace("kr", "").strip()
#     items = container.findChildren(class_="kv__item")
#     pe = items[8].find(class_="primary").text
    
#     return ticker, name, price, pe