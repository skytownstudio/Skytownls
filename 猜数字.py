import random
a = random.randint(1,10)
#电脑生成的数
n = int(input("请输入1-10之间要猜的数"))
#猜的数

while a != n: #!= 是不等于
    if n>a:
        print(n,"猜大了")
    if n<a:   #也可以elif
        print(n,"猜小了")
    n = int(input("继续猜："))
print(n,"猜对了！")
