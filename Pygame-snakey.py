# Snakey (A Nibbles Clone)
# http://inventwithpython.com/blog
# By Al Sweigart al@inventwithpython.com
# Creative Commons BY-NC-SA license
# 158 lines of code


"""
Welcome to the Code Comments for Snakey. Code Comments is a series of simple games with detailed comments in the source code, so you can see how the game works.
Bem vindo aos Códigos Comentados para Snakey. Códigos Comentados é uma série de games(jogos) simples com comentários detalhados no código fonte, assim você pode ver como o game(jogo) trabalha.

The text in between the triple-double-quotes are comments. The Python interpreter ignores any text in between them, so we can add any comments about the source code without affecting the program. In general for Code Comments, the comments will describe the lines of code above the comment. It helps to view this file either on the Code Comments site or with a text editor that does "syntax highlighting", so that the comments appear in a separate color and are easier to distinguish from the code.
O texto entre aspas duplas-triplas são comentários. O interpretador do Python ignora qualquer texto entre elas, assim nós podemos adicionar qualquer comentário sobre o código fonte sem afetar o programa. Em geral nos Códigos Comentados, os comentários descreverão as linhas do código acima do comentário. Isto irá ajudá-lo a visualizar este arquivo no site Code Comments ou com um editor de texto que destaca a sintaxe, de modo que os comentários aparecem em uma cor diferente e são fáceis de distinguí-los do código.

This Code Comments assumes you know some basic Python programming. If you are a beginner and would like to learn computer programming, there is a free book online called "Invent Your Own Computer Games with Python" at http://inventwithpython.com
Estes Códigos Comentados assumem que você tenha algum conhecimento básico sobre a linguagem Python. Se você é um iniciante e gostaria de aprender programação de computadores, existe um livro grátis(free) online chamado "Invent Your Own Computer Games with Python" disponível no site http://inventwithpython.com

The Code Comments programs make references to sections of this book throughout the program. This Code Comments can also teach you how to use the Pygame library to make your own games with graphics, animation, and sound. You can download Pygame from http://pygame.org and view its documentation at http://pygame.org/docs/
Os programas dos Códigos Comentados fazem referência à seções deste livro em todo o programa. Os Códigos Comentados também podem te ensinar  a como usar a biblioteca Pygame para fazer seus próprios games com gráficos, animações e sons. Você pode fazer o download do Pygame no site: http://pygame.org e visualizar sua documentação em: http://pygame.org/docs/

HOW TO PLAY SNAKEY:
COMO JOGAR SNAKEY:
You are the green snake on the screen. Use the arrow keys or the WASD keys to move the snake around and eat the red apples that are on the screen. Each time you eat an apply, your snake grows in length. Do not run into either the edges or yourself.
Você é a cobra verde na tela. Use as teclas de setas ou as teclas WASD para mover a cobra e comer as maçãs vermelhas que estão na tela. Cada vez que você comer uma maçã, sua cobra aumenta de tamanho. Não execute nas bordas e nem sobre si mesmo.

"""
import random
import time
import pygame
import sys
from pygame.locals import *
"""Here we import modules that our game needs. random has random number functions, time has the sleep() function, sys has the exit() function, and pygame contains all the pygame-related functions.
Aqui nós importamos módulos que nosso game precisa. "random" tem funções de números aleatórios, "time" tem a função sleep(), "sys" tem a função exit() e "pygame" contém todas as funções relacionadas ao paygame.

pygame.locals contains constants like MOUSEMOTION and MOUSEBUTTONUP and QUIT for the events. It's easier to type MOUSEBUTTONUP instead of pygame.locals.MOUSEBUTTONUP, so we use the "from pygame.locals import *" format to import these to the local namespace.
pygame.locals contém constantes como MOUSEMOTION e MOUSEBUTTONUP e QUIT para os eventos. É mais fácil digitar  MOUSEBUTTONUP em vez de pygame.locals.MOUSEBUTTONUP, assim usamos o formato "from pygame.locals import *" para importar estes para o local namespace.

"""

FPS = 5
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)
"""These constant variables (the uppercase names means we shouldn't change the values stored in them) set some standard values for our game. You can play around with different values for them (though some values might cause bugs in the game.) By using constants instead of the values directly, it is easier to make changes since we only have to change them in one place.
Estas variáveis constantes (os nomes em letras maiúsculas significa que não podemos mudar o valor armazenado nelas) definem alguns valores padrão para o nosso jogo. Você pode jogar com valores diferentes pra eles (no entanto alguns valores podem causar erros no jogo). Usando constantes ao invés dos valores diretamente, é mais fácil fazar mudanças e então somente temos que mudá-las em um lugar.

For example, if we used 20 instead of CELLSIZE, then if we wanted to change our code later we'd have to change every place in the code we find 20. This is trickier than just changing the one line where CELLSIZE is originally set.
Por exemplo, se usamos 20 ao invés de CELLSIZE, então se quisermos mudar nosso código depois, teremos que mudar todos os lugares no código onde encontramos 20. Isto é muito mais dificil do que mudar somente uma linha onde CELLSIZE está originalmente definida.

Note that WINDOWWIDTH and WINDOWHEIGHT refer to the width and height of the game window in pixels. We'll further divide up the window into "cells", which are areas that each segment of the snake and the apple can exist in. The window will be CELLWIDTH cells in width and CELLHEIGHT cells in height, with each CELLSIZE set to 20 pixels.
Note que WINDOWWIDTH e WINDOWHEIGHT se referem a largura e a altura da janela do jogo, em pixels. Dividiremos ainda mais a janela em "celulas", que são áreas que podem existir dentro cada segmento da cobra e da maçã.  A janela terá CELLWIDTH células na largura e CELLHEIGHT células na altura, com cada CELLSIZE definida como 20 pixels.

More information about constants is at http://inventwithpython.com/chapter9.html#ConstantVariables
Mais informação sobre as constantes podem ser obtidas em: http://inventwithpython.com/chapter9.html#ConstantVariables
"""

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
DARKGRAY = (40, 40, 40)

