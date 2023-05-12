import re

# 定义正则表达式
regex = r'^test(?!.*automation trigger:revert to last version).*$'

# 定义测试数据
test_data = [
    "test1",
    "test2",
    "test3",
    "test4",
    "test5",
    "test6",
    "test7",
    "test8",
    "test9",
    "test10",
    "test automation trigger:revert to last version",
    "test with automation trigger:revert to last version",
    "test automation trigger:revert to last version and more",
    "automation trigger:revert to last version test",
    "automation trigger:revert to last version",
    "test MR3 fhiogsdfghsh gdgdhg",
    "test MR#2  fhiogsdfghsh gdgdhg",
]
# strart 1
# strart 2
# start 3
# test1
# test2
# 遍历测试数据并进行匹配
for data in test_data:
    match = re.match(regex, data)
    if match:
        print(f"{data}: 匹配成功")
    else:
        print(f"{data}: 匹配失败")