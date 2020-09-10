# 导入requests模块
import requests
from lxml import etree
import openpyxl
#导入BeautifulSoup模块
from bs4 import BeautifulSoup
#定义变量url，设定要请求的网页地址：https://maoyan.com/films/1240752
a = input('请输入你想爬取的页数（请输入数字）： ')

str1 = 'https://movie.douban.com/subject/26754233/comments?start='
str2 = '&limit=20&sort=new_score&status=P'
    # 定义保存贴吧不同URL链接的列表
url_list = []
for i in range(0,int(a)):
        # 求出第i页的pn值
    pn = i*20
        # 利用字符串的拼接构造第i 页的URL链接
    url = str1+str(pn)+str2
        # 利用append方法将该URL链接填入url_list列表
    url_list.append(url)



name=[]
star=[]
comment=[]
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
# 利用requests.get()函数发送客户端请求。
for i in range(len(url_list)):
#定义请求头headers，添加User-Agent报头。User-Agent报头可以设置为：Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.
    response = requests.get(url_list[i],headers=headers)
# 读取出response中的HTML文档。提示：.content.decode('utf8')
    text = response.content.decode('utf8')
# 解析HTML文档，提示：运用 BeautifulSoup(要解析的文本，'解析器')函数。
    bs = BeautifulSoup(text,'html.parser')
# 利用find_all()方法找到昵称，class属性为'name'的<span>标签。
    HTML = etree.HTML(text)
    name1 = HTML.xpath('//div[@class="comment-item"]//span[@class="comment-info"]/a')
    star1 = HTML.xpath('//div[@class="comment-item"]//span[@class="comment-info"]/span[2]/@class')



# 利用find_all()方法找到评论，class属性为'comment-content'的<div>标签。
    comment1 = bs.find_all('span',class_='short')
    name.append(name1)
    star.append(star1)
    comment.append(comment1)
#注意上面两步得到的都是列表数据。现在我们将他们写入csv文件。提示：Tag对象的text方法。
#利用openpyxl.Workbook()函数创建新的workbook（工作薄）对象，就是创建新的空的Excel文件。



wb = openpyxl.Workbook()
#wb.active就是获取这个工作薄的活动表，通常就是第一个工作表。
sheet = wb.active
#可以用.title给工作表重命名。现在第一个工作表的名称就会由原来默认的“sheet1”改为你命名的值。
sheet.title = '八佰'
#先把要写入的每一行内容，赋值给row。然后把每一行一次写入Excel文件。提示：for循环
row = ['用户名','评分','评论']
sheet.append(row)
for i in range(0,len(name)):
    for j in range(0,len(name1)):
        row = [name[i][j].text,star[i][j][7]+"星",comment[i][j].text]
        sheet.append(row)
#保存新建的Excel文件，并命名为“one.xlsx”
wb.save('douban comments.xlsx')