BGCOLOR = BLACK
"""We also set up some constant values for different colors. Pygame uses tuples of three integers to represent color. The integers represent the amount of red, green, and blue in the color (this is commonly called a RGB). 0 means there is none of the primary color in the color, and 255 means there is the maximum amount. So (255, 0, 0) is red, since it has the maximum amount of red but no green or blue. But (255, 0, 255) adds the max amount of blue with the red, creating purple.
Também podemos definir algumas valores constantes para diferentes cores. Pygame usa tuplas de 3 inteiros para representar a cor. Os inteiros representam a quantidade de vermelho, verde e azul na cor (isto é comumente chamado RGB). 0 significa que não existe nada de cor primária na cor e 255 significa que existe uma quantidade máxima. Assim, (255, 0, 0) é vermelho, já que ele tem a quantidade máxima de vermelho e não tem nada de verde ou azul. Mas, (255, 0, 255) adiciona a quantidade máxima de azul com vermelho, criando a cor pupura.

More information about colors is at http://inventwithpython.com/chapter17.html#ColorsinPygame
Mais informação sobre cores está disponível em: http://inventwithpython.com/chapter17.html#ColorsinPygame
"""

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

"""We need values for each of the directions up, down, left, and right in our program. These can be any four distinct values, as long as they are used consistently it won't matter to our program. We could use the strings 'up', 'down', etc. Instead, we'll use constant variables.
Precisamos de valores para cada direção acima, abaixo, esquerda e direita em nosso programa. Estes podem ser quaisquer quatro valores diferente, enquanto eles forem utilizados de forma consistente não causará problemas para nosso programa. Poderiamos usar as strings 'up','down', etc. Mas, em vez disso usaremos variáveis constantes.

The difference is if we make a typo using the strings, Python won't crash but it will still cause a bug. For instance, if we had this bit of code:
    if direction == 'dwon':
A diferença é que se cometermos um erro de digitação usando uma string, Python não vai parar a execução, mas seguirá com o erro. Por exemplo, se temos este bit de código:
if direction == 'dwon':

...então o programa continuará executando, mas contém um erro porque se a variável direção foi definida como 'down', esta condição vai ser avaliada como False (que não é como queremos que o código se comporte).
...then the program will still run, but it would contain a bug because if the direction variable was set to 'down', this condition would still evaluate to False (which is not how we'd want the code to behave).

But if we use constant values instead and make a similar typo:
    if direction == DWON:
Mas se em vez disso usarmos valores constantes e cometermos um erro similar de digitação:
    if direction == DWON:

... então o Python falha quando se depara com esta linha porque não há variavel definida como DWON, mas somente como DOWN. Porque está falha é uma coisa boa? Bem, não é, mas neste caso seria o de imediatamente alertar-nos que há um problema e nós poderíamos consertá-lo. Se tivessemos usado uma string ao invés disso, isto poderia demorar algum tempo até descobrirmos onde estava a causa do erro. Usando constantes desta maneira, nos ajudará a garantir que nosso programa trabalhe corretamente.
...then Python crashes when it comes across this line because there is no such variable as DWON, just DOWN. Why is crashing a good thing? Well, it's not, but in this case it would immediately alert us that there is a problem, and we could fix it. If we had used a string instead, it might take a while to track down where the bug is caused. Using constants in this way helps us ensure that our program works correctly.
"""

