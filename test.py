import unittest
from demo02 import PythonOrgSearch

def suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(PythonOrgSearch('test_register'))
    suiteTest.addTest(PythonOrgSearch('test_login'))
    return suiteTest

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())