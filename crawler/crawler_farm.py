
"""
Run the Crawler.

Date: 09/19/2018
"""

from crawler import Crawler
from storage.mysql import MySQLStorage
import argparse

# argument parser for password
parser = argparse.ArgumentParser(description='Supply the password.')
parser.add_argument('-p',
            dest='password',
            required=True,
            type=str,
            help='the rds password')
args = parser.parse_args()

# get all CA cities
cities = []
with open('./cities/CA.csv', 'r') as f:
    for city in f:
        cities.append(city.strip())

# instantiate crawler
x = Crawler(cities=cities, gas_stations=['all'], storage=MySQLStorage(password=args.password), min_sleep_time=15, max_sleep_time=60)

# crawl
x.crawl()