def main():
    global MAINCLOCK, MAINSURF, BASICFONT
    """The main() function is where our program begins. (See the last two lines of code to see why.) Normally, because we define MAINCLOCK and MAINSURF and BASICFONT inside this function, these are local variables to the main() function and the names MAINCLOCK and MAINSURF and BASICFONT won't exist outside of this function. By using a global statement, we can tell Python that we want these variables to be global variables.
    A função main() é onde nosso programa começa. (Veja as duas últimas linhas do código para entender o porque). Normalmente, porque definimos MAINCLOCK e MAINSURF  e BASICFONT dentro desta função, elas são variáveis locais a função main() e os nomes MAINCLOCK e MAINSURF e BASICFONT não existem fora desta função. Ao usar uma declaração global, podemos dizer ao Python que queremos que estas variáveis sejam variáveis globais.
    
    More information about global and local variables is at http://inventwithpython.com/chapter6.html#VariableScope
    Mais informação sobre variáveis locais e globais em :  http://inventwithpython.com/chapter6.html#VariableScope
    """

    pygame.init()
    MAINCLOCK = pygame.time.Clock()
    MAINSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Snakey')
    """pygame.init() needs to be called before any of the other Pygame functions.
    pygame.init() precisa ser chamado antes de qualquer outra função Pygame.
    
    pygame.time.Clock() returns a pygame.Clock object. We will use this object's tick() method to ensure that the program runs at no faster than 15 frames per second (or whatever integer value we have in the FPS constant.)
    pygame.time.Clock() retorna o objeto pygame.Clock. Usaremos este objeto no metodo tick() para garantir que o programa não seja executado em mais de 15 frames por segundo (ou qualquer outro valor inteiro que temos no FPS constante.)
    
    pygame.display.set_mode() creates the window on the screen and returns a pygame.Surface object. Any drawing done on this Surface object with the pygame.draw.* functions will be displayed on the screen when we call pygame.display.update().
    pygame.display.set_mode() cria a janela na tela e retorna um objeto pygame.Surface. Todo o desenho feito sobre a superfície deste objeto com as funções pygame.draw.* serão mostradas na tela quando chamamos pygame.display.update().
        
    More information about pygame.display.set_mode() is at http://inventwithpython.com/chapter17.html#ThepygamedisplaysetmodeandpygamedisplaysetcaptionFunctions
    Mais informação sobre pygame.display.set_mode() está em: http://inventwithpython.com/chapter17.html#ThepygamedisplaysetmodeandpygamedisplaysetcaptionFunctions

    The call to the pygame.font.Font() constructor function creates a Font object. We will store this Font object in the global variable BASICFONT.
    A chamada a função pygame.font.Font() cria um obejto Font. Amazenaremos este objeto Font na variável global BASICFONT."""
    
    showStartScreen()
    while True:
        gameLoop()
        showGameOverScreen()
    """The animation of the rotating "Snakey!" text is handling inside the showStartScreen() function and will be explained later. After the call to showStartScreen() returns, we enter an infinite loop where the main part of the game is run (in the gameLoop() function) and then the "game over" screen is show (in the showGameOverScreen() function) when the game ends. Because this loop keeps looping, the game starts again after the showGameOverScreen() is done.
       A animação do texto da "Snakey! (cobra)" giratória é manipulado dentro da função showStartScreen() e explicaremos mais tarde. Após a chamada a showStartScreen() retornar, entramos em um laço (loop) infinito, onde a parte principal do jogo é executada (na função gameLoop()) e então a tela "game over" é mostrada (na função showGameOverScreen()) quando o jogo termina. Por causa desse laço manter o looping, o jogo inicia denovo depois da showGameOverScreen() estar pronta."""

