import turtle
t = turtle.Turtle()


t.speed(0)
a = input("1")
b = input("2")
c = input("3")
d = input("4")
color = [a,b,c,d]
for x in range(1000):
    t.color(color[x%4])
    t.forward(x)
    t.left(91)

    
turtle.done()
