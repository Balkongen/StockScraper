import unittest
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
    
    def test_get_cashFlow_swedish(self):
        scraper = Scraper("shb.a")
        x = float(scraper.getCashFlow())

    def test_get_cashFlow_american(self):
        scraper = Scraper("msft")
        x = float(scraper.getCashFlow())

    def test_get_ticker_of_company_no_exist(self):
        with self.assertRaises(ValueError):
            scraper = Scraper("noTicker")


if __name__ == "__main__":
    unittest.main()
