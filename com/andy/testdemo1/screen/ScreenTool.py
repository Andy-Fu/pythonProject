import os
import pywintypes
import win32gui
import win32con
from time import sleep
import keyboard  #监听键盘

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



def closeWindowByName():
    global pid
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
    keyboard.add_hotkey('ctrl+q', activeWindowByName)
    keyboard.add_hotkey('esc', closeWindowByName)
    # 按ctrl+alt输出b
    try:
        keyboard.wait('ctrl+esc')
        return True
    except KeyboardInterrupt as e:
        print(f"：中断错误:{e}")
        return False

if __name__ == '__main__':
    doRegiestHotKey()


