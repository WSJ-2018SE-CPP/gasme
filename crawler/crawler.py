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
from storage.csv import CSVStorage
import time


class Crawler:
    """
    A Crawler class for crawling GoogleMaps gas station prices.
    """

    def __init__(self, cities, gas_stations, sleep=5):
        """
        Initializes a crawler.

        Args:
          cities: a list of "city, state"
          gas_stations: a list of gas stations
          sleep: number of seconds to sleep after web request
        """
       
        # list of cities
        self.cities = cities

        # list of gas stations
        self.gas_stations = gas_stations

        # sleep time 
        self.sleep = sleep

        # parser for the gas station blocks
        self.parser = Parser()

        # mapping between parameter and location in parser, learned from testing
        self.params = dict([
            ('address',[14,37,0,0,17,0]),
            ('brand',[14,11]),
            ('price_1',[14,86,0,0,0]),
            ('price_2',[14,86,0,1,0]),
            ('price_3',[14,86,0,2,0]),
            ('lat',[14,9,2]),
            ('lon',[14,9,3])
        ])

        # storage medium
        self.storage = CSVStorage(fname='./storage/test.csv', keys=self.params.keys())


    def crawl(self):
        """
        Begin crawling.
        """

        # for each city
        for city in self.cities:

            # for each gas station
            for gas_station in self.gas_stations:

                # search the area
                res = self._search(city, gas_station)

                # politeness sleeping (maybe can optimize for right after web request)
                time.sleep(self.sleep)

                # store the results
                self.storage.store(res)

    
    def _search(self, city, gas_station):
        """
        Search the latitude and longitude for gas station information.

        Args:
          city: the city to search
          gas_station: the gas station to search
        """

        # print feedback
        print('Searching %s gas stations in %s --> ' % (gas_station, city), end='', flush=True)

        # url to search
        url = 'https://www.google.com/maps/search/%s+gas+prices+%s' % (gas_station.replace(' ', '+'), city.replace(' ','+'))

        # search results
        res = []

        # read the url
        with urllib.request.urlopen(url) as response:

            # extract gas station blocks
            for block in self._get_gas_station_blocks(response.read().decode('utf-8'), gas_station):

                # extract data from the blocks
                res.append(self._extract_info_from_block(block))

        # print feedback
        print('Found %d' % len(res), flush=True)

        # return results
        return res


    def _get_gas_station_blocks(self, html, gas_station):
        """
        Extract gas station information blocks from the raw html.

        Args:
          html: the raw html
          gas_station: the gas station
        """

        # array for the resulting blocks
        res = []

        # find the beginning of the first gas station block
        s = '\\"%s gas prices' % gas_station
        beg = html.find(s, 0)
        beg = html.find(s, beg+len(s))
        beg = html.find(s, beg+len(s))
        beg = html.find('[', beg+len(s))

        # extract the gas blocks
        while True:

            # if ] occurs before [, there are no more gas station blocks
            if html[beg:].find(']') < html[beg:].find('['):
                break

            # get the starting index of the block
            beg = html.find('[', beg)

            # counter, +1 for [ and -1 for ]. when x == 0, the block is complete.
            # x will always be incremented from the first character because
            # we have set beg to [. Therefore, we check complete after + or - x.
            x = 0

            # initialize the end of the block
            end = beg

            # for each character in the text starting at the beginning block character
            for c in html[beg:]:

                # increment x
                if c == '[':
                    x += 1

                # decrement x
                elif c == ']':
                    x -= 1

                # append block if closed
                if x == 0:
                    res.append(html[beg:end+1])
                    beg = end + 1
                    break

                # increment end
                end += 1
        
        # return the blocks
        return res


    def _extract_info_from_block(self, block):
        """
        Extracts relevant information from html gas station block.

        Args:
          block: the gas station block
        """

        # dictionary object for results
        d = dict()

        # parse the current block
        self.parser.parse(block)

        # extract data from the parser
        for key, value in self.params.items():
            d[key] = self.parser.search(value)

        # return the results
        return d

