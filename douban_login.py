# 本地Chrome浏览器设置方法
from selenium import webdriver #从selenium库中调用webdriver模块
import time

driver = webdriver.Chrome('/usr/local/bin/chromedriver') # 设置引擎为Chrome，真实地打开一个Chrome浏览器

driver.get('https://accounts.douban.com/passport/login?source=main') # 访问页面
time.sleep(2)  # 暂停两秒，等待浏览器缓冲

driver.find_element_by_class_name('account-tab-account').click()
time.sleep(2)
driver.find_element_by_id('username').send_keys('19924760691')
time.sleep(2)
driver.find_element_by_id('password').send_keys('wangzhedz')
time.sleep(2)
driver.find_element_by_class_name('account-form-field-submit ').click()
time.sleep(10)
driver.close()
