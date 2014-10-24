from scrapy.spider import Spider
from scrapy.selector import Selector

from scrapy_tutorial.items import LivingsocialItem 

class LivingsocialSpider(Spider):
	name = "livingsocial"
	allowed_domains = ["livingsocial.com"]
	start_urls = [
		"https://www.livingsocial.com/cities/13-san-jose"
		]

	def parse(self, response):
		sel = Selector(response)	
