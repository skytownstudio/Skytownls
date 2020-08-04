import random

types=["♥","♦","♣","♠"]
num=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

cards = []

for fs in range(4):
    for fa in range(13):
        card = types[fs] + num[fa]
        cards.append(card)

pa=[[],[],[],[]]

for i in range(4):
    for x in range(i,52,4):
        pa[i].append(cards[x])
    print("玩家"+str(i+1)+"的牌为："+str(pa[i]))
winnum = types[random.randint(0,3)]
print("包含",winnum,"的玩家会获胜")

for winaaa in range(4):
    randomCard = pa[winaaa][random.randint(0,12)]
    print("玩家"+str(winaaa)+"的牌为"+randomCard)
    if randomCard[0] == winnum:
        print("玩家"+str(winaaa)+"赢了")
    else:
        print("玩家"+str(winaaa)+"输了")
