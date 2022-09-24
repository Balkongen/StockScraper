import pandas as pd
import sys
from script import COLUMNS

ticker = sys.argv[1]

data = pd.read_csv("stocks.csv")

if ticker not in data["Ticker"].values:
    print("The stock is not listed")
else:
    data = data.loc[data["Ticker"] != ticker]
    data.to_csv("stocks.csv")
