import turtle
import math

def drawBoard():
    for i in range(2):
        drawer.penup()
        drawer.goto(-300, 100 - 200 * i)
        drawer.pendown()
        drawer.forward(600)
    drawer.right(90)
    for i in range(2):
        drawer.penup()
        drawer.goto(-100 + 200 * i, 300)
        drawer.pendown()
        drawer.forward(600)
    num = 1
    for i in range(3):
        for j in range(3):
            drawer.penup()
            drawer.goto(-290 + j * 200, 280 - i * 200)
            drawer.pendown()
            drawer.write(num, font = ("Arial", 12))
            num += 1
    screen.update()

def drawX(x,y):
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    drawer.setheading(60)
    for i in range(2):
        drawer.forward(75)
        drawer.backward(150)
        drawer.forward(75)
        drawer.left(75)
    screen.update()

def drawO(x, y):
    drawer.penup()
    drawer.goto(x, y + 75)
    drawer.pendown()
    drawer.setheading(0)
    for i in range(180):
        drawer.forward((150 * math.pi)/180)
        drawer.right(2)
    screen.update()

def addX(row, column):
    drawX(-200 + 200 * column, 200 - 200 * row)

drawer = turtle.Turtle()
drawer.pensize(10)
drawer.ht()

screen = turtle.Screen()
screen.tracer(0)

drawBoard()
drawO(0,0)