def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    """There are six steps to making text display on the screen in Pygame. The first is to create a pygame.font.Font object (which we will just call a Font object for short). In this case, we create a Font object from the "freesansbold.ttf" font file (this font comes with Pygame) and we want the size of the Font to be at 100 points.
    Existem seis passos para fazer a exibição de texto sobre a tela no Pygame. O primeito é criar um objeto pygame.font.Font (que só será chamado objeto Font em resumo). Neste caso, criamos um objeto Font a partir do arquivo fonte "freesansbold.ttf" (esta fonte vem com Pygame) e queremos que tamanho da fonte seja 100 pontos.
    
    If you want to draw text in other fonts or sizes, you must create a new Font object for each one.
    Se você deseja desenhar um texto em outras fontes ou tamanhos, você deve criar um novo objeto Font para cada um"""

    titleSurf1 = titleFont.render('Snakey!', True, WHITE, DARKGREEN)
    titleSurf2 = titleFont.render('Snakey!', True, GREEN)
    pressKeySurf = BASICFONT.render('Press a key to start.', True, DARKGRAY)
    """The second step is to call the Font object's render() method, which will return a Surface object with the text drawn on it. The fourth parameter provides the background color on the Surface. If you don't provide this fourth parameter, then the Surface object will have a transparent background.
    O segundo passo é chamar o objeto Font método render(), que retornará um objeto superfície com um texto desenhado sobre ela. O quarto parâmetro fornece a cor de fundo na superficie. Se vc não fornecer este quarto parametro, o objeto superfície terá um fundo transparente.
    
    There is more info on anti-aliasing at http://inventwithpython.com/chapter17.html#TherenderMethodforFontObjects
    Existem mais informações sobre o anti-aliasing em: http://inventwithpython.com/chapter17.html#TherenderMethodforFontObjects
    
    Remember that the font size information is already stored in the pygame.font object stored in our global variable named FONT.
    Lembrando que a informação sobre o tamanho da fonte está armazenada no objeto pygame.font armazenado em nossa variável global chamada FONT.
    """

    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    """The third step is to get a Rect object from the Surface object, so we can set the position of the text on the screen. The Surface object's get_rect() method will return a Rect object for the surface with the text on it.
    O terceiro passo é pegar um objeto Rect a partir do objeto Surface, assim definimos a posição do texto sobre a tela. O objeto Surface get_rect() retornará um objeto Rect para a superfície com o texto sobre ela.
    
    The fourth step is to set the position of the text. You can see the above two lines are getting the Rect object for the "Press a key to start." and then setting the topleft corner of the Rect to an x coordinate of WINDOWWIDTH - 200 (that is, 200 pixels to the left of the window's right edge (since the window is WINDOWWIDTH pixels long)), and a y coordinate of WINDOWHEIGHT - 30.
    O quarto passo é definir a posição do texto. Você pode ver acima duas linhas estão recebendo o objeto Rect para a "Press a Key to start."  e então definindo o canto superior esquerdo do Rect em uma coordenada x de WINDOWWIDTH - 200 (isto é, 200 pixels a esquerda da janela do lado direito (já que a janela é  WINDOWWIDTH pixels)), e um coordenada y de WINDOWHEIGHT - 30.
    
    The fifth step is to draw the Surface object containing the text at the position on the screen specified by the Rect object with the blit() method. The sixth step is to call pygame.display.update(). These are done a few lines down.
    O quinto passo é desenhar o objeto superfície contendo o texto na posição sobre a tela especificada pelo objeto Rect com o método blit(). O sexto passo é chamar pygame.display.update(). Estes são feitos em poucas alinhas abaixo.
    """

    degrees1 = 0
    degrees2 = 0
    while True:
        """To achieve the rotating "Snakey!" animation in the game's start menu, we will take the Surface objects stored in titleSurf1 and titleSurf2, and create rotated images of them (which will be stored in Surface objects in the rotatedSurf1 and rotatedSurf2 variables). We will rotate them at larger and larger amounts of rotation each time we draw them on the screen, so it looks like they're spinning around until they circle all the way aroud.
        Para conseguir a animação do giro "Snakey" no menu iniciar (start)do jogo, pegaremos o objeto Superfície armazenado no "titleSurf1" e "titleSurf2" e criamos imagens rotacionadas deles (que serão armazenados no objeto Superfície nas variáveis rotatedSurf1 e rotateSurf2). Vamos rodá-los em quantidades cada vez maiores de rotação cada vez que desenhá-los sobre a tela, assim, parece que eles estão girando em torno do círculo em toda a volta.
        
        The degrees1 and degrees2 will track how many degrees we rotate the two pieces of text.
        Os "degrees1" e "degrees2" irão controlar quantos graus rotacionamos as duas partes do texto."""
        
        MAINSURF.fill(BGCOLOR)
        """To wipe out the previous screen, first we fill MAINSURF will the background color we stored in BGCOLOR. Remember, the Surface object stored in MAINSURF is special because it was the Surface object returned by pygame.display.set_mode(), which means that what is drawn on this Surface object will appear on the screen when the pygame.display.update() function is called. All the other Surface objects just exist in the computer's memory and won't be displayed on the screen unless they are copied to MAINSURF with the blit() method.
        Para apagar a tela anterior, primeiro temos que preencher MAINSURF (superficie principal) com a cor de fundo que foi armazenada em BGCOLOR. Lembrando que, o objeto Superfície armazenado em MAINSURF é especial porque ele era a o objeto Surface retornado pelo pygame.display.set_mode(), que significa que o que está desenhado sobre este objeto Superficie aparecerá sobre a tela quando a função pygame.display.update() é chamada. Todos os outros objetos Superficie somente existem na memória do computador e não serão exibidos na tela a menos que sejam copiados para MAINSURF com o método blit().
        """

        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        """Creating a new rotated surface from another surface object is easy to do. Just call the pygame.transform.rotate() function, passing the Surface object you want to get a rotated Surface object of for the first parameter (like we do with titleSurf1 above), and then pass an integer of how many degrees you want it rotated.
        Criar uma nova superfície rotacionada a partir de um objeto superficie é facil de fazer. Somente chama-se a função pygame.transform.rotate(), passa-se o objeto superfície que vc quer  pegar o obejto superficie rotacionado para o primeiro parâmetro (como fizemos acima com titleSurf1), e então passa-se um inteiro com quantos graus você quer que seja rotacionado.
        
        There are 360 degrees in one full rotation, and in Pygame a positive integer for rotating will rotate the image counterclockwise, and a negative integer will rotate the image clockwise.
        Existem 360 graus em uma rotação completa, e no Pygame um inteiro positivo rotacionará a imagem no sentido anti-horário e um inteiro negativo rotacionará a imagem no sentido horário.

        Note that the original Surface object stored in the titleSurf1 is not rotated, but rather a copy of titleSurf1 is made and returned by pygame.transform.rotate() and it is that Surface object that is rotated.
        Note que o objeto Superficie original armazenado no titleSurf1 não é rotacionado, mas sim uma cópia de titleSurf1 é feita e retornada pelo pygame.transform.rotate() e é este objeto Superficie que é rotacionado """
        

        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        """Now (just like the third and fourth step we took with pressKeySurf above), we want to get a Rect object from the Surface object in rotatedSurf1 so we can position it.
        Agora (assim como a terceira e quarta etapa pegamos com pressKeySurf), desejamos obter um objeto Rect a partir do objeto Superfície, em rotatedSurf1 para que possamos posicioná-lo. """

        MAINSURF.blit(rotatedSurf1, rotatedRect1)
        """Here is the fifth step in getting text to appear on the screen: calling the Surface object's blit() method (in this case, the Surface object is the one in MAINSURF) so that we can copy the rotated surface to MAINSURF.
         Aqui é a quinta etapa na obtençao do texto que aparece na tela: chamando o objeto superficie pelo metodo blit() (neste caso, o objeto Superficie é um em MAINSURF) de modo que podemos copiar a superficie rotacionada para MAINSURF. """
        

        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        MAINSURF.blit(rotatedSurf2, rotatedRect2)
        """Here we do the same rotate/get the Rect/set the position/blit to MAINSURF steps with titleSurf2.
           Aqui fazemos o mesmo rotate/get o Rect/set a position/blit para os passos MAINSURF com titleSurf2. """

        MAINSURF.blit(pressKeySurf, pressKeyRect)
        """We'll also blit the "Press a key to start." text to the screen. """

        if checkForKeyPress():
            return
        """Rememeber that this code is currently in an infinite loop, and will repeat until the program execution reaches a break or return statement. Here, we call our checkForKeyPress() function (which we will define later) to see if the user has pressed any key. If this function returns True, then we execute a return statement and break out of showStartScreen().
           Lembrando que este código está em um loop infinito e repetirá até que a execução do programa chega a uma ruptura ou instrução de retorno. Aqui, chamamos nossa função checkForKeyPress() (que definiremos mais tarde) para ver se o usuário  tem pressionado qualquer tecla. Se esta função retorna True, então executa um instrução de retorno e sai da showStartScree(). """
        

        pygame.display.update()
        MAINCLOCK.tick(FPS)
        """The call to pygame.display.update() takes everything drawn on the MAINSURF surface and draws it on the screen. The call to MAINCLOCK.tick() will then cause the program to wait for a fraction of a second. If we didn't have this call, then the program would draw frames of this animation as fast as possible. This means our game would run very fast on fast computers, and very slow on slow computers.
           A chamada a pygame.display.update() pega tudo desenhado na superficie MAINSURF e desenha na tela. A chamada a MAINCLOCK.tick() vai fazer o programa aguardar por uma fração de segundo. Se não temos esta chamada, em seguida o programa desenhará quadros de animação o mais rápido possível. Isto significa que nosso jogo seria executado muito rápido em computadores mais rápidos e muito lento em computadores lentos."""
        

        degrees1 += 3
        degrees2 += 7
        if degrees1 > 360:
            degrees1 -= 360
        if degrees2 > 360:
            degrees2 -= 360
        """For the next frame of animation, we want to rotate the two "Snakey!" pieces of text at different rates. So we increase degrees1 by 3 while we increase degrees2 by 7. Just to ensure that these values don't get too large, if they get above 360 we will subtract 360 from them.
           Para o próximo quadro de animação, desejamos rotacionar duas "cobras" (Snakey!) e peças do texto em diferentes taxas. Assim, aumentamos o (degree1) grau1 por 3, enquanto aumentamos o (degree2) grau2 por 7. Somente para garantir que estes valores não vão ficar muito grandes, se ficar acima de 360 subtrairemos 360 deles."""


