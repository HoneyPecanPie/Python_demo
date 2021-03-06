import scrapy
from ..items import MaoyanItem

class MaoyanSpider(scrapy.Spider):
    # 爬虫名
    name = 'maoyan'
    # 允许爬取的域名
    allowed_domains = ['maoyan.com']
    offset = 0
    # 起始的URL地址
    start_urls = ['https://maoyan.com/board/4?offset=0']

    def parse(self, response):

        # 基准xpath,匹配每个电影信息节点对象列表
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        # dd_list : [<element dd at xxx>,<...>]
        for dd in dd_list:
            # 创建item对象
            item = MaoyanItem()
            # [<selector xpath='' data='霸王别姬'>]
            # dd.xpath('')结果为[选择器1,选择器2]
            # .extract() 把[选择器1,选择器2]所有选择器序列化为unicode字符串
            # .extract_first() : 取第一个字符串
            item['name'] = dd.xpath('./a/@title').extract_first().strip()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').extract()[0].strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').extract()[0]

            # print(item)
            yield item

        self.offset += 10
        if self.offset <= 90:
            url = 'https://maoyan.com/board/4?offset={}'.format(str(self.offset))

            yield scrapy.Request(
                url=url,
                callback=self.parse
            )