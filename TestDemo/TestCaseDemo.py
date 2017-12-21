import unittest


class MyTestCase(unittest.TestCase):
    def setup(self):
        print("Case Before")
        pass

    def tearDown(self):
        print("Case After")
        pass

    def test_case1(self):
        a = 3
        self.assertEqual(a,4,"Restult Fail")

    def test_case2(self):
        b = 3
        self.assertEqual(b,3,"Restult Fail")

    def test_case3(self):
        print("test_case3")

    def test_case4(self):
        print("test_case4")