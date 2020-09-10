import requests
import time
from lxml import etree
import re

def GetInfo():
    a = input('请输入你想爬取的贴吧名称（例如想爬取python吧，就输入“python”）： ')
    b = input('请输入你想爬取该贴吧的页数（请输入数字）： ')
    return a,b

def GetURL(a,b):
    str1 = 'http://tieba.baidu.com/f?kw='
    str2 = '&ie=utf-8&pn='
    # 定义保存贴吧不同URL链接的列表
    url_list = []
    for i in range(0,int(b)):
        # 求出第i页的pn值
        pn = i*50
        # 利用字符串的拼接构造第i 页的URL链接
        url = str1+a+str2+str(pn)
        # 利用append方法将该URL链接填入url_list列表
        url_list.append(url)
    return  url_list

def LoadPage(url_list):
    # 获取url_list中URL链接的个数。
    url_number = len(url_list)
    # 定义存储 b 个HTML文档的列表 html
    html = []
    # 定义请求头,模拟浏览器进行访问
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    for i in range(0,url_number):
        response = requests.get(url_list[i],headers=headers)
        text = response.content.decode('utf8')
        #利用append方法将爬取到的HTML文档保存到  html  列表
        html.append(text)
    return html

def GetTiezi(html):
    # 参数html为存储贴吧每个不同页面HTML文档的列表。
    # 获取列表html中，HTML文档的个数
    html_number = len(html)
    all_title = []
    all_href = []
    for i in range(0,html_number):
        # 利用lxml模块解析HTML文档,同时把HTML文档中的注释语句’<!---->‘删掉。
        html[i] = html[i].replace('<!--','')
        html[i] = html[i].replace('-->','')
        HTML = etree.HTML(html[i])
        # 获取每一页贴吧HTML文档中每个贴子的标题
        result_title = HTML.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/text()')
        # 将获取到的每一页的贴子标题进行存储
        all_title.append(result_title)
        # 获取每一页贴吧HTML文档中每个贴子标题的跳转链接
        result_href = HTML.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/@href')
        # 对每一个爬取到的跳转链接，通过字符串拼接补充 ’ http://tieba.baidu.com‘ ，使链接完整。
        a = 'http://tieba.baidu.com'
        for i in range(0,len(result_href)):
            result_href[i] = a + result_href[i]
        # 将获取到的每一页的帖子跳转链接进行存储
        all_href.append(result_href)
    # 这样，all_title和all_href 就保存了b页贴吧HTML文档中的所有贴子标题和贴子跳转链接
    return all_title,all_href

def GetAllData(all_title,all_href):
    # 获去贴吧的页数
    number_tieba = len(all_href)
    f = open('AllData.txt', 'w+', encoding='utf8')
    # 定义请求头
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    for i in range(0,number_tieba):
        print('正在获取第'+str(i+1)+'页贴吧的所有贴子信息......')
        # 获取该页贴吧的贴子的数目
        number_teizi = len(all_href[i])
        print('该页共'+str(number_teizi)+'个帖子\n')
        for  j  in range(0,number_teizi):
            # 对每一个帖子的url地址发送GET请求
            time.sleep(2)
            print('正在下载第'+str(j+1)+'个帖子的内容...')
            response = requests.get(all_href[i][j],headers = headers)
            html_teizi = response.content.decode('utf8')
            title = '\n\n第'+str(i+1)+'页贴吧第'+str(j+1)+'个贴子的标题: '
            f.write(title+all_title[i][j]+'\n')
            f.write(all_href[i][j]+'\n')
            # 利用正则表达式匹配到每一个楼层的区域。
            pattern = re.compile('<cc>.*?</cc>',re.S)
            huifu = pattern.findall(html_teizi)
            # 获取贴子楼层的数量
            number_lou = len(huifu)
            # 对每一个楼层进行信息提取
            for  k in range(0,number_lou):
                HTML = etree.HTML(huifu[k])
                new_text = ''
                new_img = ''
                new_a = ''
                new_video = ''
                # 提取文本内容
                text = HTML.xpath('//div[@class="d_post_content j_d_post_content  clearfix"]/text()')
                if text != []:
                    for w in range(0,len(text)):
                        new_text = new_text+text[w]+'\n'
                # 提取图片内容
                img = HTML.xpath('//div[@class="d_post_content j_d_post_content  clearfix"]/img/@src')
                if img != []:
                    for w in range(0,len(img)):
                        new_img = new_img+img[w]+'\n'
                # 提取链接内容
                a = HTML.xpath('//div[@class="d_post_content j_d_post_content  clearfix"]/a/text()')
                if a != []:
                    for w in range(0,len(a)):
                        new_a = new_a+a[w]+'\n'
                # 提取视频内容
                video = HTML.xpath('//div[@class="d_post_content j_d_post_content  clearfix"]/div/div/video/@src')
                if video != []:
                    for w in range(0,len(video)):
                        video = new_video+video[w]+'\n'
                f.write('\n第'+str(i+1)+'页贴吧第'+str(j+1)+'个贴子第'+str(k+1)+'层的回复： \n')
                f.write(new_text+new_img+new_a+new_video)
                f.write('\n')
    f.close()

if __name__ == "__main__":
    a,b = GetInfo()
    url_list = GetURL(a,b)
    html = LoadPage(url_list)
    time.sleep(2)
    all_title,all_href = GetTiezi(html)
    GetAllData(all_title,all_href)
