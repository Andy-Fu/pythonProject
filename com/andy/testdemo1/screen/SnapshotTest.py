import os
import signal
import subprocess

import pywintypes
from PIL import Image
import win32gui
import win32con
import pyautogui

import sys
import win32process as wproc
import win32api as wapi
from pywinauto.application import Application
from time import sleep

import pynput.keyboard as pk
import keyboard  #监听键盘


names = set()
windows = []

def get_window_title(window, nouse):
    '''
    获取窗口标题函数
    :param window: 窗口对象
    :param nouse:
    :return:
    '''
    if win32gui.IsWindow(window) and win32gui.IsWindowEnabled(window) and win32gui.IsWindowVisible(window):
        #windows.append(win32gui.GetWindow(window))
        names.add(win32gui.GetWindowText(window))



def main(*argv):
    if not argv:
        window_name = input("Enter window name: ")
    else:
        window_name = argv[0]

    handle = win32gui.FindWindow(None, window_name)
    print("Window `{0:s}` handle: 0x{1:016X}".format(window_name, handle))
    if not handle:
        print("Invalid window handle")
        return
    remote_thread, _ = wproc.GetWindowThreadProcessId(handle)
    wproc.AttachThreadInput(wapi.GetCurrentThreadId(), remote_thread, True)
    prev_handle = win32gui.SetFocus(handle)

#name = input('请输入需要截图的活动窗口名称: \n')
#window = win32gui.FindWindow(0, name)  # 根据窗口名称获取窗口对象
def getActiveWindows():
    global window
    win32gui.EnumWindows(get_window_title, 0)
    for window in windows:
        print("###", window)
    list_ = [name for name in names if name]
    for n in list_:
        print('活动窗口: ', n)


def activeWindowByName():
    global window
    isWindowShow = False
    while not isWindowShow:
        os.system('start snippingtool')
        # getActiveWindows()
        window = win32gui.FindWindow(None, "截图工具")  # 根据窗口名称获取窗口对象
        if window == 0:
            isWindowShow = False
            print(f"打开失败！重试一次")
            continue
        else:
            print(f"打开成功!")
            isWindowShow = True
    print(f"##截图工具{window}")
    win32gui.ShowWindow(window, win32con.SW_NORMAL)  # 将该窗口最大化
    win32gui.SetActiveWindow(window)
    isForegroundWindow = False
    while (not isForegroundWindow):
        try:
            win32gui.SetWindowPos(window, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
            win32gui.SetWindowPos(window, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                                  win32con.SWP_SHOWWINDOW | win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
            win32gui.SetForegroundWindow(window)
            isForegroundWindow = True
            print("is true")
        except pywintypes.error as e:
            isForegroundWindow = False
            print(f"会报一下错误：{e}，需要怎么该")

    print("按键按下！")
    sleep(1)
    keyboard.press_and_release('Ctrl+n')

def on_press(key):
    # 监听按键
    print("-------------")
    key=str(key)
    print("按键为",key)
def on_release(key):
    print("+++++++++++")
    print("####",key)

def test_a():
    print('aaa')

def test():
    global pid
    print("22222")
    window = win32gui.FindWindow(None, "截图工具")  # 根据窗口名称获取窗口对象
    if window == 0:
        print("截图工具未打开!")
        return
    # 关闭截图工具
    win32gui.SetWindowPos(window, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    win32gui.SetWindowPos(window, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                          win32con.SWP_SHOWWINDOW | win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    win32gui.SetForegroundWindow(window)
    keyboard.press_and_release('alt+f4')


def doRegiestHotKey():
    #activeWindowByName()
    # 连接事件以及释放
    # with pk.Listener(on_press=on_press ,on_release = on_release,key ={'ctrl','alt','q'}) as pklistener:
    #     pklistener.join()
    keyboard.add_hotkey('ctrl+q', activeWindowByName)
    keyboard.add_hotkey('esc', test)
    # 按ctrl+alt输出b
    try:
        keyboard.wait('ctrl+esc')
        return True
    except KeyboardInterrupt as e:
        print(f"：中断错误:{e}")
        return False

    # if keyboard.wait(hotkey='ctrl+alt+q') == None:
    #     activeWindowByName()


    # with pk.GlobalHotKeys({'<ctrl>+<alt>+q': activeWindowByName}) as h:
    #     h.join()

    # print("Python {0:s} {1:d}bit on {2:s}\n".format(" ".join(item.strip() for item in sys.version.split("\n")), 64 if sys.maxsize > 0x100000000 else 32, sys.platform))
    # main(*sys.argv[1:])
    # print("\nDone.")



#win32gui.ShowWindow(window, win32gui.SW_MAXIMIZE)  # 将该窗口最大化
if __name__ == '__main__':
    doRegiestHotKey()


