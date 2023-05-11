class LoopDemo:
    def __init__(self) -> None:
        ...

    # 被打血量问题
    def whileLoop(self):
        blood_volume = 10
        base_harm = 3
        count = 0
        while blood_volume > 0:
            blood_volume -= base_harm
            # 三元运算符
            print(f"妈妈打我了，伤害{base_harm},还剩血量：{blood_volume if blood_volume > 0 else 0}")
            count += 1
        print(f"当看到这个消息的时候，我应该已经没了：你看看我被打了多少次：{count}")

    # 邀请卡问题
    # 线下交流会参与人员名单： ['曾彬','吴晨','严涛','李伟','秦云','王娟','赵秀荣','曹秀华','程玲','商娜']
    # 为每位嘉宾打印邀请卡：
    # 亲爱的 XXX:
    #    感谢您长久以来对路飞学城的支持与关注。我门将于2050年，在北京丽思卡尔顿酒店门口，举办线下交流活动。
    #        特邀您自费参加！
    def forLoop(self):
        guest_list = ['曾彬', '吴晨', '严涛', '李伟', '秦云', '王娟', '赵秀荣', '曹秀华', '程玲', '商娜']
        for name in guest_list:
            print(f'''
        亲爱的{name}:
           感谢您长久以来对路飞学城的支持与关注。我门将于2050年，在北京丽思卡尔顿酒店门口，举办线下交流活动。
              特邀您自费参加！
            ''')

    def forLoopTest(self):
        count = 10
        guest_list = ['曾彬', '吴晨', '严涛', '李伟', '秦云', '王娟', '赵秀荣', '曹秀华', '程玲', '商娜']
        
        for index, item in enumerate(guest_list):
            print(f"现在循环第{index}次:{item}")

        print(f"______________{count}")
        # range(10) 从0循环到9，每次加1
        for i in range(count):
            print(f"现在循环第{i}次")
        # range(2,10) 从2循环到9,每次加1
        print(f"______________{count}")
        # range(3,10,2) 从3开始 每次加2，循环到9
        for i in range(3, 10, 2):
            print(f"现在循环第{i}次")

        print(f"______________{count}")
        for i in range(count, 3, 2):
            print(f"现在循环第{i}次")
