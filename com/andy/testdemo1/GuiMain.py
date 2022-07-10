import random
import sched
import sys
import time
import tkinter as tk
import threading

import pyautogui

clickState = False


def clickMe():
    global clickState
    print(clickState)
    if clickState:
        clickState = False
        strVar.set("@@@@@@")
    else:
        clickState = True
        strVar.set("7777777")

def mianView():
    global strVar
    window = tk.Tk()
    window.title("MyMusic")
    window.geometry("500x300")
    strVar = tk.StringVar()
    strVar.set("hello world！")
    lab = tk.Label(window, textvariable=strVar, bg="Green", font=("黑体", 12), width=30, height=2)
    lab.pack()


    btn = tk.Button(window, text="点击", command=clickMe)
    btn.pack()
    window.mainloop()

isRuning = False
timer:threading.Timer
def fun_timer():
    global isRuning,timer
    if not isRuning :
        return
    print('Hello Timer!')
    positionX,positionY = pyautogui.position()
    size = pyautogui.size()
    pyautogui.moveTo(random.randint(0, size.width),random.randint(0, size.height))
    print(f"{positionX},{positionY}")
    timer = threading.Timer(5, fun_timer)
    timer.start()

def clickStart():
    global isRuning,timer
    isRuning = True
    timer = threading.Timer(1, fun_timer)
    timer.start()
    print(f"clickStart{isRuning}")

def clickPause():
    global isRuning,timer
    isRuning = bool(1 - isRuning)
    timer.cancel()
    print(f"clickPause{isRuning}")

def clickStop():
    global isRuning
    global timer
    isRuning = False
    timer.cancel()
    print(f"clickStop{isRuning}")
window: tk.Tk
def close_window():
    global window,timer
    window.destroy()
    timer.cancel()
    sys.exit("程序结束！")


def mianView1():
    global window
    window = tk.Tk()
    window.title("Mouse Control")
    window.geometry("350x80+700+450")

    start = tk.Button(window, text="开始",bg="Pink", font=("黑体",16), width=6, command=clickStart)
    pause = tk.Button(window, text="暂停",bg="red", font=("黑体",16), width=6, command=clickPause)
    stop = tk.Button(window, text="停止", bg="green",font=("黑体",16), width=6, command=clickStop)
    start.grid(column=0, row=0,padx=5,pady=5)
    pause.grid(column=1, row=0,padx=5,pady=5)
    stop.grid(column=2, row=0,padx=5,pady=5)
    window.protocol("WM_DELETE_WINDOW", close_window)
    window.mainloop()


if __name__ == '__main__':
    # mianView()
    mianView1()
