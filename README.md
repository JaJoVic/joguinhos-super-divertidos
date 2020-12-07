# Super Jogos

>### Notas de atualização:
>* **Completo** (Part. Victor): A animação de iniciação do jogo, o menu e o Pong já estão todos integrados, bastar executar o *Principal.py*, quando o tema do menu é mudado o do jogo Pong também é.
>* **README**: Fiz uma pequena atualização do README já preparando como uma parte do roteiro para o futuro vídeo.

# Table of Contents
1. [Resumo](##Resumo)
2. [Contexto](##Contexto)
3. [Conceitos](#Conceitos)
4. [Animação](#Animação)
5. [Referências](##Referências)

## Resumo
Projeto desenvolvido durante a matéria Pensamento Computacional, ministrada pelo professor Daniel Sabino, na UFRN. Neste projeto desenvolvemos um sistema com 3 jogos utilizando a biblioteca *turtle* e a linguagem *Python*.

## Contexto
Jogos são ótimas fontes de entrenimento. Neles podemos nos divertir, nos emocionar, ver a realidade de formas que só são possíveis neles e até aprender. Além disso, um código fonte simples de um jogo pode ser uma poderosa ferramenta para auxiliar no aprendizado de determinada linguagem de programação, pensando na simplicidade e no lado lúdico desta forma de arte foi criado o Super Jogos, um sistema desenvolvido em linguagem *python* e utilizando a biblioteca *turtle*.

# Conceitos
Agora iremos descrever os conceitos mais importantes que fizeram parte de parte do projeto. Para tudo funcionar é necessário antes de tudo uma janela. Para fazer isso utilizamos os seguintes comandos.

```python
    Janela = turtle.Screen()
    Janela.title("Título da janela")
    Janela.bgcolor("Cor do plano de fundo") #Nome da cor ou Hexadecimal (tavlez RGB?)
    Janela.setup(width=Largura, height=Altura) #Númericos
```

## Animação
A animação ocorre assim que se inica o jogo, nela vemos uma tartaruguinha percorrendo a tela e por onde ela passa vai surgindo as palavras. Os conceitos mais fundamentais para compreender todo o projeto se encontram aqui. A figura abaixo demonstra como fica a janela no final da animação.

![Imagem de Introdução](Documento\ImagemIntroducao.jpg)

Nela criamos uma tartaruga com nome apresentador. E atribuímos algumas características para ele ficar com essa forma.

```python
Apresentador = turtle.Turtle()
Apresentador.shape("turtle") #Forma da tartaruga
Apresentador.color("Cor da tartaruga")
```
Observer que no método *.shape()* podemos inserir diferentes formas para ela, como a de um arquivo .gif(é o único formato que turtle aceita), olhe o exemplo abaixo de como inserimos a logo no do *IMD* no projeto.

```python
Janela.addshape('SuaImagem.gif') #A logo é adicionada as formas possíveis
Logo = turtle.Turtle()
Logo.shape('SuaImagem.gif') #A tartaruga se transforma na logo
```

## Referências
[Um breve tutorial do Turtle - Português](https://medium.com/reflex%C3%A3o-computacional/m%C3%B3dulo-turtle-d8949db55008)

[Vídeo de inspiração do Pong - Inglês](https://www.youtube.com/watch?v=XGf2GcyHPhc&t=19452s&ab_channel=freeCodeCamp.org)

[Vídeo de criação de um botão com Turtle - Inglês](https://www.youtube.com/watch?v=-XiZIEcDukY&ab_channel=RounakBhowmik)
