import random
import sys


class RandomDemo:
    def __int__(self) -> None: ...

    # 猜数字小游戏：
    # 程序随机生成一个0-99之前的整数。并命名为：num。
    # 给用户10次机会，猜出num 中的数字是什么：
    # 1、如果用户输入的数字大于num，则打印"猜大了"
    # 2、如果用户输入的数字小于num，则打印"猜小了"
    # 3、如果猜中，则打印“恭喜你！”，并退出程序
    def randomGame(self):
        num = random.randint(0,99)
        getInput: int
        residue_degree = 10
        for index in range(10):
            residue_degree -=1
            try:
                getInput = int(input("请输入(0-99)："))
            except  KeyboardInterrupt as ke:
                print("输入终止！游戏结束")
                sys.exit("程序结束！")
                # break
            except ValueError as ve:
                print(f"输入有误，请重新输入，输入范围为(0-99)!,剩余次数：{residue_degree}")
                continue
            if getInput == num :
                print("恭喜你！")
                sys.exit("程序结束！")
                # break
            elif getInput > num:
                print(f"猜大了！,剩余次数：{residue_degree}")
            elif getInput < num:
                print(f"猜小了！,剩余次数：{residue_degree}")
            else:
                print(f"输入有误,剩余次数：{residue_degree}")

    # 随机数模块
    def randomTest(self):
        # 生成0，1之间的随机数
        rd = random.random()
        print(rd)

        # 生成3，5之前随机值
        rdf = random.uniform(3,5)
        print(rdf)

        # 生成5，10之间的整数
        rdi = random.randint(5,10)
        print(rdi)

        # 从序列中随机选择
        rdcs = random.choice("abcdefghijklmnopqrstuvwxyz")
        print(rdcs)
        rdcl = random.choice(["andy","luckly","sunshine","richard"])
        print(rdcl)

        # 随机打乱列表中的顺序
        list1 = [1,2,3,4,5,6,7,8,9]
        random.shuffle(list1)
        print(list1)

        # 从列表中随机选择多个结果
        list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        rds = random.sample(list2,3)
        print(rds)



