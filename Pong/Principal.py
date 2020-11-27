#Projeto PONG

import turtle
from time import sleep
#Para som funionar no linux ou mac
#import os
#Para som funionar no windows
import winsound

# Configurações iniciais
Janela = turtle.Screen()
Janela.title("Pong por @JaJoVic")
Janela.bgcolor("black") 
Janela.setup(width=800, height = 600) 
Janela.tracer(0)

#Placa
PlacarA = 0
PlacarB = 0

#Barra direita
BarraD = turtle.Turtle()
BarraD.speed(0)
BarraD.shape("square")
BarraD.color("white")
BarraD.shapesize(stretch_wid=5, stretch_len = 1)
BarraD.penup()
BarraD.goto(350,0)

#Barra esquerda
BarraE = turtle.Turtle()
BarraE.speed(0)
BarraE.shape("square")
BarraE.color("white")
BarraE.shapesize(stretch_wid=5, stretch_len = 1)
BarraE.penup()
BarraE.goto(-350,0)

#Bola
Bola = turtle.Turtle()
Bola.speed(0)
Bola.shape("square")
Bola.color("white")
Bola.penup()
Bola.goto(0,0)
#Movimento da bola (varia de acordo com o computador)
Bola.dx = 0.3
Bola.dy = 0.3

#Caneta
Caneta = turtle.Turtle()
Caneta.speed(0)
Caneta.shape("square")
Caneta.color("white")
Caneta.penup()
Caneta.hideturtle()
Caneta.goto(0, 260)
Caneta.write(f'Jogador A : {PlacarA}  Jogador B : {PlacarB}', align="center", font =("Courier",20, "bold"))

#Funções
def BarraDSobe():
    y = BarraD.ycor()
    y += 20
    BarraD.sety(y)

def BarraDDesce():
    y = BarraD.ycor()
    y -= 20
    BarraD.sety(y)

def BarraESobe():
    y = BarraE.ycor()
    y += 20
    BarraE.sety(y)

def BarraEDesce():
    y = BarraE.ycor()
    y -= 20
    BarraE.sety(y)

#Comandos do teclado
Janela.listen()
Janela.onkeypress(BarraDSobe, "Up")
Janela.onkeypress(BarraDDesce, "Down")
Janela.onkeypress(BarraESobe, "w")
Janela.onkeypress(BarraEDesce, "s")


#Loop Principal
while True:
    Janela.update()

    #Mover bola
    Bola.setx(Bola.xcor() + Bola.dx)
    Bola.sety(Bola.ycor() + Bola.dy)

    #Colisão nas Bordas
        #Eixo Y
    if Bola.ycor() > 290:
        Bola.sety(290)
        Bola.dy *= -1
        #Som no linux
        #os.system("afplay pop.mp3&")
        #Som no windows (NÃO FUNCIONA AINDA)
        #winsound.PlaySound("Pong\som\moeda.waw",winsound.SND_ASYNC, winsound.SND_FILENAME)
    if Bola.ycor() < -290:
        Bola.sety(-290)
        Bola.dy *= -1
        #Som no linux
        #os.system("afplay pop.mp3&")

        #Eixo X
    if Bola.xcor() > 390:
        Bola.goto(0,0)
        Bola.dx *= -1
        PlacarA += 1
        #Som no linux
        #os.system("afplay pop.mp3&")

    if Bola.xcor() < -390:
        Bola.goto(0,0)
        Bola.dx *= -1
        PlacarB += 1
        #Som no linux
        #os.system("afplay pop.mp3&")

    Caneta.clear()
    Caneta.write(f'Jogador A : {PlacarA}  Jogador B : {PlacarB}', align="center", font =("Courier",20, "bold"))



    # Colisão barra e bola
        #Direita
    if Bola.xcor() > 340 and Bola.xcor() < 350 and Bola.ycor() < BarraD.ycor() + 40 and Bola.ycor() > BarraD.ycor() - 40:
        Bola.setx(340)
        Bola.dx *= -1

        #Esquerda
    if Bola.xcor() < -340 and Bola.xcor() > -350 and Bola.ycor() < BarraE.ycor() + 40 and Bola.ycor() > BarraE.ycor() - 40:
        Bola.setx(-340)
        Bola.dx *= -1

