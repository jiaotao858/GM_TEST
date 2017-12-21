#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os,time

#创建保存路径
localday = time.strftime("%Y-%m-%d",time.localtime())
localtime = time.strftime("%Y%m%d%H%M%S",time.localtime())
filename = "C:\\Users\\allonshore\\Desktop\\text\\" + localday + "\\"

if os.path.exists(filename) == False:
    os.makedirs(filename)
    print("创建目录成功！")
# else:
#     print("文件夹已经存在！")

    # filename = filename1+"hello.txt"
    # dir = open(filename,'w+')
    # dir.write("11111")
    # dir.close()

def jietu():
    driver = webdriver.Chrome()
    driver.get("https://testhotel.guomintrip.com")
    driver.maximize_window()
    driver.get_screenshot_as_file(filename+"登录页面.png")

if __name__ == '__main__':
    # wenjian()
    jietu()
#

# localday = time.strftime("%Y-%m-%d",time.localtime())
# localtime = time.strftime("%Y-%m-%d %H%M%S",time.localtime())
# filename1 = "C:\\Users\\jiaotao\\Desktop\\text\\"+localday+"\\"+ localtime+"\\"
#
# if os.path.exists(filename1) == False:
#     os.makedirs(filename1)
# else:
#     print("文件夹已经存在")
#
# filename = filename1+"hello.txt"
# dir = open(filename,'ab')
# dir.write('xxxxxx'.encode('utf-8'))
# dir.close()

