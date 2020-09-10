import requests
import re
import time

def GetURL(i):
    # i 参数代表第 i 页。
    a = 'https://www.neihan8s.com/article/list_5_'
    b = '.html'
    c = str(i)
    # 利用字符串的拼接返回第 i 页的URL地址
    return(a+c+b)

def LoadPage(url):
    # 参数url 为某一页的URL链接地址
    # 构造请求头headers
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    # 发起客户端GET请求，接收服务端响应。
    response = requests.get(url,headers=headers)
    html = response.content.decode('gbk')
    return html

def Extract(html):
    # 参数html为爬取到的内涵段子HTML文档
    # 跨行匹配，最小内容匹配
    pattern = re.compile('<div class="f18 mb20">(.*?)</div>',re.S)
    # 注意哦，result是列表类型数据
    result = pattern.findall(html)
    return result

if __name__ == "__main__":
    # 保存段子内容的文件
    f = open('result_duanzi.html','w+')
    # 爬取5页的段子
    for i in range(0,5):
        # 获取每一页的 url 地址
        url = GetURL(i+1)
        print(url)
        # 爬取每一页的HTML文档
        html = LoadPage(url)
        # 对HTML文档进行正则表达式匹配，提取出段子内容。
        result = Extract(html)
        # 记录每一页段子的个数
        num = len(result)
        # 把每一个段子都写进文件
        for j in range(0,num):
            # 标注第几页第几个段子，用换行符<br>把每个段子尽量隔开
            f.write('<br>第'+str(i+1)+'页，第'+str(j+1)+'个段子:<br><br><br>')
            f.write(result[j])
        print('第'+str(i+1)+'页段子下载完成')
        time.sleep(5)
    f.close()
