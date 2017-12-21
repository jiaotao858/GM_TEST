import unittest


class MyTestCase(unittest.TestCase):
    def setup(self):
        print("Case Before")
        pass

    def tearDown(self):
        print("Case After")
        pass

    def test_caseQ(self):
        a = 3
        self.assertEqual(a,4,"Restult Fail")

    def test_caseW(self):
        b = 3
        self.assertEqual(b,3,"Restult Fail")

def suite():
    suitTest = unittest.TestSuite()
    # suitTest.addTest(MyTestCase,'test_case1')
    suitTest.addTest(MyTestCase('test_case2'))
    return suitTest



if __name__ == '__main__':
    unittest.main(defaultTest='suite')
