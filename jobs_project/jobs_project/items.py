# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class JobsProjectItem(Item):
    title = Field()
    description = Field()
    city = Field()
    country = Field()
