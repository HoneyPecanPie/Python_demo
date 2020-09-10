# 导入requests模块
import requests
#导入BeautifulSoup模块
from bs4 import BeautifulSoup
#定义变量url，设定要请求的网页地址：https://maoyan.com/films/1240752
url = 'https://maoyan.com/films/1203'
#定义请求头headers，添加User-Agent报头。User-Agent报头可以设置为：Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
# 利用requests.get()函数发送客户端请求。
response = requests.get(url,headers=headers)
# 读取出response中的HTML文档。提示：.content.decode('utf8')
html = response.content.decode('utf8')
# 解析HTML文档，提示：运用 BeautifulSoup(要解析的文本，'解析器')函数。
bs = BeautifulSoup(html,'html.parser')
# 利用find_all()方法找到昵称，class属性为'name'的<span>标签。
name = bs.find_all('span',class_='name')
# 利用find_all()方法找到评论，class属性为'comment-content'的<div>标签。
comment = bs.find_all('div',class_='comment-content')
#注意上面两步得到的都是列表数据。现在我们将他们进行输出。提示：Tag对象的text方法。
for i in range(0,len(comment)):
    print('用户： '+name[i].text)
    print('评论： '+comment[i].text+'\n')
