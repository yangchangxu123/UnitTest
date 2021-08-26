import unittest
from test_cases.unitTest_demo import UnitTest_Dome
import os
from HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()

#第一种添加用例方法
# suite.addTest(UnitTest_Dome('test_02'))
# suite.addTest(UnitTest_Dome('test_03'))
# suite.addTest(UnitTest_Dome('test_07'))

#第二种添加方法
cases = [UnitTest_Dome('test_02'),UnitTest_Dome('test_03')]
#suite.addTests(cases)

#第三种添加方法:读取相关路径下的所有测试用例，从文件名读取
# test_dir = '../'
# discover = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='unit*')

#第四种方法，添加测试用例,从类名读取
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(UnitTest_Dome))

#第五种方法，添加测试用例,从模块名读取
# suite.addTests(unittest.TestLoader().loadTestsFromName('unitTest_demo.UnitTest_Dome'))

#运行套件
# runner = unittest.TextTestRunner()
# runner.run(suite)

#集成测试报告
report_name = '测试报告名称'
report_title = '测试报告标题'
report_desc = '测试报告描述'
report_path = './report/'    #b保存路径
report_file = report_path + 'report.html'   #文件：./report/report.html

#判断文件夹是否存在
if not os.path.exists(report_path):
    os.mkdir(report_path)
else:
    pass

with open(report_file,'wb') as report:
    suite.addTests(cases)
    runner = HTMLTestRunner(stream=report,title=report_title,description=report_desc,tester='杨昌旭')
    runner.run(cases)