a = 0
while a < 3:
    a = int(input("请输入一任意大于2的偶数"))
for x in range(2,a):
    flag = "是质数"  #为了保证该示例人人看得懂，我们不使用布尔值进行表示
    for y in range(2,x):
        if x % y == 0:
            flag = "不是质数"
            break
    if flag == "是质数":
        b = a - x
        for y in range(2,b):
            if b % y == 0:
                flag = "不是质数"
                break
        if flag == "是质数":
            print(str(a) + "=" + str(x) + "+" + str(b))
            break
