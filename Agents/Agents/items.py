# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AgentsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Name = scrapy.Field()
    Job_Title = scrapy.Field()
    Image_url = scrapy.Field()
    Address = scrapy.Field()
    Contact_Number = scrapy.Field()
    Social = scrapy.Field()
