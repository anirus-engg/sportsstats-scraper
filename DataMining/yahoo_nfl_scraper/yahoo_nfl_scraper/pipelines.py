# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class YahooNflScraperPipeline(object):

    def process_item(self, item, spider):
        for key, value in item.iteritems():
            if key == 'player':
                item[key] = item[key].pop()
            else:
                item[key] = item[key].pop().encode('ascii', errors='ignore')
            print "PIPELINE: Got ", item[key]
        return item
