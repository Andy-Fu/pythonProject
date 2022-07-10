# 身高预测系统
# 身高预测公式：
# 男性成人时身高 = （父亲身高 + 母亲身高） * 0.54
# 女性成人时身高 = （父亲身高 * 0.923 + 母亲身高） / 2
# 如果经常进行体育锻炼，那么可以增加2%
# 如果有良好的饮食习惯，那么可以增加1.5%

class ChildHeight:
    def __init__(self) -> None:
        ...

    def computuHeight(self):
        fatherHeight = float(input("父亲身高："))
        motherHeight = float(input("母亲身高："))
        gender = input("孩子性别：")
        do_physical_training = input("是否体育锻炼(是/否)：")
        do_healthy_eating = input("是否健康饮食(是/否)：")
        child_height: float
        if gender == "男":
            child_height = (fatherHeight + motherHeight) * 0.54
        else:
            child_height = (fatherHeight * 0.923 + motherHeight) / 2

        if do_physical_training == "是":
            child_height *= 1.02
        if do_healthy_eating == "是":
            child_height *= 1.015
        print(f"孩子的身高为：{child_height}")
