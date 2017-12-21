import unittest
from TestDemo import TestCaseDemo

def suite1():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(TestCaseDemo.MyTestCase('test_case1'))
    suiteTest.addTest(TestCaseDemo.MyTestCase('test_case4'))
    print("suit1 执行")
    return suiteTest

def suite2():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(TestCaseDemo.MyTestCase('test_case2'))
    suiteTest.addTest(TestCaseDemo.MyTestCase('test_case3'))
    print("suit2 执行")
    return suiteTest

def AllSuite():
    allTest = unittest.TextTestResult(suite1(),suite2())
    print("suite1,suit2 执行")
    return AllSuite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite2())