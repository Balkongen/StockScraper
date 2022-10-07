import sys
from Scraper import Scraper

input_ticker = sys.argv[1]

scraper = Scraper(input_ticker)

print(scraper.to_string())