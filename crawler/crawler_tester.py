"""
Test the Crawler.

Date: 09/11/2018
"""

from crawler import Crawler

x = Crawler(cities=['San Ramon', 'Pomona'], gas_stations=['all'], min_sleep_time=15, max_sleep_time=30)

x.crawl()
