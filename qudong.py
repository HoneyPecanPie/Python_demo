'''from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# 添加无界面参数
browser = webdriver.Chrome('/usr/local/bin/chromedriver')

time.sleep(3)
browser.get('http://www.baidu.com')
browser.find_element_by_id("kw").send_keys("长城")
browser.find_element_by_id("su").click()
time.sleep(1)
browser.close()'''

'''from selenium import webdriver #从selenium库中调用webdriver模块
import time
# 添加无界面参数'''
'''options.add_argument('--headless')
options.add_argument('--no-sandbox')'''
'''driver = webdriver.Chrome('/usr/local/bin/chromedriver') # 设置引擎为Chrome，真实地打开一个Chrome浏览器

driver.get('https://www.baidu.com') # 打开网页
time.sleep(1)

element = driver.find_element_by_link_text('新闻') # 解析网页并提取name属性值为‘tj_trnews’标签下的内容。
print(type(element)) # 打印element的数据类型
print(element.text) # 打印element的文本
print(element) # 打印element
driver.close() # 关闭浏览器'''

'''from selenium import webdriver #从selenium库中调用webdriver模块
import time

driver = webdriver.Chrome('/usr/local/bin/chromedriver') # 设置引擎为Chrome，真实地打开一个Chrome浏览器

driver.get('https://www.baidu.com') # 打开网页
time.sleep(2) # 等待两秒，等浏览器加缓冲载数据

pageSource = driver.page_source # 获取完整渲染的网页源代码
print(type(pageSource)) # 打印pageSource的类型
print(pageSource) # 打印pageSource
driver.close() # 关闭浏览器'''

from selenium import webdriver #从selenium库中调用webdriver模块
from bs4 import BeautifulSoup
import time


driver = webdriver.Chrome('/usr/local/bin/chromedriver') # 设置引擎为Chrome，真实地打开一个Chrome浏览器

driver.get('https://www.baidu.com') # 打开网页
time.sleep(2) # 等待两秒，等浏览器缓冲加载数据

pageSource = driver.page_source # 获取完整渲染的网页源代码
driver.close() # 关闭浏览器

soup = BeautifulSoup(pageSource,'html.parser')
print(soup)
print(type(soup))

