
"""
Run the Crawler.

Date: 09/19/2018
"""

from crawler import Crawler
from storage.mysql import MySQLStorage
import argparse

# argument parser for password
parser = argparse.ArgumentParser(description='Supply the password.')
parser.add_argument('-f',
            dest='cities_filepath',
            required=True,
            type=str,
            help='the filepath to the list of cities')
parser.add_argument('-p',
            dest='password',
            required=True,
            type=str,
            help='the rds password')
args = parser.parse_args()

# get all cities
cities = []
with open(args.cities_filepath, 'r') as f:
    next(f)
    for city in f:
        city_params = city.split('","')
        city_name = city_params[1].replace('"','')
        state_name = city_params[2].replace('"','')
        cities.append('%s, %s' % (city_name, state_name))


# instantiate crawler
x = Crawler(cities=cities[::-1], gas_stations=['all'], storage=MySQLStorage(password=args.password), min_sleep_time=15, max_sleep_time=60)

# crawl
x.crawl()