def checkForKeyPress():
    """This function will look at the event queue for any key press events and return the first one it finds. It also checks if the program is trying to quit, in which case, it calls terminate() to end the program.
       Esta função olhará na fila de eventos para todos os eventos teclados e retornará o primeiro que encontrar. Ele também checa se o programa está tentando parar, nesse caso, ele chama terminate() para terminar o programa.
       
    You can also call this function and ignore the return value if you just want to pause the program until the user presses a key.
    Vc também pode chamar esta função e ignorar o valor de retorno se vc apenas deseja pausar o programa até o usuário pressionar uma tecla"""
    for event in pygame.event.get(QUIT):
        terminate()

    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        return event.key


def terminate():
    """In order to terminate the program, we must call both pygame.quit() (to shut down the Pygame engine) and sys.exit() (to shut down the program.) Calling sys.exit() without calling pygame.quit() first probably won't harm anything, though it does give IDLE some problems if the user runs this program from it. It's just considered a graceful way to shut down the Pygame library.
    Com o objetivo de terminar o programa, devemos chamar ambos pygame.quit() (para desligar o mecanismo Pygame) e sys.exit() (para desligar o programa). Chamar sys.exit() sem primeiro chamar pygame.quit() provavelmente não vai prejudicar nada, embora ele dê alguns problemas IDLE se o usuário executar este programa a partir dele. É apenas considerada uma maneira mais bonita de encerrar a biblioteca Pygame. """
    pygame.quit()
    sys.exit()


