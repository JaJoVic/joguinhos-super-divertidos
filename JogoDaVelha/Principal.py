import turtle

Tela = turtle.Screen()
Tela.setup(600,600)
Tela.setworldcoordinates(0,0,5,5)
Tela.tracer(0,0)
turtle.hideturtle()

JogaX = True
JogaO = False

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
    turtle.goto(x+0.8,y+0.5)
    turtle.down()
    turtle.circle(0.3, steps=100)

    Tela.update()

def DesenhaX(x,y):
    turtle.up()
    turtle.goto(x+0.2,y+0.2)
    turtle.down()
    turtle.goto(x+0.8,y+0.8)
    
    turtle.up()
    turtle.goto(x+0.2,y+0.8)
    turtle.down()
    turtle.goto(x+0.8, y+0.2)

    Tela.update()

def RegistraJogada(x,y):
    global JogaX
    global JogaO

    i = 2 - (int(y) - 1)
    j = int(x) - 1

    if JogaX:
        DesenhaX(int(x),int(y))
        Casa[i][j] = "X"
        JogaX = False
        JogaO = True

    elif JogaO:
        DesenhaO(int(x),int(y))
        Casa[i][j] = "O"
        JogaO = False
        JogaX = True

DesenhaTabuleiro()
Tela.onclick(RegistraJogada)

Casa = [[0,0,0],[0,0,0],[0,0,0]]

turtle.mainloop()

