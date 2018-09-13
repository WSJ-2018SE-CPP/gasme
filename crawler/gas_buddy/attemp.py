#! /usr/bin/python
from lxml import html
import requests

class AppCrawler:
  def __init__(self, starting_url, depth):
	  self.starting_url = starting_url
	  self.depth = depth
	  self.apps = []

  def crawl(self):
	  # All the crawl logic goes here.
	  self.get_app_from_link(self.starting_url)
	  return

  def get_app_from_link(self, link):
	  print "********* get_app_from_link ****************"
	  # Get information from link
	  start_page = requests.get(link)
	  tree = html.fromstring(start_page.text)
	  div = "h2"
	  _id = "class"
	  content = "section__headline" 
	  path = '//'+ div + '[@' + _id + '=\"' + content + '\"]/text()'
	  print path

	  name = tree.xpath(path)[0]
	  #name = tree.xpath('//h2[@class="section__headline"]/text()')[0]
	  print name
	  return

# Do something with the data. We'll just be printing it.
# We can do some analytics or whatever.
class App:
  def __init__(self, name, developer, price, links):
	  self.name = name
	  self.developer = developer
	  self.price = price
	  self.links = links

  def __str__(self):
  	return ("Name" + self.name.encode('UTF-8') + "\r\nDeveloper: " + self.developer.encode('UTF-8') + "\r\nPrice: " + self.price.encode('UTF-8') + "\r\n")

			    
def main():
# Execution starts here
	crawler = AppCrawler('https://itunes.apple.com/us/app/candy-crush-saga/id553834731?mt=8', 0)
	crawler.crawl()
	for app in crawler.apps:
		print app
	    
if __name__ == "__main__": main()
