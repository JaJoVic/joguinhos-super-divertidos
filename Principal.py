import turtle
from time import sleep
from Menu import Animacao
from Pong import JogoPong
from JogoDaVelha import JogoVelha


#Tema (Fundo, Elementos)
Claro = ['#FCFCFC', '#343536', 'Estilo/IMDLogoAzul.gif', 'Claro']
Escuro = ["#343536", '#FCFCFC', 'Estilo/IMDLogoBranco.gif', 'Escuro']
Tema = Claro


# Configurações iniciais
Janela = turtle.Screen()
Janela.title("Super Jogos - @JaJoVic")
Janela.bgcolor(Tema[0])
Janela.setup(width=800, height=600)
#Animação Inicial do Jogo
Animacao.Intro()
Janela.tracer(0)

Botao = turtle.Turtle(visible=False)
Botao.pencolor(Tema[1])
Botao.fillcolor(Tema[1])

BotaoComp = 200
BotaoLarg = 50

# Logo IMD
Janela.addshape('Estilo/IMDLogoAzul.gif')
Janela.addshape('Estilo/IMDLogoBranco.gif')
Logo = turtle.Turtle()
Logo.penup()
Logo.sety(200)
Logo.shape(Tema[2])


def DesenharBotao(Botao, Mensagem="", BotaoX=0, BotaoY=0):
    Botao.penup()
    Botao.begin_fill()
    Botao.goto(BotaoX, BotaoY)
    Botao.goto(BotaoX + BotaoComp, BotaoY)
    Botao.goto(BotaoX + BotaoComp, BotaoY + BotaoLarg)
    Botao.goto(BotaoX, BotaoY + BotaoLarg)
    Botao.goto(BotaoX, BotaoY)
    Botao.end_fill()
    Botao.goto(BotaoX + 75, BotaoY + 15)
    Botao.pencolor(Tema[0])
    if Mensagem == 'Tema: Claro/Escuro' or Mensagem == 'Jogo da Velha':
        Botao.goto(BotaoX + 15, BotaoY + 15)
        Botao.write(Mensagem, "left", font=('Arial', 15, 'normal'))
    else:
        Botao.write(Mensagem, "center", font=('Arial', 15, 'normal'))
    Botao.pencolor(Tema[1])


# Varável que Determinar ação que o botão que o usário clicou.
Acao = ''


def ClicarBotao(X, Y):
    for C in range(0, len(CordBotoes)):
        BotaoX = CordBotoes[C][0]
        BotaoY = CordBotoes[C][1]
        if BotaoX <= X <= BotaoX + BotaoComp:
            if BotaoY <= Y <= BotaoY + BotaoLarg:
                global Acao
                Acao = Opcoes[C]


# Criar botões
Opcoes = ['Tema: Claro/Escuro', 'Pong', 'Jogo da Velha', 'Sair']  # Nome dos botões
Inicio = [-100, 50, -75]  # X, Y e distância entre a origem de cada Botão
CordBotoes = []  # Salva a coordenada inicial de cada botão a função ClicarBotao identificar

for Item in range(0, len(Opcoes)):
    x = Inicio[0]
    y = Inicio[1] + Inicio[2]*Item
    DesenharBotao(Botao, Opcoes[Item], x, y)
    CordBotoes.append([x, y])


def Limpar():
    Botao.clear()
    Logo.hideturtle()
    Janela.clearscreen()



def Preencher():
    global Botao
    global BotaoComp
    global BotaoLarg
    global Janela
    global Logo
        # Configurações iniciais
    Janela = turtle.Screen()
    Janela.title("Super Jogos - @JaJoVic")
    Janela.bgcolor(Tema[0])
    Janela.setup(width=800, height=600)
    #Animação Inicial do Jogo
    Janela.tracer(0)
    
    Botao = turtle.Turtle(visible=False)
    Botao.pencolor(Tema[1])
    Botao.fillcolor(Tema[1])

    BotaoComp = 200
    BotaoLarg = 50

    # Logo IMD
    Janela.addshape('Estilo/IMDLogoAzul.gif')
    Janela.addshape('Estilo/IMDLogoBranco.gif')
    Logo = turtle.Turtle()
    Logo.penup()
    Logo.sety(200)
    Logo.shape(Tema[2])
    global CordBotoes
    CordBotoes = []
    Logo.shape(Tema[2])
    Logo.showturtle()
    Janela.bgcolor(Tema[0])
    Botao.pencolor(Tema[1])
    Botao.fillcolor(Tema[1])
    for Item in range(0, len(Opcoes)):
        x = Inicio[0]
        y = Inicio[1] + Inicio[2]*Item
        DesenharBotao(Botao, Opcoes[Item], x, y)
        CordBotoes.append([x, y])


while True:
    Janela.update()
    if Acao == 'Sair':
        Acao = ''
        break
    if Acao == 'Pong':
        Limpar()
        JogoPong.IniciarPong(Tema[3])
        Preencher()
        Acao = ''
    if Acao == 'Tema: Claro/Escuro':
        Acao = ''
        if Tema == Claro:
            Tema = Escuro
        elif Tema == Escuro:
            Tema = Claro
        Limpar()
        Preencher()
    if Acao == 'Jogo da Velha':
        Limpar()
        JogoVelha.IniciarVelha(Tema[3])
        break
        #Preencher()
        #Acao = ''
    Janela.onclick(ClicarBotao)
