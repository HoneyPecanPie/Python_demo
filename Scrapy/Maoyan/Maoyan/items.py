# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


#定义MaoyanItem类，继承自scrapy.Item
class MaoyanItem(scrapy.Item):
    #定义电影名称的属性
    name = scrapy.Field()
    #定义主演信息的属性
    star = scrapy.Field()
    #定义上映时间的属性
    time = scrapy.Field()
