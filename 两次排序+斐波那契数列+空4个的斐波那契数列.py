l = [8,7,12,10,3] #放进列表
print("排序前：",l)
for x in range(4): #四轮交换
    for y in range(4-x): #每轮都比上一次少一道交换
        if l[y] > l[y+1]: #如果左边大于右边那么执行
            l[y],l[y+1] = l[y+1],l[y] #交换
            print("交换中",l)
print("排序后：",l)

import random
a = range(1,100)  
s = random.sample(a,10)  #随机抽取数字来进行交换
print("排序前：",s)
for x in range(9):
    for y in range(9-x):
        if s[y] < s[y+1]:
            s[y],s[y+1]=s[y+1],s[y]
            print("交换中",s)
print("交换后：",s)

es = [] #奇
os = [] #偶
a = 1
b = 1
for x in range(20):
    if a % 2 == 0:
        es.append(a)
    else:
        os.append(a)
    a,b = b,a+b
print(es)
print(os)

s = []
x = 1
for n in range(10):  #每次加4的斐波那契数列哈
    s.append(x)
    x += 4
print(s)
