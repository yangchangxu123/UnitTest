import unittest

from ddt import ddt, file_data
from selenium import webdriver


@ddt
class UnitTest_Dome(unittest.TestCase):

    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass

    @file_data('../data/data.yaml')
    def test_01(self,**data):
        print(data.get('data'))
        # name = kwargs.get('name')
        self.driver = webdriver.Chrome()
        # if name == "123456":
        #     print('successful!')
        # else:
        #     print('false')

        # self.assertEqual(123456,name,msg="我是msg")
        self.driver.quit()

    def test_02(self):
        print('02')

    def test_03(self):
        print('0003')
    # @unittest.skip("无条件跳过")
    # def test_02(self):
    #     print('2')
    @unittest.skipUnless(1>2,'unless条件跳过')
    def test_04(self):
        print('3')

    # def test_04(self):
    #     print('4')
    # @unittest.skipIf(1>2,'if条件跳过')
    # def test_05(self):
    #     print('5')
    # @unittest.expectedFailure
    # def test_06(self):
    #     print('6')
    #     self.assertEqual(123,456,msg='not equal')

    def test_07(self):
        self.assertEqual(1111,2222,msg='这是一个断言')

if __name__ == '__main__':
    unittest.main()
