# 学费计算器
# 路飞学成共有15门编程课程，每门课程单价：10000元
#  .一次性购买3门课程及以上，每门课程优惠1.5元
#  . 一次性购买5门课程及以上，每门课程优惠2元
#  . 一次性购买10门以上， 赠送终身Vip, 优惠50元，并且赠送黑姑娘的签名照

class TuitionCalculator:
    def __int__(self) -> None:
        ...

    def doCalculator(self):
        sinle_price = 1000
        num = int(input("购买课程数量为："))
        pay: float
        if 3 <= num < 5:
            pay = num * (sinle_price - 1.5)
        elif 5 <= num < 10:
            pay = num * (sinle_price - 2)
        elif 10 <= num <= 15:
            pay = num * sinle_price - 50
            print("获得终身Vip一张")
            print("获得黑姑娘签名照一张")
        elif num > 15:
            print("请理性消费")
        else:
            print("输入有误")
        print(f"本次消费金额为：{pay}")