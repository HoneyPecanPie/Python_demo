import json
import jsonpath
file = open('two.json',encoding='utf8')
# json.load()函数加载文件
Dict = json.load(file)
# 利用JsonPath模块提取msg下面的信息。
msg = jsonpath.jsonpath(Dict, '$.msg')
print(msg)
