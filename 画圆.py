import turtle
t = turtle.Turtle()
x = int(input("请输入x坐标"))
y = int(input("请输入y坐标"))
radius = int(input("请输入圆的半径"))
t.penup()
t.goto(x,y - radius)
t.pendown()
t.circle(radius)
