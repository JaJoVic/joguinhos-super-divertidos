import turtle

def IniciarVelha(Cor='Claro'):
    Claro = ['#FCFCFC', '#343536', 'Estilo/IMDLogoAzul.gif', 'Claro']
    Escuro = ["#343536", '#FCFCFC', 'Estilo/IMDLogoCinza.gif', 'Escuro']
    if Cor == 'Claro':
        Tema = Claro
    elif Cor == 'Escuro':
        Tema = Escuro

    Janela = turtle.Screen()
    Janela.setup(600,600)
    Janela.setworldcoordinates(0,0,5,5)
    Janela.tracer(0)
    Janela.bgcolor(Tema[0])


    global JogaX
    global JogaO
    global Jogadas
    global GameOver
    JogaX = True
    JogaO = False
    Jogadas = 0
    GameOver = False
    Casas = [[0,0,0],[0,0,0],[0,0,0]]
    Tartaruga = turtle.Turtle()
    Tartaruga.hideturtle()
    Tartaruga.pencolor(Tema[1])
    def DesenhaTabuleiro():
        Tartaruga.pensize(10)    
        for i in {2,3}:        
            Tartaruga.up()
            Tartaruga.goto(1,i)
            Tartaruga.seth(0)
            Tartaruga.down()
            Tartaruga.fd(3)
        
            Tartaruga.up()
            Tartaruga.goto(i,1)
            Tartaruga.seth(90)
            Tartaruga.down()
            Tartaruga.fd(3)
        Janela.update()

    def DesenhaO(x,y):
        Tartaruga.up()
        Tartaruga.goto(x+0.8,y+0.5)
        Tartaruga.down()
        Tartaruga.circle(0.3, steps=100)

        Janela.update()

    def DesenhaX(x,y):
        Tartaruga.up()
        Tartaruga.goto(x+0.2,y+0.2)
        Tartaruga.down()
        Tartaruga.goto(x+0.8,y+0.8)
        
        Tartaruga.up()
        Tartaruga.goto(x+0.2,y+0.8)
        Tartaruga.down()
        Tartaruga.goto(x+0.8, y+0.2)

        Janela.update()

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
                    Janela.textinput("Game over!","X venceu!")
                    GameOver = True
                elif Casas[i][2] == "O":
                    Janela.textinput("Game over!","O venceu!")
                    GameOver = True

            elif Casas[0][i] == Casas[1][i] and Casas[1][i] == Casas[2][i] and Casas[2][i] != 0:
                if Casas[2][i] == "X":
                    Janela.textinput("Game over!","X venceu!")
                    GameOver = True
                elif Casas[2][i] == "O":
                    Janela.textinput("Game over!","O venceu!")
                    GameOver = True

        if Casas[0][0] == Casas[1][1] and Casas[1][1] == Casas[2][2] and Casas[2][2] != 0:
            if Casas[2][2] == "X":
                Janela.textinput("Game over!","X venceu!")
                GameOver = True
            elif Casas[2][2] == "O":
                Janela.textinput("Game over!","O venceu!")
                GameOver = True
            
        elif Casas[2][0] == Casas[1][1] and Casas[1][1] == Casas[0][2] and Casas[0][2] != "O":
            if Casas[0][2] == "X":
                Janela.textinput("Game over!","X venceu!")
                GameOver = True
            elif Casas[0][2] == "O":
                Janela.textinput("Game over!","O venceu!")
                GameOver = True

        if Jogadas == 9 and not GameOver:
            Janela.textinput("Game over!","Empate!")
            GameOver = True

    DesenhaTabuleiro()
    Janela.onclick(RegistraJogada)
    while True:
        Janela.update()
        if GameOver == True:
            Tartaruga.clear()
            Tartaruga.reset()
            Janela.clearscreen()
            Janela.resetscreen()
            Janela.bye()
            Janela.clearscreen()
            break
