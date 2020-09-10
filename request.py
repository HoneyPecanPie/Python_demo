# 导入urllib.request库
import  urllib.request
# url作为Request()方法的参数，构造并返回一个Request对象
request = urllib.request.Request("http://www.baidu.com")
# Request对象作为urlopen()方法的参数，发送给服务器并接收响应
response = urllib.request.urlopen(request)
# 还是用read()方法从响应中读取到HTML文档
html = response.read()
# 将HTML文档写入文件 first.html
f = open('second.html','wb+')
f.write(html)
f.close()