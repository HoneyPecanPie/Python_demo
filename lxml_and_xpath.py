from lxml import etree

# 使用lxml.etree.parse()函数打开XML文档
xml = etree.parse('one.xml')
# 利用XPath语法寻找标签
a = xml.xpath('//title/text()')
print(a)
