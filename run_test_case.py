#coding:utf-8
import unittest
import os,time,xdrlib
import HTMLTestRunner
import configparser,xlrd
#from Send_email import  main2
# from Test_case.DialPlate import AudioCallCase
# from Test_case.IMChat import IM_AudioCall
#待执行用例的目录
def allcase():
    # conf = ConfigParser.SafeConfigParser ()
    # conf.read ("config\\config.ini")
    case_dir=r'F:\script\UC_1.0_Android\UC_Android\Test_case\DialPlate'
    # case_path=os.path.join(os.getcwd(),"case")
    testcase = unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(case_dir,pattern='*.py',top_level_dir=None)
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
# def get_case_from_Excel():
#     print('get_case_from_Excel')
#     # test_case =
#     runner = unittest.TextTestRunner()
#     case_dir=r'F:\script\UC-1.0_android\DialPlate'
#     case_dir2=r'F:\script\UC-1.0_android\DialPlate'
#     discover=unittest.defaultTestLoader.discover(case_dir,pattern='VideoCallCase.py',top_level_dir=None)
#     discover2=unittest.defaultTestLoader.discover(case_dir2,pattern='AudioCallCase.py',top_level_dir=None)
#     discover_arr = [discover,discover2]
#     # runner.run(unittest.suite.TestSuite tests=[unittest.suite.TestSuite tests=[circleStart.VideoCallCase testMethod=test_4wait]])
#
#     print(discover2)
#     print(discover_arr)
#     # runner = unittest.TextTestRunner()
#     # for discover in discover_arr:
#     #     runner.run(discover)
def get_case():
    xlsfile = r"F:\script\UC_1.0_Android\UC_Android\config\testcase.xls"
    case_dir = "F:\\script\\UC_1.0_Android\\UC_Android\\Test_case"
    book = xlrd.open_workbook(xlsfile)
    sheet0 = book.sheet_by_index(0)
    nrows = sheet0.nrows
    discover_arr=[]
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner()
    # print(nrows)
    for i in range(1, nrows):
        is_run = sheet0.cell_value(i, 3)
        # print(is_run)
        if is_run == 'Y':
            discover = unittest.defaultTestLoader.discover(case_dir+'\\'+sheet0.cell_value(i,1),pattern=sheet0.cell_value(i,2),top_level_dir=case_dir)
            # continue
            discover_arr.append(discover)
    for test_suite in discover_arr:
        for test_case in test_suite:
            suite.addTest(test_case)
    # suite = unittest.TestSuite()
    # # arr['AudioCallCase'] = AudioCallCase.AudioCallCase
    # case_dir = r'F:\script\UC-1.0_android'
    # module = 'DialPlate'
    # # module2 = 'IMChat'
    # discover_arr = []
    # discover=unittest.defaultTestLoader.discover(case_dir+'\\'+module,pattern='*.py',top_level_dir=case_dir)
    # discover_arr.append(discover)
    # for discover in discover_arr:
    #     for test_suite in discover:
    #         for test_case in test_suite:
    #             suite.addTest(test_case)
    #
    # # if AudioCallCase==Y
    # #     suite.addTest(AudioCallCase.AudioCallCase("test_1call_num"))
    # str = IM_AudioCall.AudioCall('test_audiocall')
    # print(type(str))
    # suite.addTest(str)
    # # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="自动化测试unittest测试框架报告", description="用例执行情况：")
    # runner = unittest.TextTestRunner()
    runner.run(suite)
if __name__=="__main__":
    get_case()
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
    ##################################################
    # runner = unittest.TextTestRunner()
    # # runner.run(allcase())
    # report_path = r'E:\testresult.html'
    # fp = open(report_path,"wb")
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="自动化测试unittest测试框架报告",description="用例执行情况：")
    # runner.run(allcase())
    # fp.close()
    # print(time.ctime())