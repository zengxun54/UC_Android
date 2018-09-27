#coding:utf-8
import unittest
import os,time,xdrlib
import HTMLTestRunner
import configparser
#from Send_email import  main2
#待执行用例的目录
def allcase():
    # conf = ConfigParser.SafeConfigParser ()
    # conf.read ("config\\config.ini")
    case_dir=r'F:\script\UC_1.0_Android\UC_Android\Test_case\DialPlate'
    # case_path=os.path.join(os.getcwd(),"case")
    testcase = unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(case_dir,pattern='VideoCallCase.py',top_level_dir=None)
    # discover=unittest.defaultTestLoader.discover(case_dir,pattern='circleStart.py',top_level_dir=None)
    #discover方法筛选出来的用例，循环添加到测试套件中
    # print(discover)
    for test_suite in discover:
        for test_case in test_suite:
            #添加用例到testcase
            testcase.addTest(test_case)
    return testcase
    # print(testcase)
# # def circleRun():
# def circleRun():
#     n=1
#     while n<550:
#         runner = unittest.TextTestRunner()
#         runner.run(allcase())
#         # report_path = r'E:\testresult.html'
#         # fp = open(report_path,"wb")
#         # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="自动化测试unittest测试框架报告",description="用例执行情况：")
#         # runner.run(allcase())
#         # fp.close()
#         print(time.ctime())
#         print(n)
#         n+=1
def get_case_from_Excel():
    print('get_case_from_Excel')
    # test_case =
    runner = unittest.TextTestRunner()
    case_dir=r'F:\script\UC-1.0_android\DialPlate'
    case_dir2=r'F:\script\UC-1.0_android\DialPlate'
    discover=unittest.defaultTestLoader.discover(case_dir,pattern='VideoCallCase.py',top_level_dir=None)
    discover2=unittest.defaultTestLoader.discover(case_dir2,pattern='AudioCallCase.py',top_level_dir=None)
    discover_arr = [discover,discover2]
    # runner.run(unittest.suite.TestSuite tests=[unittest.suite.TestSuite tests=[circleStart.VideoCallCase testMethod=test_4wait]])

    print(discover2)
    print(discover_arr)
    # runner = unittest.TextTestRunner()
    # for discover in discover_arr:
    #     runner.run(discover)

if __name__=="__main__":
    # get_case_from_Excel()
    # # runner = unittest.TextTestRunner()
    # # # runner.run(allcase())
    # # report_path = r'E:\testresult.html'
    # # fp = open(report_path,"wb")
    # # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="自动化测试unittest测试框架报告",description="用例执行情况：")
    # # runner.run(allcase())
    # # fp.close()
    # circleRun()
    # #main2()  #from send_email import main2  发送邮件！
    runner = unittest.TextTestRunner()
    runner.run(allcase())
    report_path = r'E:\testresult.html'
    fp = open(report_path,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="自动化测试unittest测试框架报告",description="用例执行情况：")
    # runner.run(allcase())
    fp.close()
    print(time.ctime())