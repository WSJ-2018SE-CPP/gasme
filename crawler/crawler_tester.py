"""
Test the Crawler.

Date: 09/11/2018
"""

from crawler import Crawler


#x = Crawler(cities=['Pomona, CA', 'Covina, CA', 'Diamond Bar, CA', 'Ontario, CA'], gas_stations=['all','76', 'Chevron', 'ARCO', 'Shell', 'Mobil'])
x = Crawler(cities=['Pomona, CA', 'Covina, CA', 'Eugene, OR', 'Orlando, FL'], gas_stations=['all', '76'])

x.crawl()
