import unittest,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from setting import *

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        '''测试登录是否成功'''
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        # self.assertIn('登录',driver.title)
        elem1 = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[1]/input')
        elem1.send_keys('18640857882')
        elem2 = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input')
        elem2.send_keys('jt123456')
        elem3 = driver.find_element_by_class_name('layui-btn-normal')
        elem3.send_keys(Keys.RETURN)
        time.sleep(3)
        self.assertEqual(driver.title,"登录","标题错误")
        # time.sleep(10)
        # print('结束任务')

    def test_register(self):
        '''测试注册是否成功'''
        driver = self.driver
        driver.get('https://testhotel.guomintrip.com')
        driver.find_elements_by_link_text('免费注册')
        driver.implicitly_wait(30)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div/div[1]/input').send_keys('中央人民广播电台')
        select = Select(driver.find_element_by_class_name('layui-input gm-select'))
        select.select_by_value('北京')
        time.sleep(5)
        self.assertEqual(driver.title, "注册", "标题错误")




    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(PythonOrgSearch('test_register'))
    # suite.addTest(PythonOrgSearch('test_login'))
    runner = unittest.TextTestRunner()
    runner.run(suite)