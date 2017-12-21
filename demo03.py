#coding:utf-8
#查询关闭某给进程
# import win32com.client
# import os
# #关闭某个程序
# def check_exsit(process_name):
#     WMI = win32com.client.GetObject('winmgmts:')
#     processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
#     if len(processCodeCov) > 0:
#         print ('%s is exists' % process_name)
#         os.system('taskkill /f /im %s' %process_name)
#     else:
#         print ('%s is not exists' % process_name)
#
# if __name__ == '__main__':
#     check_exsit('Notepad++.exe')

#测试toast（错误登录提示等）
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import os,time
#
# driver = webdriver.Chrome()
# driver.get('https://hotel.guomintrip.com')
# #输入用户名
# driver.find_element_by_xpath('/html/body/div/div[2]/form/div[1]/input').send_keys('')
# #输入密码
# driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input').send_keys('')
# #点击登录
# driver.find_element_by_xpath('/html/body/div/div[2]/form/div[4]/div/a').click()
# driver.implicitly_wait(10)
# print(driver.find_element_by_class_name('layui-layer-content').text)
# driver.quit()

#首页查询
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# import os,time
#
# driver = webdriver.Chrome()
# driver.get('https://hotel.guomintrip.com')
# #输入用户名
# driver.find_element_by_xpath('/html/body/div/div[2]/form/div[1]/input').send_keys('18640857881')
# #输入密码
# driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input').send_keys('jt123456')
# #点击登录
# driver.find_element_by_xpath('/html/body/div/div[2]/form/div[4]/div/a').click()
# #智能等待
# driver.implicitly_wait(10)
# #清空默认目的地
# driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/form/div[1]/input').clear()
# #设置目的地
# driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/form/div[1]/input').send_keys('山东省')
# #设置出行时间
# '''
# 1.时间控件变为可编辑状态
# 2.清空默认时间
# 3.输入需要时间值
# '''
# js = "document.getElementById('checkinDate').removeAttribute('readonly')"
# driver.execute_script(js)
# driver.find_element_by_id('checkinDate').clear()
# driver.find_element_by_id('checkinDate').send_keys('2017-12-01')
# #设置离店时间
# js = "document.getElementById('checkoutDate').removeAttribute('readonly')"
# driver.execute_script(js)
# driver.find_element_by_id('checkoutDate').clear()
# driver.find_element_by_id('checkoutDate').send_keys('2017-12-05')
# #设置价格
# select_pri = Select(driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/form/div[3]/select[1]'))
# select_pri.select_by_value(',150')
# #设置星级
# select_star = Select(driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/form/div[3]/select[2]'))
# select_star.select_by_value('23')#23代表三星级
# #设置酒店名称
# driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/form/div[4]/input').send_keys('迪士尼欢乐酒店')
# #点击搜索
# driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/form/div[5]/button').click()

# 完整下单操作
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os,time

#设置图片保存路径
localday = time.strftime("%Y-%m-%d",time.localtime())
localtime = time.strftime("%Y-%m-%d %H%M%S",time.localtime())
filename = "C:\\Users\\allonshore\\Desktop\\text\\" + localday + "\\"+localtime+"\\"
if os.path.exists(filename)==False:
    os.makedirs(filename)

