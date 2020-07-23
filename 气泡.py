import turtle
import random
t = turtle.Turtle()
color = ["red","yellow","#00FF00","blue","purple"]

for x in range(30):
    a = random.randint(-200,200)
    b = random.randint(-110,200)
    t.penup()
    t.goto(a,b)
    t.pendown()
    t.begin_fill()
    t.color(color[x%5])
    if x%3 == 0:
        t.circle(10)
    else:
        for x in range(3):
            t.forward(20)
            t.left(120)
    t.end_fill()
