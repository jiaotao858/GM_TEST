#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.support.ui import Select
import time,os
import win32com.client

driver = webdriver.Chrome()
# driver.get('https://testhotel.guomintrip.com')
# try:
#     assert '首页' in driver.title
# except:
#     print('有问题')
# elem1 = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[1]/input')
# elem1.send_keys('18640857881')
# elem2 = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input')
# elem2.send_keys('jt123456')
# elem3 = driver.find_element_by_class_name('layui-btn-normal')
# # print('hhhhhh')
# elem3.send_keys(Keys.RETURN)
# time.sleep(10)
# s = driver.title
# if s == '首页':
#     print('确定是这样的吗？？？')
# else:
#     print(s)
# time.sleep(10)
# driver.close()


#跳转系统
driver.get('https://testhotel.guomintrip.com')
#最大化
driver.maximize_window()
#跳转至注册页
driver.find_element_by_xpath('/html/body/div/div[2]/form/div[4]/a').click()
driver.implicitly_wait(30)
#公司名称
driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div/div[1]/input').send_keys('中央人民广播电台')
# select = Select(driver.find_element_by_class_name('layui-input gm-select'))
#选择省份
select_p = Select(driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div/div[2]/div/div[1]/select[1]'))
# select.select_by_index(1)
# select.select_by_value('210000')
select_p.select_by_visible_text('河北省')
#选择城市
select_c = Select(driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div/div[2]/div/div[1]/select[2]'))
select_c.select_by_visible_text('唐山市')
#选择区域
select_q = Select(driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div/div[2]/div/div[1]/select[3]'))
select_q.select_by_visible_text('路南区')
#公司地址
driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div/div[2]/div/div[2]/input').send_keys('奥林匹克大道')
#营业执照
driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div/div[3]/input').send_keys('123456789876543')
#上传图片
driver.find_element_by_id('uploadImg').send_keys('C:\\Users\jiaotao\Desktop\p.jpg')
#设置管理员账号
driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div/div[5]/input').send_keys('15524638915')
#获取短信验证码
driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div/div[6]/button').click()
#选择复选框
driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div/div[15]/input').click()
print(driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div/div[15]/input').is_selected())
#提交信息
driver.find_element_by_class_name('text-center').click()
#获取对话框
# Alernt = driver.switch_to.alert
# Alernt.text()
#获取toast提示
# print(driver.switch_to.parent_frame())
print(driver.find_element_by_class_name('layui-layer-content').text)
time.sleep(10)
driver.quit()
print("测试远程更新！")

print ("测试push是否成功")

print ("测试pull上传")
#关闭chormedriver
# def check_exsit(process_name):
#     WMI = win32com.client.GetObject('winmgmts:')
#     processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
#     if len(processCodeCov) > 0:
#         print ('%s is exists' % process_name)
#         os.system('taskkill /f /im %s' %process_name)
#     else:
#         print ('%s is not exists' % process_name)
# os.system('taskkill /f /im chromedriver.exe')
# os.system('taskkill /f /im IEdriver.exe')

