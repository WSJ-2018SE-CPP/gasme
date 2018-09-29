"""
Crawler definition for extracting gas station information from GoogleMaps.

Version 1.0:
    - address
    - lat/lon
    - gas price (3 tiers)
    - brand (76, Shell, etc.)

Date: 09/11/2018
"""

import urllib.request
from parser.parser import Parser
from random import randint
import time

class Crawler:
    """
    A Crawler class for crawling GoogleMaps gas station prices.
    """

    def __init__(self, cities, gas_stations, storage, min_sleep_time=15, max_sleep_time=60):
        """
        Initializes a crawler.

        Args:
          cities: a list of "city, state"
          gas_stations: a list of gas stations
          sleep_time: number of seconds to sleep after web request
        """
       
        # list of cities
        self.cities = cities

        # list of gas stations
        self.gas_stations = gas_stations

        # sleep time 
        self.min_sleep_time = min_sleep_time
        self.max_sleep_time = max_sleep_time

        # parser for the gas station blocks
        self.parser = Parser()

        # parameters to extract
        self.params = ['address', 'brand', 'lat', 'lon', 'price_1', 'price_2', 'price_3']

        # storage medium
        self.storage = storage


    def crawl(self):
        """
        Begin crawling.
        """

        # for each city
        for city in self.cities:

            # store data per city so less connections to db made
            data = []

            # for each gas station
            for gas_station in self.gas_stations:

                # search the area
                res = self._search(city, gas_station)

                # politeness sleeping within a random range, so we don't seem like a robot
                time.sleep(randint(self.min_sleep_time, self.max_sleep_time))

                # append the results
                data.append(res)

            # store the results
            self.storage.store_data(res)

    
    def _search(self, city, gas_station):
        """
        Search the latitude and longitude for gas station information.

        Args:
          city: the city to search
          gas_station: the gas station to search

        Return:
          A list of gas station information for each station within the html from the url request
        """

        # print feedback
        print('Searching %s gas stations in %s --> ' % (gas_station, city), end='', flush=True)

        # url to search
        url = 'https://www.google.com/maps/search/%s+gas+prices+%s' % (gas_station.replace(' ', '+'), city.replace(' ','+'))

        # read the url
        with urllib.request.urlopen(url) as response:

            # parse the html for gas station information
            res = self.parser.parse(html=response.read().decode('utf-8'),
                    gas_station=gas_station,
                    params=self.params)

            # print feedback
            print('Found %d' % len(res), flush=True)

            # return results
            return res
        
        # print feedback
        print('Found %d' % 0, flush=True)

        # return empty list if couldn't open url
        return []

