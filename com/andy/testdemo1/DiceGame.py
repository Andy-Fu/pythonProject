# 掷骰子游戏，随机生成点数
# 判断点数是大还是小（3-10是小，11-18是大）

# 用户开始玩游戏：
# 如果猜对了，赢钱；猜错，输钱；
# 输完了，游戏结束
import random
import sys
import tkinter

button:tkinter.Button
input:tkinter.Entry
stake:tkinter.Entry
deposit:tkinter.Entry
balanceVar:tkinter.StringVar
inputvar :tkinter.StringVar
stakeVar :tkinter.StringVar
depositVar :tkinter.StringVar
dictList = ["大","小"]
totleMoney = 1000
def judgeLess(sum):
    if 10 >= sum >= 3 :
        return True
    elif 18>= sum >= 11:
        return False
    else:
        return None

def gameStart(suspect):
    sum = 0
    print(random.randint(1, 6))
    dices = []
    for i in range(3):
        dice = random.randint(1, 6)
        print(f"index and dice value:{i},{dice}")
        dices.append(dice)
        sum += dice
    result = judgeLess(sum)
    if result == None :
        print("程序出错！请稍后再试！")
        sys.exit("程序结束！")
    if  suspect == result :
        return True
    else:
        return False


def getInputValue():
    print("getInputValue")
    global input,inputvar

    inputValue = input.get()
    if inputValue in dictList:
        return True
    else:
        input.delete(0,"end")
        return False

def getStakeValue():
    print("getStakeValue")
    global stake,stakeVar
    stakeValue = stake.get()
    try:
        stakeValue = int(stakeValue)
        return True
    except Exception as e:
        print("输入有误！")
        stake.delete(0, "end")
        return False

def getDepositValue():
    print("getDepositValue")
    global deposit,depositVar,totleMoney,balanceVar
    depositValue = deposit.get()
    try:
        depositValue = int(depositValue)
        totleMoney+=depositValue
        print(f"充值成功，账户余额：{totleMoney}")
        balanceVar.set("账户余额："+str(totleMoney))
        deposit.delete(0, "end")
        return True
    except Exception as e:
        print("输入有误！")
        deposit.delete(0, "end")
        return False

def clickStart():
    global input,stake,totleMoney,button,balanceVar
    inputValue = input.get()
    stakeValue = stake.get()
    button.focus_force()
    if inputValue == '' or stakeValue == '':
        print("请输入！")
        return
    stakeValue = int(stakeValue)
    # 总金小于赌注 直接返回
    if totleMoney < stakeValue :
        print(f"余额不足暂时不能玩，账户余额{totleMoney}")
        return
    result = gameStart(inputValue=="小")
    if result :
        totleMoney += stakeValue
        print(f"恭喜你！账户余额{totleMoney}")
    else:
        totleMoney -= stakeValue
        print(f"很抱歉！{totleMoney}")
    balanceVar.set("账户余额：" + str(totleMoney))





def mainView():
    global input,stake,deposit,depositVar,inputvar,stakeVar,button,totleMoney,balanceVar
    window = tkinter.Tk()
    window.geometry("600x300")
    inputvar = tkinter.StringVar()
    stakeVar = tkinter.StringVar()
    depositVar = tkinter.StringVar()
    balanceVar = tkinter.StringVar()
    balanceVar.set("账户余额："+ str(totleMoney))
    welcom = tkinter.Label(window,text="欢迎来到老虎机",width=20,height=5,font="黑体 18 bold",anchor="w")
    balance = tkinter.Label(window,textvariable=balanceVar,width=20,height=5,font="黑体 12 bold",anchor="e")
    lable = tkinter.Label(window,text="请猜大小(大/小)：",width=20)
    input = tkinter.Entry(window,textvariable=inputvar,validate="focusout",width=20,  validatecommand=getInputValue)
    lable1 = tkinter.Label(window, text="请输入赌注大小(正整数)：",width=20)
    stake = tkinter.Entry(window,textvariable=stakeVar,validate="focusout",width=20, validatecommand = getStakeValue)
    lable2 = tkinter.Label(window, text="请输入充值金额：",width=20)
    deposit = tkinter.Entry(window,textvariable=depositVar,validate="focusout",width=20, validatecommand = getDepositValue)
    button = tkinter.Button(window, text="开始游戏",width=40,background="pink",command=clickStart)
    input.delete(0,"end")
    welcom.grid(column=0,columnspan=2,row=0,ipadx=0)
    balance.grid(column=1,columnspan=2,row=0,ipadx=0)
    lable.grid(column=0,row=1)
    input.grid(column=1,row=1)
    lable1.grid(column=2, row=1)
    stake.grid(column=3,row=1)
    lable2.grid(column=0,row=2)
    deposit.grid(column=1,row=2)
    button.grid(column=2,columnspan=2,row=2)
    window.mainloop()

def mainRoot():
    print("******欢迎来玩老虎机********")
    mainView()


if __name__ == '__main__':
    mainRoot()