#coding:utf-8
#打开admin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os,time
#创建保存路径
localday = time.strftime("%Y-%m-%d",time.localtime())
localtime = time.strftime("%Y-%m-%d %H%M%S",time.localtime())
filename1 = "C:\\Users\\allonshore\\Desktop\\text\\" + localday + "\\" + localtime + "\\"
if os.path.exists(filename1) == False:
    os.makedirs(filename1)
else:
    print("文件夹已经存在")
#初始化
driver = webdriver.Chrome()
driver.get("https://testadmin.guomintrip.com")
#用户名和密码
driver.find_element_by_name("loginId").send_keys("guo")
driver.find_element_by_name("password").send_keys("gm666qwe")
driver.find_element_by_id("loginBtn").click()
# print(driver.find_element_by_class_name('layui-layer-content').text)
#点击订单查询
driver.implicitly_wait(30)
driver.find_element_by_link_text("订单查询").click()
#搜索订单
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[2]/div[1]/input").send_keys(1000189420171218)
#确认订单
driver.find_element_by_link_text("查看").click()
driver.find_element_by_link_text("确认hold房").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//*[@id='layui-layer3']/div[3]/a[2]").click()
#刷新页面
# driver.refresh()
#确认hold房
driver.save_screenshot(filename1+'确认订单.png')
print("======================")
time.sleep(5)
