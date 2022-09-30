import unittest
from parameterized import parameterized
from App.Scraper import Scraper

import pandas as pd

class Test_Scraper(unittest.TestCase):
    
    SCRAPER_SWE = Scraper("shb.a")
    SCRAPER_US = Scraper("msft")

    def test_get_ticker_of_company_no_exist(self):
        with self.assertRaises(ValueError):
            scraper = Scraper("noTicker")

    def test_get_ticker(self):
        self.assertEqual(self.SCRAPER_US.ticker, "msft")
    
    def test_get_name(self):
        self.assertEqual(self.SCRAPER_US.getName(), "Microsoft Corp.")

    # TODO
    # change these tests (price)
    def test_get_price_american(self):
        scraper = Scraper("msft")
        scraper.getPrice()

    def test_get_price_swedish(self):
        scraper = Scraper("shb.a")
        scraper.getPrice()
    
    @parameterized.expand(["shb.a","msft"])
    def test_get_cashFlow_swedish(self, ticker):
        scraper = Scraper(ticker=ticker)
        cash_flow = scraper.getCashFlow()
        
        self.assertEqual(type(cash_flow), float)

    def test_get_cashFlow(self):
        cash_flow = self.SCRAPER_SWE.getCashFlow()
        self.assertEqual(type(cash_flow), float)
    
    def test_get_peratio(self):
        pe = self.SCRAPER_SWE.getCashFlow()
        self.assertEqual(type(pe), float)
    
    def test_if_pandasIsofcorrectdatatype(self):
        stock_pd = self.SCRAPER_SWE.to_pandas()
        df = pd.DataFrame()
        self.assertEqual(type(stock_pd), type(df))

    def test_to_string_format(self):
        self.assertEqual(self.SCRAPER_SWE.to_string(),
        "Name: " + str(self.SCRAPER_SWE.getName()) + " \n" +
        "Price: " + str(self.SCRAPER_SWE.getPrice()) + " \n" +
        "P/E: " + str(self.SCRAPER_SWE.getPriceEaringsRatio()))

if __name__ == "__main__":
    unittest.main()
