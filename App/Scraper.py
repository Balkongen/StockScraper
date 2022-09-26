from multiprocessing.sharedctypes import Value
import requests
from bs4 import BeautifulSoup
import pandas as pd

class Scraper:

    def __init__(self, ticker):
        self.ticker = ticker
        self.__org_url = "https://www.marketwatch.com/investing/stock/" + ticker
        self.__cashflow_url = "https://www.marketwatch.com/investing/stock/" + ticker + "/financials"
        self.__checkUrl()

    def __checkUrl(self):
        doc = self.__scrape(None)
        
        name = doc.find(class_="company__name")
        if name == None:
            raise ValueError("Ticker does not exist")
        # try:
        #     name = doc.find(class_="company__name")
        # except:
        #     raise ValueError()
        #     print("Wrong ticker symbol")

    def __scrape(self, url_x):
        if url_x == None:
            url = self.__org_url
        else:
            url = url_x
        
        res = requests.get(url=url).text
        return BeautifulSoup(res, "html.parser")

    def getName(self):
        doc = self.__scrape(None)
        return doc.find(class_="company__name").text

    def getPrice(self):
        doc = self.__scrape(None)
        price = doc.findChild(class_="intraday__price").text
        price = self.__format_string(price=price)
        return float(price)
        # return float(doc.findChild(class_="intraday__price").text.replace("kr", "").strip())

    def __format_string(self, price):
        symbols = ["kr", "$", "€"]
        
        price = str(price)
        price = price.strip()
        for x in symbols:
            price = price.replace(x, "")

        return price


    def getPriceEaringsRatio(self):
        doc = self.__scrape(None)
        container = doc.find(class_="list list--kv list--col50")
        items = container.findChildren(class_="kv__item")
        return float(items[8].find(class_="primary").text)

    def getCashFlow(self):
        doc = self.__scrape(self.__cashflow_url)
        link = doc.find("a", {"instrument-target": "financials/cash-flow"})["href"]
        doc = self.__scrape(link)
        table = doc.find("table", {"aria-label": "Financials - Financing Activities data table"}).findChildren("div")
        
        col = []
        for td in table:
            col.append(td.text)

        for ix, item in enumerate(col):
            if item == "Free Cash Flow":
                cash_flow = str(col[ix + 2])
                return self.__convertString(cash_flow)
        
    def __convertString(self, string):
        values = {"M": 1000000, "B": 1000000000, "Cr": 10000000,
            "L": 100000, "K": 1000, "Tr": 1000000000000}
        suffix = string[-1] 
        
        if suffix in values:
            string = float(string.replace(suffix, "")) * values.get(suffix)
        else:
            float(string)
        return string

    def to_pandas(self):
        columns = ["Ticker", "Name", "Price", "P/E", "Free Cash Flow"]
        data = [[
            self.ticker, 
            self.getName(),
            self.getPrice(),
            self.getPriceEaringsRatio(),
            self.getCashFlow()]]
        
        return pd.DataFrame(data=data, columns=columns)
       