#初始化操作
driver = webdriver.Chrome()
driver.get('https://testhotel.guomintrip.com')
driver.execute_script("window.open('https://testadmin.guomintrip.com')")
driver.execute_script("window.open('https://testebooking.guomintrip.com')")
#切换句柄
handles = driver.window_handles
driver.switch_to.window(handles[0])
print(driver.current_url)
#最大化页面
driver.maximize_window()
#输入用户名
driver.find_element_by_xpath('/html/body/div/div[2]/form/div[1]/input').send_keys('18640857881')
#输入密码
driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input').send_keys('jt123456')
#点击登录
driver.find_element_by_xpath('/html/body/div/div[2]/form/div[4]/div/a').click()
#智能等待
driver.implicitly_wait(10)
# #设置目的地
driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/form/div[1]/input').clear()
driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/form/div[1]/input').send_keys('贵州省')
#查询酒店
driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/form/div[4]/input').send_keys('迪士尼欢乐酒店')
#点击搜索
driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/form/div[5]/button').click()
#页面滑动
time.sleep(3)
driver.execute_script("window.scrollTo(1000,1000)")
#点击预定按钮
driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[2]/div[1]/div[2]/div[11]/a').click()
#填写入住人信息
driver.implicitly_wait(30)
driver.find_element_by_xpath('/html/body/div[3]/div/form/div[3]/ul/li[1]/div/input').send_keys("正常流程a")
driver.find_element_by_xpath("/html/body/div[3]/div/form/div[3]/ul/li[2]/div/input").send_keys("18640857881")
#选择支付方式(账户支付)
driver.find_element_by_xpath("/html/body/div[3]/div/form/div[6]/div[2]/label[1]").click()
#提交订单
driver.find_element_by_xpath("/html/body/div[3]/div/form/div[6]/div[3]/button").click()
#获取订单编号
billNO = str(driver.find_element_by_xpath("/html/body/div[3]/div/form/div/div[2]/div/div[1]/div[2]").text)
billId = billNO.split("：")[1]
driver.save_screenshot(filename+"获取订单编号.png")
print(billId)

#===========切换至admin.guomintrip
driver.switch_to.window(handles[2])
print(driver.current_url)
#用户名和密码
driver.find_element_by_name("loginId").send_keys("guo")
driver.find_element_by_name("password").send_keys("gm666qwe")
driver.find_element_by_id("loginBtn").click()
# print(driver.find_element_by_class_name('layui-layer-content').text)
time.sleep(3)
driver.save_screenshot(filename+"登录成功.png")
#点击订单查询
driver.implicitly_wait(30)
driver.find_element_by_link_text("订单查询").click()
#搜索订单
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[2]/div[1]/input").send_keys(billId)
#确认订单
driver.find_element_by_link_text("查看").click()
driver.find_element_by_link_text("确认hold房").click()
#确认hold房
driver.implicitly_wait(5)
driver.find_element_by_xpath("//*[@id='layui-layer3']/div[3]/a[2]").click()
#刷新页面
time.sleep(3)
driver.refresh()
#验证状态
a_ord_sta = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/table[1]/tbody/tr[8]/td[2]/a").text
assert a_ord_sta == "取消hold房"
#截图
driver.save_screenshot(filename+"hold房成功.png")

#===========切换至hotel.guomintrip进行付款
driver.switch_to.window(handles[0])
driver.refresh()
h_ord_sta =driver.find_element_by_xpath("/html/body/div[3]/div/form/div/div[3]/div[1]/button").text
assert h_ord_sta == "确认支付"
driver.find_element_by_xpath("/html/body/div[3]/div/form/div/div[3]/div[1]/button").click()
driver.implicitly_wait(10)
h_ord_suss = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[1]").text
assert h_ord_suss == "支付成功"

#===========切换至ebooking.guomintrip
driver.switch_to.window(handles[1])
print(driver.current_url)
driver.find_element_by_xpath("//*[@id='loginId']").send_keys("15524638915")
driver.find_element_by_xpath("//*[@id='password']").send_keys("jt123456")
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/button").click()
driver.find_element_by_link_text("订单处理").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/div[2]/input").send_keys(billId)
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/div[2]/button[1]").click()
driver.find_element_by_link_text("处理").click()
driver.implicitly_wait(10)
driver.find_element_by_link_text("确认订单").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//*[@id='layui-layer100002']/div[2]/div/div/input").send_keys('1233')
driver.find_element_by_xpath("//*[@id='layui-layer100002']/div[3]/a").click()
# driver.implicitly_wait(10)
time.sleep(2)
print(driver.find_element_by_class_name('layui-layer-content').text)
time.sleep(3)
#退出
driver.quit()