import pandas as pd
from bs4 import BeautifulSoup
import requests
import sys
import os

# ticker = sys.argv[1]

url = "https://www.marketwatch.com/investing/stock/msft?mod=search_symbol"

res = requests.get(url).text
doc = BeautifulSoup(res, "html.parser")

container = doc.find(class_="list list--kv list--col50")

name = doc.find(class_="company__name").text
items = container.findChildren(class_="kv__item")
price = items[0].find(class_="primary").text
pe = items[8].find(class_="primary").text

# print(name)
# print(price)
# print(pe)

if os.path.getsize("stocks.csv") == 0:
    data = [[name, price, pe]]
    df = pd.DataFrame(data, columns=["Name", "Price", "P/E"])
else:
    dict = {"Name": name, "Price": price, "P/E": pe}
    df = df.append(dict, ignore_index=True)

df.to_csv("stocks.csv",index=False,header=False)

print(df)