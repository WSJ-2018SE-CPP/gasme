"""
Crawler definition for extracting gas station information from GoogleMaps.

Version 1.0:
    - address
    - lat/lon
    - regular gas price
    - brand (76, Shell, etc.)

Date: 09/11/2018
"""

import urllib.request
from parser.parser import Parser


class Crawler:
    """
    A Crawler class for crawling GoogleMaps gas station prices.
    """

    def __init__(self, city):
        """
        Initializes a crawler.

        Args:
          lat: the initial latitude
          lon: the initial longitude
        """
       
        # starting city, maybe?
        self.city = city

        # parser for the gas station blocks
        self.parser = Parser()

        '''
        How to move the crawler???
        - supply boundary??
        - supply movement distance???
        - queue????
        '''


    def crawl(self):
        """
        Begin crawling.
        """

        # maybe a queue???

        # search the lat and long
        res = self._search(self.city)

        # print results for now
        for r in res:
            print(r)

        # add to database???

    
    def _search(self, city):
        """
        Search the latitude and longitude for gas station information.

        Args:
          city: the city to search
        """

        # url to search
        url = 'https://www.google.com/maps/search/gas+prices+%s' % city.replace(' ','+')

        # search results
        res = []

        # read the url
        with urllib.request.urlopen(url) as response:

            # extract gas station blocks
            for block in self._get_gas_station_blocks(response.read().decode('utf-8')):

                # extract data from the blocks
                res.append(self._extract_info_from_block(block))

        # return results
        return res


    def _get_gas_station_blocks(self, html):
        """
        Extract gas station information blocks from the raw html.

        Args:
          html: the raw html
        """

        # array for the resulting blocks
        res = []

        # find the beginning of the first gas station block
        s = '\\"gas prices' 
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

        # extract the data from the known locations
        d['address'] = self.parser.search([14, 37, 0, 0, 17, 0])
        d['brand'] = self.parser.search([14,11])
        d['price'] = self.parser.search([14,86,0,0,0])

        # return the results
        return d

