# 导入urllib.request库
import  urllib.request
# 向指定的URL发送请求，并返回服务器响应的类文档对象
Response = urllib.request.urlopen('http://www.baidu.com')
# 类文件对象支持 文件对象的操作方法，read()方法读取文件全部内容，返回字符串
Html = Response.read()
# 将HTML文档写入文件 first.html
f = open('first.html','wb+')
f.write(Html)
f.close()