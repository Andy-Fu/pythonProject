import os.path
import re

# 忽略大小写 匹配c/d
import sys
from pathlib import Path
import requests  # 调用 requests 库


import exrex as exrex
# name = "黄佳斯".encode("gb2312")
# for i in range(0,5,2):
#     print(i)

# name = "黄佳斯"
# for i in range(0,len(name),2):
#     print(i)
#
# print("黄".encode("gb2312"))
# strname = ''
# print(name)
# name1= "xc%ex%e9%xc%bx%bc%xc%fx%bc"
# name1 = "%xb%bx%c6%xb%cx%d1%xc%bx%b9"
# name = "%E9%BB%84%E4%BD%B3%E6%96%AF"
# name1 = "黄佳斯"
# url = f'http://www.jxpta.com/cjcx.php?id={name1}&ziduan=3494&mima=362524199711266028&dlbz=cjcx&texttow=1'
# dates = {'date': '2021-05-05', 'key': 'XXXX'}
#dates = {'date': '2021-07-15', 'key': 'XXXX'}
# headers = {
#  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'}
# res = requests.get(url, headers=headers)  # 修改 headers 隐藏真实的请求地址，改为浏览器请求,即是伪装
# print(res.content.decode("gb2312"))

cde_name = "cde _name_asd"
cde_name=cde_name.replace("_","[",1)
cde_name=cde_name.replace("_","]",1)
print("##########" + cde_name)
partt1='_'
partt2='][a-zA-Z]'
pattreback = re.compile(partt2)
print("search___",pattreback.search(cde_name))
parrblack2 = re.compile(r'(|)(CD|abc|F|G|[0-9])(|)')

s2 = "599"
print("s2",parrblack2.search(s2))


parrblack = re.compile(r'(^.{0}$)')
s0 = "None"
print("s0",parrblack.search(s0))

print("-------------")
parrblack1 = re.compile(r'^((?!(^.{0}$)).)+$')
print(exrex.getone(r'^((?!(^.{0}$)).)+$'))
s1 = '1111aaa'
print("s1",parrblack1.search(s1))
print("-------------")

pattern = re.compile('(?i)(^C$|^D$)')
str1 = 'CD'
print(pattern.search(str1))

patternY = re.compile('(^Y$|^N$)')
stry = 'N'
print(patternY.search(stry))

#res = re.compile('^(?!(^C$|^D$))')
res = re.compile(r'^((?!(^C$|^D$)).)*$')
stry1 = 'D'
print("C or D:\t",res.search(stry1))
#var = exrex.getone(r'^(?!(^C$|^D$))')
var = exrex.getone(r'^((?!(^C$|^D$)).)*$')
var1 = exrex.getone(r'(^C$|^D$)')
print(var, var1)



def genear(aaa):
    return [exrex.getone(aaa) for i in range(10)]
print("---------------")
name = "伍思霞"
print(name.encode("gb2312"))
print("---------------")
print(genear(r'^((?!(^C$|^D$)).)*$'))
tag = "sfsfsgsg"
records = 10
print('({})'.format('"' + tag + '","' + str(records) + '"'))
datav = f'({tag},{records})'



root_pth = str(sys.argv[0])[:33]
print(root_pth)
resouse = root_pth + '/resources'
stats = resouse + '/sql/'
table_name = "transaction_master"
business_date = '2022-03-01'

if not os.path.exists(Path(stats)):
    os.makedirs(Path(stats))
    print(f"statsPath:{stats}")
    insert_stats = "Insert overwrite table {} partition(business_date = '{}') \n Values \n ".format(table_name, business_date)
    with open(Path(stats+"tmdq_expect_result.sql"),'w') as  f:
        f.write(insert_stats)
        datas = []
        for i in range(5):
            dataValue = '("{}",{})'.format(tag,records)
            print(dataValue)
            datas.append(dataValue)
        dataValueFinal = "\n,".join(datas)
        print(dataValueFinal)
        f.write(dataValueFinal +"\n")
        f.write(";")
        f.close()



print(f'({tag},{records})')
