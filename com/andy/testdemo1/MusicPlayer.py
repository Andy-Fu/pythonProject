import os
import random
import time
import datetime

import pygame



class MusicPlayer:
    basePath = r"D:\PycharmProjects\pythonProject\resources"
    def __int__(self)->None:...
    def play_music(self, filePath):
        pygame.mixer.init()
        print(filePath)
        pygame.mixer.music.load(filePath)
        pygame.mixer.music.play()
        time.sleep(30)
        pygame.mixer.music.stop()

    def shuffle_play(self):
        pathList = os.listdir(self.basePath)
        random.shuffle(pathList)
        filePath = random.choice(pathList)
        self.play_music(self.basePath+"/"+filePath)

    def specific_play(self):
        filePath =  self.basePath+r"\富士山下 - 陈奕迅.mp3"
        self.play_music(filePath)

    # %Y-%m-%d %H:%M:%S -> 2022-07-10 01:14:09
    # %H:%M:%S -> 01:14:09
    def mainRoot(self):
        print("*****欢迎来到本系统******")
        nowTime = datetime.datetime.now()
        print(nowTime.strftime("%H:%M:%S"))
        scheduleTime =(nowTime + datetime.timedelta(seconds=+20)).strftime("%H:%M:%S")
        print(scheduleTime)
        specificTime = (nowTime + datetime.timedelta(seconds=+60)).strftime("%H:%M:%S")
        print(specificTime)
        # 获取5分钟之后的时间
        print()
        while True:
            nowTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(f"\r系统当前时间为：{nowTime}",end="")
            if scheduleTime == nowTime:
                self.shuffle_play()
                continue
            elif nowTime == specificTime:
                self.specific_play()
                break
            time.sleep(0.8)