def gameLoop():
    """This is where the main part of the game takes place. We have an infinite loop (the "while True:" loop) that handles player input, updating the state of the game world, and displaying the game world on the screen. The part before the infinite loop sets up variables for the start of a game. When the game is over, we return from this function.
       Esta é onde a parte principal do jogo ocorre. Temos um loop infinito (the "while True:" loop) que manipula a entrada do jogador, atualizando o estado do mundo do jogo e mostrando o mundo do jogo na tela.  A parte anterior ao loop infinto define variáveis para o inicio do jogo. Quando o jogo acaba, retornamos para esta função """
    
    startx = random.randint(5, CELLWIDTH - 6)
    starty = random.randint(5, CELLHEIGHT - 6)
    snakeCoords = [(startx, starty), (startx-1, starty)]
    """The data structure that we will use to keep track of the snake is a list of tuples of two integers. Each tuple represents one segment of the snake. The two integers represent the x & y coordinates of the snake segment. The snake starts off with two segments at a random location.
       A estrutura de dados que usaremos para controlar a cobra é uma lista de tuplas com dois inteiros. Cada tupla representa um segmento da cobra. Os dois inteiros representam as coordenadas x e y do segmento da cobra. A cobra começa dois segmentos em uma localização aleatória. """

    direction = RIGHT
    """At the start of the game, we'll just have the snake be going to the RIGHT.
       No começo do jogo, teremos a cobra indo para a direita."""

    apple = (random.randint(0, CELLWIDTH - 1), random.randint(0, CELLHEIGHT - 1))
    """We'll start the first apple off at a random location on the screen.
      Começaremos a prmeira maça em uma localização aleatória na tela. """

    while True:
        # get player input
        for event in pygame.event.get():
            """Here we loop through all the events in the event queue. The pygame.event.get() function will return a list of pygame.event.Event objects that have been generated since the last time pygame.event.get() was called. An Event object is generated whenever the player presses a key, clicks the mouse, tries to shut down the program, move sthe mouse, and many other situations.
            Aqui vamos percorrer todos os eventos na fila de eventos. A função pygame.event.get() retornará uma lista de objetos pygame.event.Event que foram gerados desde a última vez que pygame.event.get() foi chamado. Um objeto Event é gerado sempre que o jogador pressiona uma tecla, clica o mouse, tenta encerrar o programa, move o mouse e em muitas outras situações.

            More info on events can be found here: http://inventwithpython.com/chapter18.html#EventsandHandlingtheKEYDOWNEvent
            Mais informações sobre eventos podem ser encontrados aqui: http://inventwithpython.com/chapter18.html#EventsandHandlingtheKEYDOWNEvent
            """

            if event.type == QUIT:
                """The QUIT event is created when the user tries to shut down the program by clicking the X in the top right corner, or by killing the program from the task manager or some other means. Note that QUIT comes from pygame.locals.QUIT, but we can simply type QUIT because we used "from pygame.locals import *" instead of "import pygame.locals". The same applies for MOUSEMOTION, MOUSEBUTTONUP, KEYDOWN, and the keyboard constants such as K_ESCAPE and K_8 since these values are also in pygame.locals.
                   O evento QUIT é criado quando o usuário tenta fechar o programa clicando no X no canto superior direito ou matando o programa pelo gerenciador de tarefas ou outros meios. Note que QUIT vem de pygame.locals.QUIT, mas podemos simplismente digitar QUIT porque usamos "from pygame.locals import *" ao invés de "import pygame.locals". O mesmo se aplica para MOUSEMOTION, MOUSEBUTTONUP, KEYDOWN, e as constantes do teclado tais como K_ESCAPE e K_8 já que esses valores também estão no pygame.locals. """
                terminate()
            elif event.type == KEYDOWN:
                """The KEYDOWN event is created when the user presses any key on the keyboard. We can tell which key the user pressed by looking at the value in event.key
                O evento KEYDOWN é criado quando o usuario pressiona qualquer tecla do teclado. Podemos dizer que o usuário pressiona a tecla olhando para o valor no event.key
                By pressing one of the keys, we will change the value in the direction variable so that the snake heads in a new direction. The player can either use the arrow keys (whose value in Pygame is represented by Pygame's K_LEFT and K_DOWN (etc) constants), or by using the WASD keys (which are for up, left, down, and right respectively.) We use Pygame's K_a and K_w (etc) constants for those keys.
                Ao pressionar uma das teclas, mudaremos o valor da variável direção de modo que a cabeça da cobra terá uma nova direção. O jogador pode ou usar as teclas de setas (cujos valores no Pygame é representado por constantes Pygame's K_LEFT e K_DOWN (etc)), ou usando as teclas WASD (que são para acima, esquerda, abaixo e direita respectivamente.) Usamos constantes Pygame's K_a e K_w (etc) para aquelas teclas.
                                
                Also note that we don't want the snake to be able to turn in on itself and end the game. So if the snake is going right but the player pushes the left arrow key, we don't want to change the value in the direction variable.
                Note que não desejamos que a cobra seja capaz de transformar a si mesma e terminar o jogo. Então, se a cobra está indo para a direita mas o jogador tecla a seta para a esquerda, não queremos mudar o valor na variavel de direção."""
                
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                if (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                if (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                if (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                if event.key == K_ESCAPE:
                    """If the player pushes the Esc key, then we want to terminate the program.
                       Se o jogador tecla a tecla Esc, então deseja terminar o programa."""
                    terminate()

        # check if the snake has hit itself or the edge
        if snakeCoords[0][0] == -1 or snakeCoords[0][0] == CELLWIDTH or snakeCoords[0][1] == -1 or snakeCoords[0][1] == CELLHEIGHT:
            """The condition in this if statement checks if the head of the snake (which will always be the tuple in snakeCoords[0]) has gone past the edge. If does this by checking if the head's x coordinate (which is at snakeCoords[0][0]) has a value of -1 or CELLWIDTH or if the head's y coordinate (which is at snakeCoords[0][1]) has a value of -1 or CELLHEIGHT.
            A condição nesta declaração "if" checa se a cabeça da cobra (que será sempre a tupla em snakeCoords[0]) foi além da borda. Se faz isso verificando se a coordenada x  da cabeça (que está em snakeCoords[0][0]) tem valor de -1 ou CELLWIDTH ou se a coordenada y da cabeça (que está em snakeCoords[0][1]) tem o valor -1 ou CELLHEIGHT.
            
            The reason we check if the coordinate is at CELLWIDTH or CELLHEIGHT instead of CELLWIDTH+1 or CELLHEIGHT+1 is because the cells on the window start at 0, not at 1. Say if CELLWIDTH was 32. This means the cells go from 0 to 31, not 1 to 32. So the cell x coordinate 32 would be the one just past the right edge of the screen.
            A razão para checarmos se a coordenada está em CELLWIDTH ou CELLHEIGHT em vez de CELLWIDTH+1 ou CELLHEIGHT+1 é porque as células sobre a janela começam em 0 e não em 1. Dizemos que se CELLWIDTH foi 32. Isto significa que as celulas vão de 0 a 31, não de 0 a 30. Assim a célula x, coordenada 32 seria um pouco além da borda direita da tela.  """
            return
        for snakeBody in snakeCoords[1:]:
            """In this for loop, we check if the snake's head (snakeCoords[0]) is in the same location as any of the other segments of the snake. This will tell us if the snake has crashed into itself or not.
               Neste loop "for", checamos se a cabeça da cobra (snakeCoords[0]) está na mesma localização que todos os outros segmentos da cobra. Isto vai nos dizer se a cobra colidiu consigo mesma ou não. 

            So this for loop will loop over each tuple in snakeCoords except for the first one. This is because we are using snakeCoords[1:], which means the list of values in the list starting with the one at index 1 (which is the second value, since the first index is 0). We don't want to see if the snake head is in the same location as the snake head, because this would always be true and cause an immediate game over that the player could never avoid.
            Assim este loop "for" irá percorrer sobre cada tupla no snakeCoords excepto sobre o primeiro. Isto é porque estamos usando snakeCoords[1:], que significa que a lista de valores começa com índice 1 (que é o segundo valor, já que o primeiro índice é 0 ). Não queremos ver se a cabeça da cobra está na mesma posição da cabeça da cobra, porque isto sempre será verdade e causa um imediato "game over" que o jogador nunca evitará."""
            if (snakeCoords[0][0], snakeCoords[0][1]) == snakeBody:
                return

        """The snake "moves" by constantly adding another tuple to the front of the snakeCoords list, with x and y coordinates that make it expand in the direction dictated by the "direction" variable. Adding this segment makes the snake grow by one segment. To give the appearance of movement, we then remove the last tuple in the list, which makes the snake appear to shrink by one segment. This is what causes the snake to "move" around the board.
        A cobra se move constantemente adicionando outra tupla a frente da lista snakeCoords, com as coordenadas x e y que fazem ela expandir na direção especificada pela variavel "direction". Adicionar este segmento faz a cobra crescer um segmento. Para dar a aparência de movimento, nós removemos a última tupla na lista, que faz a cobra paracer encolher um segmento. Isto é o que faz a cobra mover-se ao redor do quadro.
        
        When the snake eats an apple, we just skip removing the last tuple from the list. The net effect is that the snake is ends up being one segment longer than it was.
        Quando a cobra come uma maçã, apenas ignoramos a remoção da última tupla da lista. O efeito disso é que a cobra acaba por ser um segmento mais longo do que era."""
        if snakeCoords[0][0] == apple[0] and snakeCoords[0][1] == apple[1]:
            """If the snake's head is at the same location as the apple, then we immediately want to set the location of the apple to a new location. This will make the apple at the old location disappear, making it look like the snake "ate" the apple. Growing the snake by one segment is handled later.
               Se a cabeça da cobra está na mesma posição que a maçã, então, imediatamente queremos definir a posição da maçã para uma nova posição. Isto fará com que a maçã disapareça da posição antiga, parecendo que a cobra "comeu" a maçã. Aumentar a cobra em um segmento será tratado mais tarde. """
            apple = (random.randint(0, CELLWIDTH - 1), random.randint(0, CELLHEIGHT - 1))
        else:
            snakeCoords.pop()
            """The pop() list method removes the last value in a list. This makes the last "tail" segment of the snake disappear.
            O metodo pop() lista remove o último valor na lista. Isto faz o último segmento da cobra "cauda" desaparecer."""

        # move the snake
        """Here we insert a new tuple to the snakeCoords list, with xy coordinates that depend on the value in the variable named direction.
           Aqui inserimos uma nova tupla a lista snakeCoords, com as coordenadas xy que dependem do valor na variável chamada direction."""
        if direction == UP:
            snakeCoords.insert(0, (snakeCoords[0][0], snakeCoords[0][1] - 1))
        elif direction == DOWN:
            snakeCoords.insert(0, (snakeCoords[0][0], snakeCoords[0][1] + 1))
        elif direction == LEFT:
            snakeCoords.insert(0, (snakeCoords[0][0] - 1, snakeCoords[0][1]))
        elif direction == RIGHT:
            snakeCoords.insert(0, (snakeCoords[0][0] + 1, snakeCoords[0][1]))

        """Now that we're done with all the logic, we just want to draw the background, snake, apple, and score on the screen.
           Agora que já fizemos toda a lógica, apenas queremos desenhar o fundo, a cobra, a maçã e a pontuação na tela."""
        MAINSURF.fill(BGCOLOR)
        drawSnake(snakeCoords)
        drawApple(apple)
        drawScore(len(snakeCoords))
        """Note that the score is equal to how many segments are in the snake, which is equal to the number of tuples in the snakeCoords list.
           Note que a pontuação é igual a quantos segmentos estão na cobra, que é igual ao número de tuplas na lista snakeCoords."""
        pygame.display.update()
        MAINCLOCK.tick(FPS)
        """Then we call pygame.display.update() to update the screen, and call MAINCLOCK.tick(FPS) to pause the program a little bit so the game doesn't run too fast.
           Então chamamos pygame.display.update() para atualizar a tela e chamamos  MAINCLOCK.tick(FPS) para pausar o programa um pouco para o jogo não executar muito rápido """


def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('Game', True, WHITE)
    overSurf = gameOverFont.render('Over', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

    MAINSURF.blit(gameSurf, gameRect)
    MAINSURF.blit(overSurf, overRect)
    pygame.display.update()
    """Here we create a new Font object with big, 150 point letters. Then we render two surfaces with "Game" and "Over" and then display them on the screen.
       Aqui criamos um novo objeto Font com 150 letras grandes. Então, damos duas superfícies com "Game" e "Over" e mostramos elas na tela. """

    time.sleep(0.5)
    checkForKeyPress() # clear out any key presses in the event queue made up to this point
    """Because the next game will start immediately after we exit out of this loop, we want the "Game Over" text to stay on the screen for at least half a second. Then we also want to clear out all the key press events from the event queue. This will keep the player from accidentally skipping past the Game Over screen and starting the next game too soon because they pressed a key while the last game was still going on.
       Devido ao próximo jogo começar imediatamente em seguida, saimos deste laço, queremos que o texto "Game Over" fique na tela pelo menos por meio segundo. Então, também queremos limpar todos os eventos a partir da lista de eventos. Isto irá evitar que o jogador acidentalmente pule após o Game Over na tela e inicie o próximo jogo muito cedo, porque pressionou um botão enquanto o último jogo ainda estava em curso.""" 

    """Now we enter an infinite loop that only returns from this function when the user has pressed a key.
       Agora entramos em um loop infinito que somente sai desta função quando o usuário pressionar uma tecla."""
    while True:
        if checkForKeyPress():
            return


def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 80, 10)
    MAINSURF.blit(scoreSurf, scoreRect)
    """The drawScore() function simply displays the score.
       A função drawScore() simplesmente mostra a pontuação. """


def drawSnake(snakeCoords):
    for coord in snakeCoords:
        x = coord[0] * CELLSIZE
        y = coord[1] * CELLSIZE
        coordRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(MAINSURF, GREEN, coordRect)
        """This code loops through each of the tuples in snakeCoords and draws a green square on the screen using the pygame.draw.rect() function.This is how we make the snake appear on the screen. Remember though, the MAINSURF surface won't appear on the screen until the pygame.display.update() function is called. This is done at the end of the gameLoop() function.
           Este código percorre através de cada uma das tuplas no snakeCoords e desenha um quadrado verde sobre a tela usando a função pygame.draw.rect(). Isto é como é feito para a cobra aparecer sobre a tela. Lembrando que, a  superficie MAINSURF não aparecerá na tela até quando a função pygame.display.update() for chamada. Isto é feito no fim da função gameLoop(). """

def drawApple(coord):
    x = coord[0] * CELLSIZE
    y = coord[1] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(MAINSURF, RED, appleRect)
    """This function is very similar to the drawSnake() function, except there is no list that needs to be iterated over. And it draws a red square for the apple, instead of a green one.
      Esta função é muito similar a função drawSnake(), exceto que não existe uma lista que precisa ser iterada sobre ela. E ela desenha um quadrado vermelho para a maçã, ao invés de um verde.
     """


if __name__ == '__main__':
    main()
    """This if statement is actually the first line of code that is run in our program (aside from the import statements and the constant variable assignments. __name__ is a special variable that is created for all Python programs implicitly. The value stored in this variable is the string '__main__', but only when the script is run by itself. If this script is imported by another script's import statement, then the value of __name__ will be the name of the file (if this script still has the name snakey.py, then the __name__ variable will contain 'snakey').
       Esta declaração "if" é atualmente a primeira linha do código que está executando no programa (além das declarações de importação e as atribuições da variável constante. __name__ é uma variável especial que é criada implicitamente para todos os programas Python. Os valores armazenados nesta variável é a string '__main__', mas somente quando o script é executado por si mesmo. Se este script é importado por outro script, importa as declarações, daí o valor de __name__ será o nome do arquivo (se este script ainda tem o nome snakey.py, então a variável __name__ conterá 'snake')). 
    This is really handy if we ever want to use the functions that are in this program in another program. By having this if statement here, which then runs the main() function, we could have another program use "import snakey" and make use of any of the functions we've already written. Or if you want to test individual functions by calling them from the interactive shell, you could call them without running the game program. This trick is really handy for code reuse.
    Isto é realmente útil se quisermos usar as funções que estão neste programa em outro programa. Por ter essa instrução "if" aqui, que executa a função main (), poderíamos ter um outro programa usando "import snakey" e fazer uso de qualquer uma das funções que já foram escritas anteriormente. Ou se vc deseja testar funções individualmente chamando-as a partir de um shell interativo, vc pode chamá-las sem executar o programa do jogo. Esta estratégia é realmente útil para reutilização de código."""
    

