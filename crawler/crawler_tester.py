"""
Test the Crawler.

Date: 09/11/2018
"""

from crawler import Crawler

cities = []

with open('./cities/CA.csv', 'r') as f:
    for city in f:
        cities.append(city.strip())


x = Crawler(cities=cities, gas_stations=['all'], sleep_time=30)

x.crawl()
