import turtle

Tela = turtle.Screen()
Tela.setup(600,600)
Tela.setworldcoordinates(0,0,3,3)
Tela.tracer(0,0)
turtle.hideturtle()

JogaX = True
JogaO = False

def DesenhaTabuleiro():
    turtle.pensize(10)    
    for i in {1,2}:        
        turtle.up()
        turtle.goto(0,i)
        turtle.seth(0)
        turtle.down()
        turtle.fd(3)
    
        turtle.up()
        turtle.goto(i,0)
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

def ConfereResultado():    
    Xganhou = False
    Oganhou = False

    for i in {0,1,2}:
        if Casa[i][0] == Casa[i][1] and Casa[i][1] == Casa[i][2] and Casa[i][2] == "X":
            Tela.textinput("Game over! ","X ganhou!")
            Xganhou = True
        elif Casa[i][0] == Casa[i][1] and Casa[i][1] == Casa[i][2] and Casa[i][2] == "X":
            Tela.textinput("Game over! ","O ganhou!")
            Oganhou = True

        break

        for j in {0,1,2}:
            if Casa[0][j] == Casa[1][j] and Casa[1][j] == Casa[2][j] and Casa[2][j] == "X":
                Tela.textinput("Game over! ","X ganhou!")
                Xganhou = True
            elif Casa[0][j] == Casa[1][j] and Casa[1][j] == Casa[2][j] and Casa[2][j] == "X":
                Tela.textinput("Game over! ","O ganhou!")
                Oganhou = True
    
    if Xganhou and Oganhou:
        Tela.textinput("Game over! ","Empate!")

def Jogo():
    DesenhaTabuleiro()
    Tela.onclick(RegistraJogada)
    ConfereResultado()

Casa = [[0,0,0],[0,0,0],[0,0,0]]

Jogo()

turtle.mainloop()

