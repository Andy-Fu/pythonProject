import random
import sys
import tkinter as tk
import threading
import pyautogui

isRuning = False
timer: threading.Timer = None
window: tk.Tk


def fun_timer():
    global isRuning, timer
    if not isRuning:
        return
    print('Hello Timer!')
    positionX, positionY = pyautogui.position()
    size = pyautogui.size()
    pyautogui.moveTo(random.randint(0, size.width), random.randint(0, size.height))
    print(f"{positionX},{positionY}")
    timer = threading.Timer(5, fun_timer)
    timer.start()


def clickStart():
    global isRuning, timer
    isRuning = True
    timer = threading.Timer(1, fun_timer)
    timer.start()
    print(f"clickStart{isRuning}")

# bool 值取反    isRuning = bool(1 - isRuning)
def clickPause():
    global isRuning, timer
    if (timer == None) :
        return
    if isRuning :
        isRuning = False
        timer.cancel()
    else:
        clickStart()
    print(timer)
    print(f"clickPause{isRuning}")


def clickStop():
    global isRuning, timer
    if (timer == None):
        return
    isRuning = False
    timer.cancel()
    print(f"clickStop{isRuning}")
    sys.exit("程序结束！")


def close_window():
    global window, timer
    window.destroy()
    timer.cancel()
    sys.exit("程序结束！")


def mianView1():
    global window
    window = tk.Tk()
    window.title("Mouse Control")
    window.geometry("350x80+700+450")

    start = tk.Button(window, text="开始", bg="Pink", font=("黑体", 16), width=6, command=clickStart)
    pause = tk.Button(window, text="暂停", bg="red", font=("黑体", 16), width=6, command=clickPause)
    stop = tk.Button(window, text="停止", bg="green", font=("黑体", 16), width=6, command=clickStop)
    start.grid(column=0, row=0, padx=5, pady=5)
    pause.grid(column=1, row=0, padx=5, pady=5)
    stop.grid(column=2, row=0, padx=5, pady=5)
    window.protocol("WM_DELETE_WINDOW", close_window)
    window.mainloop()


if __name__ == '__main__':
    mianView1()
