# Joguinhos Divertidos

## Jogo da Velha

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

### Notas da atualização 1.2:
* Agora foi criado uma intrudução para o menu

### Notas da atualização 1.1:
* Desisti por enquanto de colocar som o no jogo.
* Bug da bola atravessar os quadrados: CORRIGIDO
* Bug da barra atravessar a borda : CORRIGIDO.
* Agora o sentido do Y e X inicial da bolinha é aleatório.
* Agora a velocidade das bolinhas aumenta toda vez que bate na barra, quando um ponto é marcado a velocidade volta à inicial. Agora o jogo está mais dinâmico.

### Notas da atualização 1.0:
* Essa primeira pasta vscode contém apenas o caminho do programa python em minha máquina, não deveria estar ai. Acho que há alguma forma de contornar esse problema (talvez criando um arquivo com o próprio python em si em uma pasta ? não sei);
* Outro problema é o áudio. A execução de cada aúdio varia nos sistemas Windows, Mac e Linux. Mas eu nem consegui colocar para rodar no meu Windows, tive alguns problemas;
* Há alguns bugs ainda, a bolinha às vezes atravessa a barrinha;
* **A velocidade varia**, dependendo da máquina a velocidade da bolinha muda não sei como ficou na máquina de vocês, mas na minha eu deixei assim os valores das variáveis que definem a velocidade. Para resolver esse problema eu pensei em talvez criarmos um local onde o jogador pode regular a velocidade padrão da bolinha.

Bola.dx = 0.3
Bola.dy = 0.3

### Referências

[Inspiração do projeto](https://www.youtube.com/watch?v=XGf2GcyHPhc&t=19452s&ab_channel=freeCodeCamp.org)

[Som pop](https://freesound.org/people/Vilkas_Sound/sounds/463395/)

[Som moeda](https://freesound.org/people/ProjectsU012/sounds/341695/)
