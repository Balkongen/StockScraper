import unittest
from parameterized import parameterized
from App.Scraper import Scraper

class Test_Scraper(unittest.TestCase):
    
    def test_get_ticker(self):
        scraper = Scraper("msft")
        self.assertEqual(scraper.ticker, "msft")
    
    def test_get_name(self):
        scraper = Scraper("msft")
        self.assertEqual(scraper.getName(), "Microsoft Corp.")

    def test_get_price_american(self):
        scraper = Scraper("msft")
        # self.assertEqual(scraper.getPrice(), 238.08)
        scraper.getPrice()

    def test_get_price_swedish(self):
        scraper = Scraper("shb.a")
        scraper.getPrice()
    
    @parameterized.expand(["shb.a","msft"])
    def test_get_cashFlow_swedish(self, ticker):
        scraper = Scraper(ticker=ticker)
        cash_flow = scraper.getCashFlow()
        self.assertEqual(type(cash_flow), float)

    def test_get_cashFlow_american(self):
        scraper = Scraper("msft")
        x = scraper.getCashFlow()
        self.assertEqual(type(x), float)

    def test_get_ticker_of_company_no_exist(self):
        with self.assertRaises(ValueError):
            scraper = Scraper("noTicker")

    def test_get_pe_ratio(self):
        scraper = Scraper("msft")
        pe = scraper.getPriceEaringsRatio()
        self.assertEqual(type(pe), float)

if __name__ == "__main__":
    unittest.main()
