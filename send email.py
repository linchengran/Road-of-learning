import yagmail
# 一般发邮件法
# yagmail.register('2946990451@qq.com','faevxyrqebhqdgfe')
# yag = yagmail.SMTP(user='2946990451@qq.com',host='smtp.qq.com')
# contents = ['Hello 外敷','下午好琦酱，这是一封邮件','通过python发送，检验一下效果']
# yag.send('3299369884@qq.com','敲代码好烦',contents)
# 定时发邮件法
import schedule
import time

from certifi import contents


def task1():
    yag = yagmail.SMTP(user='2946990451@qq.com',host='smtp.qq.com')
    contents = ['<h3>HELKO <h3>','<b>这是邮件<b>','<a herf=''https://lichess.org/learn''>国际象棋欢迎你</a>']
    # yag.send([收件人，邮件主题，正文内容])

# schedule.every(10).seconds.do(job)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
# schedule.every().minute.at(":17").do(job)

# def job_with_argument(name):
#     print(f"I am {name}")
#
# schedule.every(10).seconds.do(job_with_argument, name="Peter")

while True:
    schedule.run_pending()
    time.sleep(1)
