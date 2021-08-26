'''
集成HTML测试报告
'''


import os
import unittest
from HTMLTestRunner import HTMLTestRunner
from test_cases.unittest_for import UnitTest_Dome

#创建套件对象
suite = unittest.TestSuite()
#集成测试用例
cases = [UnitTest_Dome('test_02'),UnitTest_Dome('test_03'),UnitTest_Dome('test_07')]
#集成测试报告
report_name = '测试报告名'
report_title = '测试报告标题'
report_desc = '测试报告描述'
report_path = './report/'   #报告保存的文件夹
report_file = report_path + 'report.html'  #测试报告HTML
#判断文件路径是否存在
if not os.path.exists(report_path):
    os.mkdir(report_path)
else:
    pass
#打开文件，并重命名为report
with open(report_file,'wb') as report:
    #添加用例
    suite.addTests(cases)
    runner = HTMLTestRunner(stream=report,title=report_title,description=report_desc,tester='yangchangxu')
    runner.run(suite)
