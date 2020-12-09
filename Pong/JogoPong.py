import turtle
from time import sleep
import random


def IniciarPong(Cor='Claro'):
    # Tema [Cor de fundo, Cor dos objetos, Logo do Fundo]
    Claro = ['#FCFCFC', '#343536', 'Estilo/IMDLogoAzul.gif', 'Claro']
    Escuro = ["#343536", '#FCFCFC', 'Estilo/IMDLogoCinza.gif', 'Escuro']
    if Cor == 'Claro':
        Tema = Claro
    elif Cor == 'Escuro':
        Tema = Escuro

    # Configurações iniciais
    Janela = turtle.Screen()
    Janela.title("Pong por @JaJoVic")
    Janela.bgcolor(Tema[0])
    Janela.setup(width=800, height=600)
    Janela.tracer(0)

    # Logo IMD
    Janela.addshape(Tema[2])
    Logo = turtle.Turtle()
    Logo.shape(Tema[2])

    # Defini aleatoriamente o sentido em que a bolinha começa
    x_inicial = random.choice([-1, 1])
    y_inicial = random.choice([-1, 1])
    # Velocidade da bola
    Velocidade = 0.3
    # Aumento de velocidade ao bater na barrinha
    Aceleracao = 1.1

    # Placar
    PlacarA = 0
    PlacarB = 0

    # Barra direita
    BarraD = turtle.Turtle()
    BarraD.speed(0)
    BarraD.shape("square")
    BarraD.color(Tema[1])
    BarraD.shapesize(stretch_wid=5, stretch_len=1)
    BarraD.penup()
    BarraD.goto(350, 0)

    # Barra esquerda
    BarraE = turtle.Turtle()
    BarraE.speed(0)
    BarraE.shape("square")
    BarraE.color(Tema[1])
    BarraE.shapesize(stretch_wid=5, stretch_len=1)
    BarraE.penup()
    BarraE.goto(-350, 0)

    # Bola
    Bola = turtle.Turtle()
    Bola.speed(0)
    Bola.shape("square")
    Bola.color(Tema[1])
    Bola.penup()
    Bola.goto(0, 0)
    # Movimento da bola (varia de acordo com o computador)
    Bola.dx = Velocidade * x_inicial
    Bola.dy = Velocidade * y_inicial

    # Caneta
    Caneta = turtle.Turtle()
    Caneta.speed(0)
    Caneta.shape("square")
    Caneta.color(Tema[1])
    Caneta.penup()
    Caneta.hideturtle()
    Caneta.goto(0, 260)
    Caneta.write(f'Jogador A : {PlacarA}  Jogador B : {PlacarB}',
                 align="center", font=("Courier", 20, "bold"))

    # Botão de sair
    BotaoSair = turtle.Turtle(visible=False)
    BotaoSair.pencolor(Tema[1])
    BotaoSair.fillcolor(Tema[1])
    BotaoComp = 60
    BotaoLarg = 30
    BotaoX = -15
    BotaoY = -290
    BotaoSair.penup()
    BotaoSair.begin_fill()
    BotaoSair.goto(BotaoX, BotaoY)
    BotaoSair.goto(BotaoX + BotaoComp, BotaoY)
    BotaoSair.goto(BotaoX + BotaoComp, BotaoY + BotaoLarg)
    BotaoSair.goto(BotaoX, BotaoY + BotaoLarg)
    BotaoSair.goto(BotaoX, BotaoY)
    BotaoSair.end_fill()
    BotaoSair.goto(BotaoX + 5, BotaoY + 7)
    BotaoSair.pencolor(Tema[0])
    BotaoSair.write('Voltar', "center", font=('Arial', 15, 'normal'))
    BotaoSair.pencolor(Tema[1])

    # Funções
    Sair = 0

    def ClicarSair(X, Y):
        if BotaoX <= X <= BotaoX + BotaoComp:
            if BotaoY <= Y <= BotaoY + BotaoLarg:
                nonlocal Sair
                Sair = 1

    def BarraDSobe():
        if BarraD.ycor() < 245:
            y = BarraD.ycor()
            y += 20
            BarraD.sety(y)

    def BarraDDesce():
        if BarraD.ycor() > -240:
            y = BarraD.ycor()
            y -= 20
            BarraD.sety(y)

    def BarraESobe():
        if BarraE.ycor() < 245:
            y = BarraE.ycor()
            y += 20
            BarraE.sety(y)

    def BarraEDesce():
        if BarraE.ycor() > -240:
            y = BarraE.ycor()
            y -= 20
            BarraE.sety(y)

    # Comandos do teclado
    Janela.listen()
    Janela.onkeypress(BarraDSobe, "Up")
    Janela.onkeypress(BarraDDesce, "Down")
    Janela.onkeypress(BarraESobe, "w")
    Janela.onkeypress(BarraEDesce, "s")
    Janela.onclick(ClicarSair)

    # Loop Principal

    while True:  # Loop Para sair do jogo
        Janela.update()

        # Mover bola
        Bola.setx(Bola.xcor() + Bola.dx)
        Bola.sety(Bola.ycor() + Bola.dy)

        # Colisão nas Bordas
        # Eixo Y
        if Bola.ycor() > 290:
            Bola.sety(290)
            Bola.dy *= -1

        if Bola.ycor() < -290:
            Bola.sety(-290)
            Bola.dy *= -1

        # Eixo X
        if Bola.xcor() > 390:
            Bola.goto(0, 0)
            Bola.dx = (Bola.dx/abs(Bola.dx)) * Velocidade*-1
            PlacarA += 1
            Bola.dy = Velocidade

        if Bola.xcor() < -390:
            Bola.goto(0, 0)
            Bola.dx = (Bola.dx/abs(Bola.dx)) * Velocidade*-1
            PlacarB += 1
            Bola.dy = Velocidade

        Caneta.clear()
        Caneta.write(f'Jogador A : {PlacarA}  Jogador B : {PlacarB}',
                     align="center", font=("Arial", 20, "bold"))

        # Colisão barra e bola
        # Direita
        if Bola.xcor() > 340 and Bola.xcor() < 350 and Bola.ycor() < BarraD.ycor() + 60 and Bola.ycor() > BarraD.ycor() - 60:
            Bola.setx(340)
            # Quando a bola bate, ela acelera
            Bola.dx *= -Aceleracao
            Bola.dy *= Aceleracao

            # Esquerda
        if Bola.xcor() < -340 and Bola.xcor() > -350 and Bola.ycor() < BarraE.ycor() + 60 and Bola.ycor() > BarraE.ycor() - 60:
            Bola.setx(-340)
            Bola.dx *= -Aceleracao
            Bola.dy *= Aceleracao

        if Sair != 0:
            Bola.hideturtle()
            BarraE.hideturtle()
            BarraD.hideturtle()
            Caneta.clear()
            Logo.hideturtle()
            BotaoSair.clear()
            break
