from scrapy.spider import Spider
from scrapy.selector import Selector
from yahoo_nfl_scraper.items import YahooNflPassingScraperItem

class YahooNflSpider(Spider):
    name = "YahooNflPassing"
    start_urls = [
        "http://sports.yahoo.com/nfl/stats/bycategory?cat=Passing&conference=NFL&year=season_2013&timeframe=Week1&sort=626"
    ]

    def parse(self, response):
        sel = Selector(response)
        items = []
        i=0

        select = sel.xpath('//*[@id="yom-league-stats"]/table[5]/tr[4]/td[6]/text()').extract().pop().encode('ascii', errors='ignore')
        #print select
        players = sel.xpath('//*[@id="yom-league-stats"]/table[5]/tr[position() > 2]')
        for player in players:
            item = YahooNflPassingScraperItem()
            item['player'] = player.xpath('td[1]/a/text()').extract()
            item['comp'] = player.xpath('td[6]/text()').extract()
            item['att'] = player.xpath('td[7]/text()').extract()
            item['yds'] = player.xpath('td[8]/text()').extract()
            item['td'] = player.xpath('td[12]/text()').extract()
            item['int'] = player.xpath('td[11]/text()').extract()
            item['sack'] = player.xpath('td[14]/text()').extract()
            item['fum'] = player.xpath('td[17]/text()').extract()
            items.append(item)

        return items
