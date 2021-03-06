# Super Jogos
Projeto desenvolvido durante a matéria Pensamento Computacional, ministrada pelo professor Daniel Sabino, na UFRN. Neste projeto desenvolvemos um sistema com 3 jogos utilizando a biblioteca *turtle* e a linguagem *Python*.
>### Notas de atualização:
>* **Completo** (Part. Victor): A animação de iniciação do jogo, o menu e o Pong já estão todos integrados, bastar executar o *Principal.py*, quando o tema do menu é mudado o do jogo Pong também é.
>* **README(Completo)**: Acredito que toda descrição da minha parte do projeto esteja bem documentada, tudo pronto para ser utilizado como roteiro para o vídeo.

## Jogo da Velha

### Sobre o Jogo da Velha

O Jogo da Velha é um joguinho bem simples. Todos nós já o jagamos em algum momento das nossas vidas. Ele consiste em um tabuleiro com três linhas e três colunas. Em cada casa do tabuleiro, marcamos um X ou um O, dependendo do jogador que assumimos ao início da partida. O jogador X sempre começa jogando. Ganha o jogo quem conseguir completar uma linha, uma coluna ou uma diagonal com o seu símbolo (X ou O). Há também o caso de empate, isto é, nenhuma linha, coluna ou diagonal foi preenchida como mesmo símbolo.

### Código

Para escrever um jogo da velha em Python, foi utilizada a biblioteca gráfica Turtle. O código pode ser divido em três partes:

- Configuração inicial;
- Definições das funções;
- Execução do jogo.

Na primeira parte, importamos a biblioteca Turtle e criamos a janela de pop-up, que será a nossa tela. É nela que o jogo vai se passar e onde nós realizaremos as jogadas. Além disso, criamos algumas variáveis e lhes atribuimos alguns valores. Nessa parte, são definidas, por exemplo, quem começa jogando (no caso, X).

Em seguida, temos de definir as funções para o jogo. Verificamos que todas as etapas do jogo podem ser vistas como funções. Abaixo, relacionamos essas etapas com as suas respectivas funções.

- Quando vamos jogar um jogo da velha no papel, a primeira coisa que fazemos é riscar o tabuleiro no papel. Para isso, temos a função `DesenhaTabuleiro()` que o desenha na nossa tela assim que iniciamos o jogo.
- Quando jogamos, riscamos um X ou um O no papel. As funções responsáveis por isso são `DesenhaX(x,y)` e `DesenhaO(x,y)`. Ambas recebem `x` e `y` como parâmetros. Esses, por sua vez, são as coordenadas do nosso clique. Desse modo, é como se dissessemo à função em que lugar da nossa tela queremos desenhar um X ou um O.
- Naturalmente, abstraímos uma outra função: a função `RegistraJogada(x,y)`. Não paramos para "registrar uma jogada" no papel. Assim que riscamos o tabulueiro, a jogada já é registrada. Contudo, essa função precisa estar no código para, depois, verificarmos se houve algum vencedor. Essa função também recebe `x` e `y` como parâmetros, e se utiliza deles para saber qual foi a jogada e conferir se a jogada foi válida. Se sim, a jogada é registrada; senão a jogada não é registrada.
- Por fim, ao final do jogo, conferimos se alguém foi ganhador. Para isso, temos várias regrinhas lógicas que verificam se alguma das linhas, das colunas ou das diagonais foi totalmente preechida com o mesmo símbolo.

Uma vez definidas as nossas funções, podemos executá-las. Desenhamos o tabuleiro e chamamos um "listener" para responder a cada clique nosso, ou seja, para executar as nossas funções.

O jogo está pronto! Agora, é só jogar!

