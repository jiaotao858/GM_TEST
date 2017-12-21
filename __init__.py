import unittest
from demo02 import TestCaseDemo

def suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(TestCaseDemo.MyTestCase('test_case1'))
    suiteTest.addTest(TestCaseDemo.MyTestCase('test_case4'))
    return suiteTest

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())