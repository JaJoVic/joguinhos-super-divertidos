import turtle

Tela = turtle.Screen()
Tela.setup(600,600)
Tela.setworldcoordinates(0,0,5,5)
Tela.tracer(0,0)
turtle.hideturtle()

GameOver = False
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
    global Jogadas

    if x >= 1 and y >= 1 and x <= 4 and y <= 4:

        i = 2 - (int(y) - 1)
        j = int(x) - 1

        if JogaX and Casas[i][j] == 0:
            DesenhaX(int(x),int(y))
            Casas[i][j] = "X"
            JogaX = False
            JogaO = True
            Jogadas += 1

        elif JogaO and Casas[i][j] == 0:
            DesenhaO(int(x),int(y))
            Casas[i][j] = "O"
            JogaO = False
            JogaX = True
            Jogadas += 1
        
        ConfereResultado()

def ConfereResultado():
    global GameOver

    for i in range(3):
        if Casas[i][0] == Casas[i][1] and Casas[i][1] == Casas[i][2] and Casas[i][2] != 0:
            if Casas[i][2] == "X":
                Tela.textinput("Game over!","X venceu!")
                GameOver = True
            elif Casas[i][2] == "O":
                Tela.textinput("Game over!","O venceu!")
                GameOver = True

        elif Casas[0][i] == Casas[1][i] and Casas[1][i] == Casas[2][i] and Casas[2][i] != 0:
            if Casas[2][i] == "X":
                Tela.textinput("Game over!","X venceu!")
                GameOver = True
            elif Casas[2][i] == "O":
                Tela.textinput("Game over!","O venceu!")
                GameOver = True

    if Casas[0][0] == Casas[1][1] and Casas[1][1] == Casas[2][2] and Casas[2][2] != 0:
        if Casas[2][2] == "X":
            Tela.textinput("Game over!","X venceu!")
            GameOver = True
        elif Casas[2][2] == "O":
            Tela.textinput("Game over!","O venceu!")
            GameOver = True
        
    elif Casas[2][0] == Casas[1][1] and Casas[1][1] == Casas[0][2] and Casas[0][2] != "O":
        if Casas[0][2] == "X":
            Tela.textinput("Game over!","X venceu!")
            GameOver = True
        elif Casas[0][2] == "O":
            Tela.textinput("Game over!","O venceu!")
            GameOver = True

    if Jogadas == 9 and not GameOver:
        Tela.textinput("Game over!","Empate!")
        GameOver = True


DesenhaTabuleiro()
Tela.onclick(RegistraJogada)

Jogadas = 0
Casas = [[0,0,0],[0,0,0],[0,0,0]]

    

turtle.mainloop()

