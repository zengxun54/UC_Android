#coding:utf-8
import unittest
import os,time,xdrlib
import HTMLTestRunner
import configparser,xlrd
from Public import commonClass
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
    discover=unittest.defaultTestLoader.discover(case_dir,pattern='callBackCase.py',top_level_dir=None)
    # discover=unittest.defaultTestLoader.discover(case_dir,pattern='circleStart.py',top_level_dir=None)
    #discover方法筛选出来的用例，循环添加到测试套件中
    # print(discover)
    for test_suite in discover:
        for test_case in test_suite:
            #添加用例到testcase
            testcase.addTest(test_case)
    return testcase
    # print(testcase)
def circleCase():
    n=1
    testcase = unittest.TestSuite()
    case_dir=r'F:\script\UC_1.0_Android\UC_Android\Test_case\DialPlate'
    discover=unittest.defaultTestLoader.discover(case_dir,pattern='callBackCase.py',top_level_dir=None)
    # while n < 3:
    #discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            #添加用例到testcase
            while n < 3:
                print(n)
                testcase.addTest(test_case)
                n += 1
            # print(test_case)
    return testcase
    # print(testcase)
def circleRun():
    n=0
    commonCls = commonClass.commonCase(commonClass.debug_id_pre)
    while n<300:
        # commonCls.restart_adb()
        runner = unittest.TextTestRunner()
        # runner.run(allcase())
        # report_path = r'E:\testresult.html'
        # fp = open(report_path,"wb")
        # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="自动化测试unittest测试框架报告",description="用例执行情况：")
        runner.run(allcase())
        # fp.close()
        print(time.ctime())
        print(n)
        n+=1
        time.sleep(3)
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
    report_name = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    report_path = "F:\\script\\UC_1.0_Android\\UC_Android\\log\\"+report_name+'.html'
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
    fp = open(report_path,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="自动化测试unittest测试框架报告", description="用例执行情况：")
    # runner = unittest.TextTestRunner()
    runner.run(suite)
def test1():
    print('1')
def test2():
    print('2')

def packup_log():
    commonCls = commonClass.commonCase(commonClass.debug_id_pre)
    commonCls.packup_log()
if __name__=="__main__":
    # packup_log()
    # test1()
    # test2()
    get_case()
    circleRun()
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