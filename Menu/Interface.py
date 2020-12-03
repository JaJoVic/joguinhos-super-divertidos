import turtle
from time import sleep
import random

#Tema (Fundo, Elementos)
Claro = ['#FCFCFC','#343536']
Escuro = ["#343536",'#FCFCFC']

Tema = Claro

# Configurações iniciais
Janela = turtle.Screen()
Janela.title("Super Jogos - @JaJoVic")
Janela.bgcolor(Tema[0]) 
Janela.setup(width=800, height = 600) 
Janela.tracer(0)


Botao = turtle.Turtle(visible = False)
Botao.pencolor(Tema[1])
Botao.fillcolor(Tema[1])

BotaoComp = 200
BotaoLarg = 50

def DesenharBotao(Botao, Mensagem="",BotaoX=0,BotaoY=0):
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
    Botao.write(Mensagem, "center",font = ('Arial', 15, 'normal'))
    Botao.pencolor(Tema[1])

def ClicarBotao(X,Y):
    BotaoX = CordBotoes[0][0]
    BotaoY = CordBotoes[0][1]
    if BotaoX <= X <= BotaoX + BotaoComp:
        if BotaoY <= Y <= BotaoY + BotaoLarg:
            print('Clicou')

#Criar botões
Opcoes = ['Pong','Sair']
Inicio = [-100,-200,100] #X, Y e distância entre a origem de cada Botão
CordBotoes = [] #Salva a coordenada inicial de cada botão a função ClicarBotao identificar
for Item in range (0,len(Opcoes)):
    x = Inicio[0]
    y = Inicio[1] + Inicio[2]*Item
    DesenharBotao(Botao,Opcoes[Item-1],x,y)
    lista = [x,y]
    CordBotoes.insert(0,[x,y])

Janela.onclick(ClicarBotao)


while True:
    Janela.update()