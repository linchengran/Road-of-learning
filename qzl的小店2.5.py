print('''-------------qzl的小店---------------''')
import os
import sys
from PIL import Image
import random
from PIL import ImageDraw,ImageFilter,ImageFont
password=[]
filename='password.txt'
def get_colour():
    red = random.randint(0,256)
    green = random.randint(0,256)
    blue = random.randint(0,256)
    return red,green,blue
def get_code(length):
    s = '1234567890asdfghjklqwertyuiopzxcvbnm'
    code = ''
    for i in range(length):
        code += random.choice(s)
    return code
def draw_code():
    width=120
    height=80
    image_size = (width,height)

    image = Image.new('RGB', image_size, get_colour())
    draw = ImageDraw.Draw(image)
    code = get_code(4)
    myfont = ImageFont.truetype(font='tahoma.ttf', size=30)

    for i in range(4):
        distance_x = random.randint(30 * i, 30 * i + 5)
        distance_y = random.randint(0, 5)
        draw.text((distance_x, distance_y), code[i], font=myfont, fill=get_colour())
    for i in range(10):
        begin = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        draw.line((begin, end), fill=get_colour())
    for i in range(20):
            draw.point((random.randint(0, width), random.randint(0, height)), fill=get_colour())

    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    image.show()
    return code
def verify_code():
    """验证验证码"""
    code = input('请输入验证码: ')
    return code.lower() == code.lower()
draw_code()
def first():
    if os.path.exists(filename):
        with open(filename,'r') as f:
            for line in f.readlines():
                if ':' in line:
                    account, password_val = line.strip().split(':',1)
                    print(f'您的设备默认的账户为{account}')
                    for i in range(3):
                        password2 = (input('请输入账户的密码:'))
                        if password2==password_val:
                            code = input('请输入验证码')
                            print('登入成功')
                            return
                        elif password2!=password_val:
                            print(f'密码错误！,你还可以尝试{2-i}次')
                            if i == 2:
                                print('对不起，密码错误，您的尝试机会已用完')
                                input('请按回车键退出...')
                                sys.exit(0)
    else:
        print('您是第一次进入本店')
        account=input('为了您的账户安全，请您注册一个账户:')
        password1=input('请您输入您的新账户的密码:')
        with open(filename,'w',encoding='utf-8') as f:
            f.write(f'{account}:{password1}\n')
        print('注册成功')
first ()
type=input('请选择所需周边，1：痛衣，2：手办，3：徽章')
if type=='1':
    number1 = input('多少件痛衣,20元/件')
    number1 = int(number1)
    money1 = input('你准备了多少钱')
    money1 = float(money1)
    choice = input('请输入角色,明日方舟,赛马娘,原神,fate,崩铁，绝区零')
    way= input('请选择支付方式，WeChat/Alipay/Bankcard')
    if money1>=number1*20 and choice == ['明日方舟','赛马娘','原神','崩铁','绝区零','fate']:
        print('支付成功')
        print('哈哈,又可以穿{}的痛衣去社死啦'.format(choice))
        print(f'OK! 您现在成功购得{number1}件1号商品您的余额为:{money1 - number1 * 20}')
        input('程序执行完毕，请按回车键结束运行...')
    else:
        print('余额不足')
        print('钱不够还想买东西! 穷鬼别来我们店！')
        input('程序执行完毕，请按回车键结束运行...')
        sys.exit()
elif type=='2':
    number2 = input('多少个手办?,50元/个')
    number2 = int(number2)
    money2 = input('你准备了多少钱')
    money2 = float(money2)
    choice = input('请输入角色,明日方舟,赛马娘,原神,fate,崩铁，绝区零')
    way = input('请选择支付方式，WeChat/Alipay/Bankcard')
    if money2 >= number2 * 50 and choice == ['明日方舟','赛马娘','原神','崩铁','绝区零','fate']:
        print('支付成功')
        print('哈哈,又可以带{}的手办去欣赏啦'.format(choice))
        print(f'OK! 您现在成功购得{number2}件2号商品您的余额为:{money2 - number2 * 50}')
        input('程序执行完毕，请按回车键结束运行...')
    else:
        print('余额不足')
        print('钱不够还想买东西! 穷鬼别来我们店！')
        input('程序执行完毕，请按回车键结束运行...')
        sys.exit()
elif type=='3':
    number3 = input('多少个徽章?,25元/个')
    number3 = int(number3)
    money3 = input('你准备了多少钱')
    money3 = float(money3)
    choice = input('请输入角色,明日方舟,赛马娘,原神,fate,崩铁，绝区零')
    way = input('请选择支付方式，WeChat/Alipay/Bankcard')
    if money3 >= number3 * 25 and choice == ['明日方舟','赛马娘','原神','崩铁','绝区零','fate']:
        print('支付成功')
        print('哈哈,又可以拿{}的徽章去炫耀啦'.format(choice))
        print(f'OK! 您现在成功购得{number3}件3号商品您的余额为:{money3 - number3 * 25}')
        input('程序执行完毕，请按回车键结束运行...')
    else:
        print('余额不足')
        print('钱不够还想买东西! 穷鬼别来我们店！')
        input('程序执行完毕，请按回车键结束运行...')
        sys.exit()
else:
    print('我们没有这个款式')
    input('程序执行完毕，请按回车键结束运行...')
    sys.exit()
