
'''
password 
如果沒有設定 兩步驟驗證機制 那就只是一般登入信箱的密碼

如果有設定 兩步驟驗證機制 那就要去申請
詳情請參考 https://www.learncodewithmike.com/2020/02/python-email.html

兩種方式皆可成功

'''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


content = MIMEMultipart()  #建立MIMEMultipart物件
content["subject"] = "Test send email"  #郵件標題
content["from"] = "xxxx@gmail.com"  #寄件者
content["to"] = "qqqq@gmail.com" #收件者
content.attach(MIMEText("Demo python send email"))  #郵件內容




with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
    try:
        smtp.ehlo()  # 驗證SMTP伺服器
        smtp.starttls()  # 建立加密傳輸
        smtp.login("xxxx@gmail.com", "password")  # 登入寄件者gmail 
        smtp.send_message(content)  # 寄送郵件
        print("Complete!")
    except Exception as e:
        print("Error message: ", e)
        
#-----------------------------------------------------

from email.mime.text import MIMEText
from smtplib import SMTP,SMTPAuthenticationError,SMTPException


smtp="smtp.gmail.com:587"
account='xxxx@gmail.com' #寄件者
password='password'
item=MIMEText("Demo python send email") #郵件內容


item['Subject']='Test send email'  #郵件標題
mailto='qqqq@gmail.com' #收件者

server=SMTP(smtp)
server.ehlo()
server.starttls()


try:
    server.login(account,password)
    server.sendmail(account,mailto,item.as_string())
    sendmsg='郵件已寄出'
except SMTPAuthenticationError:
    sendmsg='無法登入GOOGLEMAIL'
except:
    sendmsg='郵件發生錯誤'
server.quit()


        
