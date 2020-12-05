import turtle

Tela = turtle.Screen()
Tela.setup(600,600)
Tela.setworldcoordinates(0,0,5,5)
Tela.tracer(0,0)
turtle.hideturtle()

def DesenhaTabuleiro():
    turtle.pensize(10)
    for i in {2,3}:
        turtle.up()
        turtle.goto(1,i)
        turtle.seth(0)
        turtle.down()
        turtle.fd(3)
    
        turtle.up()
        turtle.goto(i,1)
        turtle.seth(90)
        turtle.down()
        turtle.fd(3)

    Tela.update()

def DesenhaO(x,y):
    turtle.up()
    turtle.goto(x,y-0.75)
    turtle.seth(0)
    turtle.down()
    turtle.circle(0.75, steps=100)

DesenhaTabuleiro()

turtle.mainloop()