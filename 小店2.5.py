"""面向对象方法，测试GUI程序写法"""
import tkinter
from tkinter import *
from tkinter import messagebox
import os
import sys
from PIL import Image
import random
from PIL import ImageDraw,ImageFilter,ImageFont
password=[]
filename='password.txt'
# 全局变量存储验证码
current_code = ""
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
    global current_code
    width=120
    height=80
    image_size = (width,height)

    image = Image.new('RGB', image_size, get_colour())
    draw = ImageDraw.Draw(image)
    code = get_code(4)
    current_code = code  # 保存验证码到全局变量
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
def verify_code(input_code):
    """验证验证码"""
    return input_code.lower() == current_code.lower()
draw_code()
def buy():
    # 角色选项映射
    roles = {
        '1': '明日方舟',
        '2': '赛马娘',
        '3': '原神',
        '4': 'fate',
        '5': '崩铁',
        '6': '绝区零',
        '7': '千恋万花'
    }
    
    type=input('请选择所需周边，1：痛衣，2：手办，3：徽章')
    if type=='1':
        number1 = input('多少件痛衣,20元/件')
        number1 = int(number1)
        money1 = input('你准备了多少钱')
        money1 = float(money1)
        print('请选择角色：1-明日方舟, 2-赛马娘, 3-原神, 4-fate, 5-崩铁, 6-绝区零, 7-千恋万花')
        choice_num = input('请输入角色编号(1-7): ')
        choice = roles.get(choice_num)
        way= input('请选择支付方式，WeChat/Alipay/Bankcard')
        valid_choice=['明日方舟','赛马娘','原神','崩铁','绝区零','fate','千恋万花']
        if money1>=number1*20 and choice in valid_choice:
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
        print('请选择角色：1-明日方舟, 2-赛马娘, 3-原神, 4-fate, 5-崩铁, 6-绝区零, 7-千恋万花')
        choice_num = input('请输入角色编号(1-7): ')
        choice = roles.get(choice_num)
        way = input('请选择支付方式，WeChat/Alipay/Bankcard')
        valid_choice = ['明日方舟', '赛马娘', '原神', '崩铁', '绝区零', 'fate', '千恋万花']
        if money2 >= number2 * 50 and choice in valid_choice:
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
        print('请选择角色：1-明日方舟, 2-赛马娘, 3-原神, 4-fate, 5-崩铁, 6-绝区零, 7-千恋万花')
        choice_num = input('请输入角色编号(1-7): ')
        choice = roles.get(choice_num)
        way = input('请选择支付方式，WeChat/Alipay/Bankcard')
        valid_choice = ['明日方舟', '赛马娘', '原神', '崩铁', '绝区零', 'fate', '千恋万花']
        if money3 >= number3 * 25 and choice in valid_choice:
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

class Application(Frame):
    """一个经典的GUI程序的类写法"""
    def __init__(self,master=None):
        # super()代表父类的定义，不是父类对象
        super().__init__(master)
        self.entry01 = None
        self.master = master
        self.pack()
        self.creatWidget()
        self.creatWidget2()
    def creatWidget(self):
        self.lable01 = Label(self,text="小邱的程序",width=15,height=5,bg="blue",fg="white")
        self.lable01.pack()
        self.lable02 = Label(self,text="欢迎",width=15,height=5,bg="white",fg="pink",font=("宋体",15))
        self.lable02.pack()
    # 创建图像
        global photo
        photo = PhotoImage(file="qzl_shop_logo.gif")
        self.lable03 = Label(self,image=photo)
        self.lable03.pack()
    def creatWidget2(self):
        self.lable04 = Label(self, text="用户名")
        self.lable04.pack()
        # StringVar变量绑定到指定组件
        #  StringVar变量值发生变化，组件发生变化。反之同理
        v1 = StringVar()
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.pack()

        self.lable05 = Label(self, text="密码")
        self.lable05.pack()
        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2)
        self.entry02.pack()

        self.lable06 = Label(self, text="验证码")
        self.lable06.pack()
        v3 = StringVar()
        self.entry06 = Entry(self, textvariable=v3)
        self.entry06.pack()
        self.btn_code = Button(self, text="生成验证码", command=draw_code)
        self.btn_code.pack()
        self.btn01 = Button(self, text="登录", command=self.login)
        self.btn01.pack()

    def login(self):
        account = self.entry01.get()
        input_code = self.entry06.get()
        password = self.entry02.get()
        print("用户名：" + account)
        print("密码：" + password)
        print('验证码：' + input_code)
        if not verify_code(input_code):
            messagebox.showerror("小邱购买系统", "验证码错误！")
            return
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                lines = f.readlines()
                found = False
                for line in lines:
                    if ':' in line:
                        stored_account, stored_password = line.strip().split(':', 1)
                        if account == stored_account:
                            found = True
                            if password == stored_password:
                                messagebox.showinfo("小邱购买系统", "登录成功！欢迎光临")
                                self.start_buy()
                                return
                            else:
                                messagebox.showerror("小邱购买系统", "密码错误！")
                                return
                if not found:
                    messagebox.showerror("小邱购买系统", "账户不存在！")
        else:
            # 第一次使用，自动注册
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f'{account}:{password}\n')
            messagebox.showinfo("小邱购买系统", "注册成功！欢迎光临")
            self.start_buy()

    def start_buy(self):
        buy()
if __name__ == '__main__':
    root = tkinter.Tk()
    root.geometry("1000x800+200+200")
    root.title("用户界面")
    app = Application(master=root)
    app.mainloop()