### Notas da atualização 1.1 (João Pedro):
* Consegui centralizar o "O". Estava tendo problemas com isso.
* Pesquisando, achei um [código](https://pythonturtle.academy/tic-tac-toe-source-code-included/) interessante. Parece-me simples, mas vejo que pode ser melhorado (ao meu ver). Gostei da ideia de considerar coordenadas (e não pixels) para a tela. Acho que é mais intuitivo. Mesmo assim, mudei as coordenadas: agora, a janela é um plano cartesiano com início em (0,0) e término em (5,5). Também utilizei um `for` para desenhar o tabuleiro. Como alterei as coordenadas da tela, tive também de alterar as coordenadas com base nas quais os Os e os Xs serão desenhados. Por fim, testei, parece-me que o resultado está bom.
* Resta fazer a lógica que verifica a vitória ou a derrota ou o empate
* Também restam o event listeners para desenhar os Os e os Xs quando clicarmos na casa que queremos inseri-los

### Notas da atualização 1.0 (João Pedro):
* Perdi algum tempo tentando configurar o editor de texto. O VS Code não estava funcionando bem, e o PyCharm não reconhecia as biblioteca turtle. Tentei várias soluções, mas nada deu muito certo. Minha hipótese é que isso tenha acontecido por causa do Linux talvez. Instalei o Windows, e as coisas parecem estar dando certo até agora.
* Estou me baseando em dois vídeos para fazer o Jogo da Velha: [Tutorial Introdução ao módulo Turtle de python](https://www.youtube.com/watch?v=kq1xW8JSTyU&ab_channel=Cl%C3%A9sioMatias) e [Python Coding Tutorial: Build a Tic Tac Toe Game](https://www.youtube.com/watch?v=8eHpXLDhi6w&ab_channel=JuniLearning)
* Estou estudando o código da moça ainda, e pesquisando sobre o turtle.
* Pretendo, após isso, refatorar o código, se encontrar algumas incongruências ou aspectos que podem ser melhorados.

## Pong
# Sumário
* [Contexto](##Contexto)
* [Conceitos](#Conceitos)
    * [Animação](##Animação)
    * [Menu](##Menu)
        * [Tema](###Tema)
    * [Pong](##Pong)
        * [Barra](###Barra)
        * [Bola](###Bola)
* [Referências](#Referências)
---

## Contexto
Jogos são ótimas fontes de entrenimento. Neles podemos nos divertir, nos emocionar, ver a realidade de formas que só são possíveis neles e até aprender. Além disso, um código fonte simples de um jogo pode ser uma poderosa ferramenta para auxiliar no aprendizado de determinada linguagem de programação e támbem diversos conceitos, pensando na simplicidade e no lado lúdico desta forma de arte foi criado o Super Jogos, um conjunto de 3 jogos em linguagem *python* e alguns utilizando a biblioteca *turtle*.

# Conceitos
Agora iremos descrever os conceitos mais importantes que fizeram parte de parte do projeto. Para tudo funcionar é necessário antes de tudo uma janela. Para fazer isso utilizamos os seguintes comandos.

```python
Janela = turtle.Screen()
Janela.title("Título da janela")
Janela.bgcolor("Cor do plano de fundo") #Nome da cor ou Hexadecimal (tavlez RGB?)
Janela.setup(width=Largura, height=Altura) #Númericos
while True: #Loop que mantém a janela aberta
    Janela.update()
```

## Animação
A animação ocorre assim que se inica arquivo *principal.py* , nela vemos uma tartaruguinha percorrendo a tela e por onde ela passa vai surgindo as palavras. Os conceitos mais fundamentais para compreender todo o projeto se encontram aqui. A figura abaixo demonstra como fica a janela ao final da animação.

![](Documento/ImagemIntroducao.jpg)

Nela criamos uma tartaruga com nome apresentador. E atribuímos algumas características para ele ficar com essa forma.

```python
Apresentador = turtle.Turtle()
Apresentador.shape("turtle") #Forma da tartaruga
Apresentador.color("Cor da tartaruga")
```
Observe que no método [*.shape()*](https://docs.python.org/3/library/turtle.html#turtle.shape) podemos inserir diferentes formas para ela, desde formas geométricas simples, como de um quadradro,triângulo ou círculo até transformá-la usando um arquivo .gif (o único formato que turtle aceita), olhe o exemplo abaixo de como inserimos a logo no do *IMD* no projeto.

```python
Janela.addshape('SuaImagem.gif') #A logo é adicionada as formas possíveis
Logo = turtle.Turtle()
Logo.shape('SuaImagem.gif') #A tartaruga se transforma na logo
```

Caso deseje converter um arquivo para *.gif* nas referências tem um link.

## Menu

Após a animação inicial aparece o menu nele podemos escolher qual jogo vamos iniciar, trocar o tema dos jogos entre claro ou escuro. Nessa parte sistema podemos analisar dois elementos fundamentais, a troca do tema e os botões. O segundo conceito você poderá ver na sessão **Jogo da Velha**.

![](Documento/Menu.jpg)

### Tema
Basicamente, quando o botão do tema é clicado a janela apaga tudo (botões e logo) e desenha todos os elementos com outras cores, e ao iniciarmos o jogo ele estará com o mesmo tema do menu. Observe na figura abaixo, a mudança de cores que acontece, e a da logo também.

![](Documento/Temas.jpg)

Para isso temos que compreender como o tema é armazenado, o que acontece após o botão ser pressionado, como funciona a eliminação dos elementos da tela e o reaparecimento deles. 

O amarzenamento do tema funciona de maneira simples. Observe o código abaixo que está fora do loop while que mantém o jogo aberto (ler início do tópico conceitos).

```python
Claro = ['cor de fundo', 'cor dos elementos', 'Pasta/LogoDesseTema.gif', 'Nome do tema']
Escuro = ['cor de fundo', 'cor dos elementos', 'Pasta/LogoDesseTema.gif', 'Nome do tema']
Tema = Claro
```
Após o botão se acionado uma varável muda para o nome do que deve acontecer, dentro do loop principal há essa estrutura de decisão que ao identificar que ao identificar o nome da variável irá trocar o Tema, após isso as funções *Limpar()* e *Preencher* serão acionadas.
```python
if Acao == 'Tema: Claro/Escuro':
        Acao = ''
        if Tema == Claro:
            Tema = Escuro
        elif Tema == Escuro:
            Tema = Claro
        Limpar()
        Preencher()
```

A função *Limpar()* simplesmente esconde a logo e apaga todos os botões que foram criado, nessas duas linhas.

```python
Botao.clear()
Logo.hideturtle()
```
Na função *preencher()* a logo, que estava escondida, muda para outro arquivo *gif* e depois aparece na tela na mesma posição de antes, o plano de fundo muda sua cor usando *.bgcolor('cor')*, e os botões que foram todos apagados serão desenhados novamente, antes de começar e definido da margem do botão *.pencolor('cor')* e a cor que será preenchido *.fillcolor('cor')*, apos isso começa um loop que irá desenhar todos os botões, que não cabem a discussão no momento.

```python
global CordBotoes #Variável que diz a localização dos botões
CordBotoes = []
# Logo
Logo.shape(Tema[2])
Logo.showturtle()
# Plano de fundo
Janela.bgcolor(Tema[0])
#Desenha os botões
Botao.pencolor(Tema[1])
Botao.fillcolor(Tema[1])
for Item in range(0, len(Opcoes)):
    x = Inicio[0]
    y = Inicio[1] + Inicio[2]*Item
    DesenharBotao(Botao, Opcoes[Item], x, y)
    CordBotoes.append([x, y])
```

## Pong 
 
Podemos compreender o jogo Pong da seguinte forma. Há 3 elementos, duas barras e uma bola, as barras se movem para cima ou para baixo a partir de comandos pelo teclado. A bola sempre se move na diagonal e ao bater nas bordas superiores ou inferiores ela muda o sentido no eixo *y*, quando bate nas barras ela inverte o sentido no eixo *x* , caso chega as bordas laterais um ponto é marcado para o jogador da barra que está do lado oposto.

### Barra 
o funcionamento da barra **ocorre todo fora do loop** que mantém a janela aberta. Vamos analisar como funciona a criação da barra esquerda.

```python
BarraE = turtle.Turtle() #Cria-se uma tartaruga
BarraE.speed(0) #Sem animação na movimentação
BarraE.shape("square") #Forma
BarraE.color(Tema[1]) #Cor
BarraE.shapesize(stretch_wid=5, stretch_len=1) #Muda o tamanho da forma
BarraE.penup() #Esse comando evita que a Barra desenhe enquanto se move
BarraE.goto(-350, 0) #Define posição inicial da Barra
```
Com a barra criada e posicionada precisamos colocar movimento nela. Observe abaixo que cada botão do teclado ativa uma função que vai fazer a barra se movimentar.
```python
Janela.listen() #Sempre preparada para os comandos
Janela.onkeypress(BarraESobe, "w")
Janela.onkeypress(BarraEDesce, "s")
```

Observe uma função de exemplo, basicamente ela lê a coordenada atual da barra, adiciona um valor e defini o novo *y* como esse valor.
```python
def BarraESobe():
    if BarraE.ycor() < 245: #Impede que saia da janela
        y = BarraE.ycor() #Lê a coordenada y 
        y += 20
        BarraE.sety(y) #Defini novo y
```

### Bola
A bola é um elemento que deve sempre estar sempre mudando de espaço, além disso deve colidir com as bordas horizontais e com as barras, portanto vamos destrinchar seu funcionamento. Vamos pular a parte para defini-lá pois funciona da mesma forma que a barra.
```python
def BarraESobe():
# Velocidade da bola
Velocidade = 0.3
# Movimento da bola (varia de acordo com o computador)
Bola.dx = Velocidade
Bola.dy = Velocidade 
```
O *.dx* e *.dy* definem a velocidade da bola no jogo, no caso desse jogo ela aumenta toda vez que a bola bate na barra, mas não será aqui discutido esse mecanismo. Agora vamos ver como funciona a colisão da bola com a barra.
```python
# Esquerda
if Bola.xcor() < -340 #Bola um pouco perto da barra (evita bugs)
and Bola.xcor() > -350 #Bola não passou pela barra
and Bola.ycor() < BarraE.ycor() + 60 #Bola não passou da parte supeireior da barra
and Bola.ycor() > BarraE.ycor() - 60:#Bola não passou da parte inferior da barra
    Bola.setx(-340) #Defini a posição encostada na barra (evita bugs)
    Bola.dx *= -1 #Inverte o sentido x
```
O funcionamento de como a bola colide com as bordas e como os pontos são marcados é muito semelhante ao apresentado acima.
# Referências

### Texto
[Um breve tutorial do Turtle - Português](https://medium.com/reflex%C3%A3o-computacional/m%C3%B3dulo-turtle-d8949db55008)

[Documentação do Turtle - Português](https://docs.python.org/pt-br/3/library/turtle.html#module-turtle)

### Vídeo
[Vídeo de inspiração do Pong - Inglês](https://www.youtube.com/watch?v=XGf2GcyHPhc&t=19452s&ab_channel=freeCodeCamp.org)

[Vídeo de criação de um botão com Turtle - Inglês](https://www.youtube.com/watch?v=-XiZIEcDukY&ab_channel=RounakBhowmik)
### Converter .gif
[Online Convert Free](https://onlineconvertfree.com/pt/convert-format/png-to-gif/)

[Online Convert](https://imagem.online-convert.com/pt/converter-para-gif)
