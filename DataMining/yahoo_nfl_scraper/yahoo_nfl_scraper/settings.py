# Scrapy settings for yahoo_nfl_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'yahoo_nfl_scraper'

SPIDER_MODULES = ['yahoo_nfl_scraper.spiders']
NEWSPIDER_MODULE = 'yahoo_nfl_scraper.spiders'

ITEM_PIPELINES = {
    'yahoo_nfl_scraper.pipelines.YahooNflScraperPipeline': 100,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'yahoo_nfl_scraper (+http://www.yourdomain.com)'
