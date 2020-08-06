for x in range(10000):
    n = str(x**2)
    m = str(x)
    c = len(m)
    if x == int(n[-c::]):
        print(x)

a = 0
for x in range(2,100):
    a += 1
    if a%2 != 0:
        print(a)

s = []
for x in range(2,100):
    flag = "是质数"             #这里为了方便初学者观看，不用布尔值了
    for y in range(2,x):
        if x % y == 0:
            flag = "不是质数"
            break
    if flag == "是质数":
        s.append(x)
print(s)

