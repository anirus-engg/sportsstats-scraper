# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class YahooNflPassingScraperItem(Item):
    # define the fields for your item here like:
    # name = Field()
    player = Field()
    comp = Field()
    att = Field()
    yds = Field()
    td = Field()
    int = Field()
    sack = Field()
    fum = Field()
    pass

class YahooNflRushingScraperItem(Item):
    player = Field()
    car = Field()
    yds = Field()
    td = Field()
    lng = Field()
    fum = Field()
    pass

