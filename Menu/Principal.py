import turtle
from time import sleep
import random



# Configurações iniciais
Janela = turtle.Screen()
Janela.title("Pong por @JaJoVic")
Janela.bgcolor("black") 
Janela.setup(width=800, height = 600) 

#Criando tartaruga que apresenta o programa
Apresentador = turtle.Turtle()
Apresentador.shape("turtle")
Apresentador.color("white")
Apresentador.speed(1)

#Fontes utilizadas na apresentações
Fonte1 = ("Comic Sans", 30, "bold")
Fonte2 = ("Comic Sans", 15, "normal")

#Mostra o título do jogos
Apresentador.right(90)
Apresentador.penup()
Apresentador.write("Super Jogos", False, "center", Fonte1)
Apresentador.forward(40)
Apresentador.write("com Python", False, "center", Fonte2)
Apresentador.forward(25)
Apresentador.write("e turtle", False, "center", Fonte2)
Apresentador.speed(2)
Apresentador.forward(300)

#leva a tartaruga escondida ao canto
Apresentador.hideturtle()
Apresentador.speed(10)
Apresentador.goto(-400,150)
Apresentador.speed(2)
Apresentador.left(90)

#Mostra os desenvolvedores
Apresentador.showturtle()
Apresentador.forward(280)
Apresentador.speed(1)
Apresentador.write("Desenvolvido por:", False, "right", Fonte2)
Apresentador.forward(70)
Apresentador.right(90)
Apresentador.write("Janiely Kelly Silva Pereira - Turma 1 ", False, "left", Fonte2)
sleep(0.2)
Apresentador.forward(25)
Apresentador.write("João Pedro Fonseca Dantas - Turma 1", False, "left", Fonte2)
sleep(0.2)
Apresentador.forward(25)
Apresentador.write("Victor Vieira Targino - Turma 3", False, "left", Fonte2)
Apresentador.forward(10)




#Loop Principal
while True:
    Janela.update()
