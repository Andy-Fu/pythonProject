# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import time
from datetime import date

import pygame

from com.andy.testdemo1.ChildHeight import ChildHeight
from com.andy.testdemo1.LoopDemo import LoopDemo
from com.andy.testdemo1.MusicPlayer import MusicPlayer
from com.andy.testdemo1.RandomDemo import RandomDemo
from com.andy.testdemo1.TuitionCalculator import TuitionCalculator


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# 变量的定义
def testValue():
    alex_name = "刘德华"
    alex_sex = "男"
    alex_age = "61"
    print(alex_name + "\t" + alex_sex + "\t" + alex_age)

    # 快速交换两个变量
    index = 10
    pre_index = 15
    print("index:%d\t,pre_index:%d" % (index, pre_index))
    index, pre_index = pre_index, index
    print("index:%d\t,pre_index:%d" % (index, pre_index))
    # 列表基本操作
    staff_list = ["old_shang", "Alex", "智哥"]
    print(staff_list)
    staff_list[1] = "Blex"
    print(staff_list)
    staff_list.append("小芸")
    print(staff_list)
    print(staff_list[1])
    print(staff_list[-1])

    staff_list.insert(1, "刘德华")
    print(staff_list)

    information_list = ["china", "sex", "61"]
    combine_list = staff_list + information_list
    print(combine_list)
    combine_list.remove("61")
    print(combine_list)
    name_pop = combine_list.pop(2)
    print(name_pop)
    print(combine_list)

    name_orign_list = "andy,luck,jack,monick,lulu"
    name_spilt = name_orign_list.split(",")
    print(name_spilt)

    name_combine = ",".join(name_spilt)
    print(name_combine)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    a = True
    b = 10
    sb = str(b)
    s0 = "Old_shang"
    print("字符串长度：" + str(len(s0)))
    s1 = "代码之神"
    s = sb + s0 + s1
    name = "andy"
    print(s)
    print(s[0])
    print(s.lower())
    print(f"我：{name} 才是代码之神")
    print(b)
    print(str(b))
    print(12 + 20.5)

    name_list = ["andy", "mack", "luckily"]
    print(name_list)
    print(sorted(name_list))

    print("欢迎使用本系统！")
    # time.sleep(1.8)
    print("播音系统已启动")
    print("***********")
    # pygame.mixer.init()
    # pygame.mixer.music.load(r"resources/富士山下 - 陈奕迅.mp3")
    # pygame.mixer.music.play()
    # time.sleep(10)
    # pygame.mixer.music.stop()
    testValue()
    # -------------------------
    # childHeight = ChildHeight()
    # childHeight.computuHeight()
    # -------------------------
    # tuitionCalculator = TuitionCalculator()
    # tuitionCalculator.doCalculator()
    # -------------------------
    # loopDemo = LoopDemo()
    # loopDemo.forLoopTest()
    # loopDemo.whileLoop()
    # loopDemo.forLoop()
    # randomDemo = RandomDemo()
    # randomDemo.randomTest()
    # randomDemo.randomGame()
    musicPlayer = MusicPlayer()
    musicPlayer.mainRoot()


# 方法参数有位置参数和默认值及可变参数时，需要将默认值参数和可变参数放在最后
def person_info(name, gender, age):
    print(f"用户姓名：{name},用户性别：{gender}, 用户年龄：{age}")


# 返回值方法
def max_number(a, b):
    return a if a > b else b


# 默认值参数。当没有输入参数时用默认值。否则用用户输入的值
def score_report(name, score=60):
    print(f"{name}同学获得的分数为{score}")

# 可变参数。在参数名前面加个*
def deal_work(date, *work):
    print(f"可变参数长度：{len(work)}")
    for index, item in enumerate(work):
        print(f"第{index}个参数为：{item}")
    print("1、获取第一个可变参数:"+work[0])
    print(f"{date},还有以下工作需要去处理：{work}")

value = 10
name = "andy"
# 局部变量和全局变量
def test_value():
    # 方法内部要改变全局变量的值 需要在方法内部申明使用全部变量，使用global valueName来申明
    global name
    value = 20
    name = "luckly"
    print(f"方法内部value值：{value},name值：{name}")

test_value()
print(f"方法外部value值：{value},name值：{name}")

deal_work(datetime.date.today(),"a","吃饭","睡觉","学习")
score_report("andy")
score_report("andy", 78)

person_info("刘德华", "男", "61")
max = max_number(3, 2)
print(max)
