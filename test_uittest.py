import unittest
class Demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setupClass")



    def setUp(self) -> None:
        print("setup method")

    def tearDown(self) -> None:
        print("tearDown method")

    def test_case01(self):
        print("testcase01")
        self.assertEqual(2, 2, "check equal")

    @unittest.skipIf(1+1==2, "skip case02")
    def test_case02(self):
        print("testcase02")
        self.assertEqual(1, 1, "check equal")

    def test_case03(self):
        print("testcase03")
        self.assertIn("h", "this")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

class Demo1(unittest.TestCase):
    def demo1_test_case01(self):
        print("demo1_testcase01")
        self.assertEqual(2, 2, "check equal")

    def demo1_test_case02(self):
        print("demo1_testcase02")
        self.assertEqual(2, 2, "check equal")


if __name__ == '__main__':
    #执行方法一：执行.py文件里所有方法
    #unittest.main()
    #执行方法二：选择类里面的某个方法执行
    # suite = unittest.TestSuite()
    # suite.addTest(Demo("test_case01"))
    # suite.addTest(Demo1("demo1_test_case01"))
    # unittest.TextTestRunner().run(suite)
    #执行方法三：选择.py文件中的某个类来执行
    # suite = unittest.TestLoader().loadTestsFromTestCase(Demo)
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(Demo1)
    # suiteall = unittest.TestSuite([suite, suite1])
    # unittest.TextTestRunner().run(suiteall)
    #第四中执行方式：执行某个目录下的.py文件
    discover = unittest.defaultTestLoader.discover("./", 'test_*.py')
    unittest.TextTestRunner().run(discover)
