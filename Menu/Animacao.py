import turtle
from time import sleep


def Intro():
    # Tema (Fundo, Elementos, Logo)
    Claro = ['#FCFCFC', '#343536', "Estilo/IMDLogoAzul.gif"]
    Tema = Claro

    # Configurações iniciais
    Janela = turtle.Screen()
    Janela.title("Super Jogos por @JaJoVic")
    Janela.bgcolor(Tema[0])
    Janela.setup(width=800, height=600)

    # Criando tartaruga que apresenta o programa
    Apresentador = turtle.Turtle()
    Apresentador.shape("turtle")
    Apresentador.color(Tema[1])
    Apresentador.speed(1)

    # Fontes utilizadas na apresentações
    Fonte1 = ("Arial", 30, "bold")
    Fonte2 = ("Arial", 15, "normal")

    # Mostra o título do jogos
    Apresentador.right(90)
    Apresentador.penup()
    Apresentador.write("Super Jogos", False, "center", Fonte1)
    Apresentador.forward(40)
    Apresentador.write("com Python", False, "center", Fonte2)
    Apresentador.forward(25)
    Apresentador.write("e turtle", False, "center", Fonte2)
    Apresentador.speed(2)
    Apresentador.forward(300)

    # Logo IMD
    Janela.addshape(Tema[2])
    Logo = turtle.Turtle(visible=False)
    Logo.penup()
    Logo.speed(10)
    Logo.setpos(0, -350)
    Logo.shape(Tema[2])
    Logo.speed(1.5)
    Logo.showturtle()
    Logo.setpos(0, -160)

    # Leva a tartaruga escondida ao canto
    Apresentador.hideturtle()
    Apresentador.speed(10)
    Apresentador.goto(-400, 150)
    Apresentador.speed(2)
    Apresentador.left(90)

    # Mostra os desenvolvedores
    Apresentador.showturtle()
    Apresentador.forward(280)
    Apresentador.speed(1)
    Apresentador.write("Desenvolvido por:", False, "right", Fonte2)
    Apresentador.forward(70)
    Apresentador.right(90)
    Apresentador.write(
        "Janiely Kelly Silva Pereira - Turma 1 ", False, "left", Fonte2)
    sleep(0.1)
    Apresentador.forward(25)
    Apresentador.write("João Pedro Fonseca Dantas - Turma 1",
                       False, "left", Fonte2)
    sleep(0.1)
    Apresentador.forward(25)
    Apresentador.write("Victor Vieira Targino - Turma 3",
                       False, "left", Fonte2)
    Apresentador.forward(10)
    sleep(1)

    while True:
        Janela.update()
        # Apagar Coisas da Tela
        Apresentador.clear()
        Apresentador.hideturtle()
        Logo.hideturtle()
        break
