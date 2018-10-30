# encoding=utf-8
import unittest
import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib
import time
import os

def _format_addr(s):
    name, addr = parseaddr (s)
    return formataddr (( \
    Header (name, 'utf-8').encode (), \
    addr.encode ('utf-8') if isinstance (addr, bytes) else addr))
## ==============定义发送附件邮件==========
def send_file(file_new):
        reportname = os.path.split(file_new)[1]
        smtpserver = '#'
        user = '#'
        password = '*'
        sender = '*'
        receiver = ['#']
        # subject='**自动化测试报告'
        file = open (file_new, 'rb').read()#将r改为rb，解决发邮件报乱码问题

        now = time.strftime ("%Y-%m-%d %H_%M_%S")
        subject = '移动端自动化测试报告--' + now
        # att=MIMEText(sendfile,"base64","utf-8")
        att = MIMEText (file, "html", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["ContenT-Disposition"] = "attachment;filename ="+reportname

        msgRoot = MIMEMultipart ('related')
        msgRoot['Subject'] = subject
        msgRoot['From'] = _format_addr (u'**测试组 <%s>' % sender)
        msgRoot['To'] = _format_addr (u'UC项目组 <%s>' % receiver)
        # msgRoot.attach(att)
        msgRoot.attach (att)

        smtp = smtplib.SMTP ()
        smtp.connect (smtpserver)
        smtp.starttls()
        smtp.login (user, password)
        smtp.sendmail(sender, receiver, msgRoot.as_string ())
        smtp.quit()



# ======查找测试目录，找到最新生成的测试报告文件======
def new_report(test_report):
    lists = os.listdir (test_report)  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))  # 按时间排序 win
    # lists.sort (key=lambda fn: os.path.getmtime (test_report + "/" + fn))  # linux
    file_new = os.path.join (test_report, lists[-1])  # 获取最新的文件保存到file_new
    print(file_new)
    return file_new

# if __name__ == "__main__":
#     # send_file(r'F:\script\UC_1.0_Android\UC_Android\Report\2018-09-30 15-14-39.html')
#     send_file('F:\\2018-09-30 16-06-25.html')
    # send_file(r'F:\script\UC_1.0_Android\UC_Android\Report\20180930151439.html')
