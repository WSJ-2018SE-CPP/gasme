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


class Crawler:
    """
    A Crawler class for crawling GoogleMaps gas station prices.
    """

    def __init__(self, lat, lon):
        """
        Initializes a crawler.

        Args:
          lat: the initial latitude
          lon: the initial longitude
        """
        
        self.lat = lat
        self.lon = lon

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
        res = self._search(self.lat, self.lon)
        print(res)

        # add to database???

    
    def _search(self, lat, lon):
        """
        Search the latitude and longitude for gas station information.

        Args:
          lat: the latitude
          lon: the longitude
        """

        # url to search
        url = 'https://www.google.com/maps/search/gas+prices/@%f,%f' % (lat, lon)

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
        s = '\\"gas prices\\"' 
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
                    res.append(html[beg:end])
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

        beg = block.find('[', 1)
        beg = block.find('[', beg+1)
        end = block.find(']', beg+1)

        return dict(address=block[beg:end])

