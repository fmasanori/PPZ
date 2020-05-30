# Tetromino (A Tetris Clone)
# http://inventwithpython.com/blog
# By Al Sweigart al@inventwithpython.com

"""
Welcome to the Code Comments for Tetromino. Code Comments is a series of simple games with detailed comments in the source code, so you can see how the game works.
Bem vindo aos Códigos Comentados para Tetromino. Códigos Comentados é uma série de games(jogos) simples com comentários detalhados no código fonte, assim você pode ver como o game(jogo) trabalha.

The text in between the triple-double-quotes are comments. The Python interpreter ignores any text in between them, so we can add any comments about the source code without affecting the program. In general for Code Comments, the comments will describe the lines of code above the comment. It helps to view this file either on the Code Comments site or with a text editor that does "syntax highlighting", so that the comments appear in a separate color and are easier to distinguish from the code.
O texto entre aspas duplas-triplas são comentários. O interpretador do Python ignora qualquer texto entre elas, assim podemos adicionar qualquer comentário sobre o código fonte sem afetar o programa. Em geral nos Códigos Comentados, os comentários descreverão as linhas do código acima do comentário. Isto irá ajudá-lo a visualizar este arquivo no site Code Comments ou com um editor de texto que destaca a sintaxe, de modo que os comentários aparecem em uma cor diferente e são fáceis de distinguí-los do código.

This Code Comments assumes you know some basic Python programming. If you are a beginner and would like to learn computer programming, there is a free book online called "Invent Your Own Computer Games with Python" at http://inventwithpython.com
Este Código Comentado assume que você tenha algum conhecimento básico sobre a linguagem Python. Se você é um iniciante e gostaria de aprender programação de computadores, existe um livro grátis(free) online chamado "Invent Your Own Computer Games with Python" disponível no site http://inventwithpython.com

The Code Comments programs make references to sections of this book throughout the program. This Code Comments can also teach you how to use the Pygame library to make your own games with graphics, animation, and sound. You can download Pygame from http://pygame.org and view its documentation at http://pygame.org/docs/
Os programas dos Códigos Comentados fazem referência à seções deste livro em todo o programa. Estes Códigos Comentados também podem te ensinar  como usar a biblioteca Pygame para fazer seus próprios games com gráficos, animações e sons. Você pode fazer o download do Pygame no site: http://pygame.org e visualizar sua documentação em: http://pygame.org/docs/

HOW TO PLAY TETROMINO/COMO JOGAR TETROMINO
Random blocks fall from the top of the screen until they hit another block or the bottom of the board. Try to complete a full horizontal line without any gaps in order to remove that line and score a point. Every ten points, you will go up one level and the blocks will begin to fall faster. Play for as long as you can!
Blocos aleatórios caem do topo da tela até tocarem outro bloco ou a base do tabuleiro. Tente completar a linha horinzontal sem deixar lacunas a fim de remover esta linha e marcar um ponto. A cada dez pontos vc subirá um nível e os blocos começarão a cair mais rápido. Jogue enquanto vc puder!!
"""

import random
import time
import pygame
import sys
from pygame.locals import *
"""Here we import modules that our game needs. random has random number functions, time has the sleep() function, sys has the exit() function, and pygame contains all the pygame-related functions.
Aqui nós importamos módulos que nosso game precisa. random tem funções de números aleatórios, time tem a função sleep(), sys tem a função exit(), e pygame contém todas as funções relacionadas ao paygame.

pygame.locals contains constants like MOUSEMOTION and MOUSEBUTTONUP and QUIT for the events. It's easier to type MOUSEBUTTONUP instead of pygame.locals.MOUSEBUTTONUP, so we use the "from pygame.locals import *" format to import these to the local namespace.
pygame.locals contém constantes como MOUSEMOTION e MOUSEBUTTONUP e QUIT para os eventos. É mais fácil digitar  MOUSEBUTTONUP em vez de pygame.locals.MOUSEBUTTONUP, assim usamos o formato "from pygame.locals import *" para importá-los para o local namespace.
"""

FPS = 25
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BLOCKSIZE = 20
BOARDWIDTH = 10
BOARDHEIGHT = 20
BLANK = -1
"""These constant variables (the uppercase names means we shouldn't change the values stored in them) set some standard values for our game. You can play around with different values for them (though some values might cause bugs in the game.) By using constants instead of the values directly, it is easier to make changes since we only have to change them in one place.
Estas variáveis constantes (os nomes em letras maiúsculas significa que não podemos mudar o valor armazenado nelas) definem alguns valores padrão para o nosso jogo. Você pode jogar com valores diferentes para eles (no entanto alguns valores podem causar erros no jogo). Usando constantes ao invés dos valores diretamente, é mais fácil fazar mudanças e então somente temos que mudá-las em um lugar.

For example, if we used 20 instead of BLOCKSIZE, then if we wanted to change our code later we'd have to change every place in the code we find 20. This is trickier than just changing the one line where BLOCKSIZE is originally set.
Por exemplo, se usamos 20 ao invés de BLOCKSIZE, então se quisermos mudar nosso código mais tarde, teremos que mudar todos os lugares no código onde encontramos 20. Isto é mais complicado do que apenas mudar a linha onde o BLOCKSIZE está originalmente definido.

WINDOWWIDTH and WINDOWHEIGHT give the size of the window in pixels. FPS is how often we redraw the image to the screen in frames per second. BLOCKSIZE are the size (in pixels) of the four individual blocks that make up the tetromino pieces. Because the blocks are squares, BLOCKSIZE will be used for both the block width and height.
WINDOWWIDTH e WINDOWHEIGHT dá o tamanho da janela em pixels. FPS é como frequentemente redesenhamos a imagem na tela em frames por segundo. BLOCKSIZE são o tamanho (em pixels) dos quatro blocos individuais que formam as peças do tetromino. Devido aos blocos serem quadrados, BLOCKSIZE será usado para a altura e para a largura do bloco.

BOARDWIDTH and BOARDHEIGHT give the size of the playing board, in blocks. A 10 x 20 board has space for up to 200 (that is, 10 x 20) blocks.
BOARDWIDTH and BOARDHEIGHT dá o tamanho do tabuleiro do jogo, em blocos. Um tabuleiro 10 x 20 tem espaço até 200 (que é, 10 x 20) blocos.

BLANK is just a value we use to represent a blank space. This will be explained later on.
BLANK é somente um valor usado para representar um espaço em branco. Isto será explicado mais tarde.

More information about constants is at http://inventwithpython.com/chapter9.html#ConstantVariables
Mais informações sobre constantes em: http://inventwithpython.com/chapter9.html#ConstantVariables
"""

MOVESIDEWAYSFREQ = 0.15
MOVEDOWNFREQ = 0.10
"""Each time the player presses the left or right key, the current falling piece moves to the left or right by one space on the board. However, if the player holds down the left key, then we would want the piece to repeatedly move the left depending on how long they hold down the key. A MOVESIDEWAYSFREQ value of 0.15 means that the falling piece would move to the left once every 0.15 seconds that the left key is being held.
Cada vez que o jogador pressiona a tecla direita ou esquerda, a peça atual que está caindo se move para a esquerda ou para a direita por um espaço no tabuleiro. No entanto, se o jogador mantém pressionada a tecla esquerda, então queremos a peça a se mover repetidamente a esquerda, dependendo de quanto tempo ele a mantenha pressionada. Um valor MOVESIDEWAYSFREQ de 0.15 significa que a peça caindo deverá se mover para a esquerda uma vez a cada 0.15 segundo que a tecla esquerda está sendo mantida.

The MOVEDOWNFREQ is similar, except this is for how often a piece should fall if the player has the down arrow key held down.
O MOVEDOWNFREQ é parecido, exceto que isto é para quantas vezes uma peça deve cair se o jogador matém a tecla de seta para baixo pressionada"""

XMARGIN = int((WINDOWWIDTH - BOARDWIDTH * BLOCKSIZE) / 2)
TOPOFBOARD = WINDOWHEIGHT - (BOARDHEIGHT * BLOCKSIZE) - 5
"""We want to calculate how much horizontal space is on either side of the board. This depends on the width of the window, the width of the board, and the size of each block. We take the full width of the window, and want to subtract the width of the board in pixels (which is BOARDWIDTH * BLOCKSIZE). This gives us the amount of space on either side of the board, so we divide by two to get the width of just one of these margins.
Queremos calcular quanto espaço horizontal está sobre o outro lado do tabuleiro. Isto depende da largura da janela, da largura do tabuleiro e do tamanho de cada bloco. Pegamos a largura total da janela e subtraimos a largura do tabuleiro em pixels (que é BOARDWIDTH * BLOCKSIZE). Isto nos dá a quantidade de espaço sobre o lado do tabuleiro, então dividimos por dois para obter a largura de apenas uma das margens.

The y coordinate of the top of the board is calculated by taking the full height of the window and subtracting the height of the board in pixels (which is BOARDHEIGHT * BLOCKSIZE), and then subtracting 5 pixels from this. The extra 5 pixels are removed because we want to make room for the blue border that goes around the board.
A coordenada y do topo do tabuleiro é calculada pegando a altura total da janela e subtraindo a altura do tabuleiro em pixels (que é BOARDHEIGHT * BLOCKSIZE) e então subtraindo 5 pixels a partir deste. Os 5 pixels extra são removidos porque queremos abrir espaço para a borda azul que gira em torno do tabuleiro"""

#            R    G    B
WHITE =    (255, 255, 255)
BLACK =    (0,     0,   0)
RED =      (155,   0,   0)
GREEN =    (0,   155,   0)
BLUE =     (0,     0, 155)
YELLOW =   (155, 155,   0)
DARKGRAY = (40,   40,  40)

BORDERCOLOR = BLUE
BGCOLOR = BLACK
COLORS = (BLUE, GREEN, RED, YELLOW)
"""We also set up some constant values for different colors. Pygame uses tuples of three integers to represent color. The integers represent the amount of red, green, and blue in the color (this is commonly called a RGB). 0 means there == None of the primary color in the color, and 255 means there is the maximum amount. So (255, 0, 0) is red, since it has the maximum amount of red but no green or blue. But (255, 0, 255) adds the max amount of blue with the red, creating purple.
Também podemos definir alguns valores constantes para diferentes cores. Pygame usa tuplas de 3 inteiros para representar a cor. Os inteiros representam a quantidade de vermelho, verde e azul na cor (isto é comumente chamado RGB). 0 significa que não existe nada de cor primária na cor e 255 significa que existe a quantidade máxima. Assim, (255, 0, 0) é vermelho, já que ela tem a quantidade máxima de vermelho e não tem nada de verde ou azul. Mas, (255, 0, 255) adiciona a quantidade máxima de azul com vermelho, criando a cor pupura.

BORDERCOLOR will store the color we use for drawing the board's border, and BGCOLOR will be the general background color used in the game.
BORDERCOLOR armazenará a cor usada para desenhar a borda do tabuleiro e BGCOLOR será a cor de fundo usada no jogo.

COLORS will be a tuple that contains all the different colors the pieces will use. Each new piece will randomly select a color from this tuple.
COLORS será a tupla que contém todas as cores das diferentes peças usadas. Cada peça nova selecionará aleatoriamente uma cor desta tupla.

More information about colors is at http://inventwithpython.com/chapter17.html#ColorsinPygame
Mais informações sobre cores em: http://inventwithpython.com/chapter17.html#ColorsinPygame
"""

S_PIECE = [['.....',
            '.....',
            '..OO.',
            '.OO..',
            '.....'],
           ['.....',
            '..O..',
            '..OO.',
            '...O.',
            '.....']]

Z_PIECE = [['.....',
            '.....',
            '.OO..',
            '..OO.',
            '.....'],
           ['.....',
            '..O..',
            '.OO..',
            '.O...',
            '.....']]

I_PIECE = [['..O..',
            '..O..',
            '..O..',
            '..O..',
            '.....'],
           ['.....',
            '.....',
            'OOOO.',
            '.....',
            '.....']]

O_PIECE = [['.....',
            '.....',
            '.OO..',
            '.OO..',
            '.....']]

J_PIECE = [['.....',
            '.O...',
            '.OOO.',
            '.....',
            '.....'],
           ['.....',
            '..OO.',
            '..O..',
            '..O..',
            '.....'],
           ['.....',
            '.....',
            '.OOO.',
            '...O.',
            '.....'],
           ['.....',
            '..O..',
            '..O..',
            '.OO..',
            '.....']]

L_PIECE = [['.....',
            '...O.',
            '.OOO.',
            '.....',
            '.....'],
           ['.....',
            '..O..',
            '..O..',
            '..OO.',
            '.....'],
           ['.....',
            '.....',
            '.OOO.',
            '.O...',
            '.....'],
           ['.....',
            '.OO..',
            '..O..',
            '..O..',
            '.....']]

T_PIECE = [['.....',
            '..O..',
            '.OOO.',
            '.....',
            '.....'],
           ['.....',
            '..O..',
            '..OO.',
            '..O..',
            '.....'],
           ['.....',
            '.....',
            '.OOO.',
            '..O..',
            '.....'],
           ['.....',
            '..O..',
            '.OO..',
            '..O..',
            '.....']]
"""For our game, we need a way to specify the shape of each piece in every possible rotation. We will set up a data structure to do this. The data structure will be a list of lists, where the inner list contains strings of five characters to represent a row of the piece. There will be five of these strings in the inner list, and each inner list represents one rotation of the piece.
Para nosso jogo, precisamos de uma maneira para especificar a forma de cada peça em todas as possíveis rotações. Definiremos uma estrutura de dados  para isto. A estrutura de dados será uma lista de listas, a lista interna contém strings de cinco caracteres para representar a coluna da peça. Existirá cinco dessas strings na lista interna e cada lista interna representa uma rotação da peça.

Take the T_PIECE data structure for an example. There are four inner lists, one for each rotation of the T-shape. We use periods to represent blank spaces and O characters to represent a filled in block for that piece. The order of these inner lists counts, because we will switch to the next one when the player presses the rotate button.
Pegando a estrutura de dados T_PIECE para um exemplo. Existem quatro listas internas, uma para cada rotação da T-shape. Usamos periodos para representar espaçoes em branco e caracteres O para representar um preenchimento no bloco para aquela peça. A ordem destas listas internas conta, porque mudaremos para o próximo, quando o jogador pressionar o botão de rotação. 

Make sure that each subsequent inner list has the piece rotated clockwise, or else the piece will rotate in odd ways during the game.
Certifique-se que cada lista interna subsequente tem a peça girado no sentido horário, ou então, a peça vai rodar de maneira estranha durante o jogo.
"""

PIECES = {'S': S_PIECE,
          'Z': Z_PIECE,
          'J': J_PIECE,
          'L': L_PIECE,
          'I': I_PIECE,
          'O': O_PIECE,
          'T': T_PIECE}
"""After we've specified the data structure for each of the pieces, we will put them all in a dictionary named PIECES. PIECES contains every possible piece in every possible rotation in our game. We will use strings of single letters as keys for the piece data.
   Depois de termos especificado a estrutura de dados para cada peça, colocaremos antão tudo em um dicionário chamado PIECES. PIECES contém todas as possíveis peças em todas as possíveis rotações no nosso jogo. Usaremos sequências de letras individuais como chaves para os dados da peça"""

# Convert the shapes in PIECES from our input-friendly format to a programmer-friendly format.
"""The way we entered the data that describes the shape of each piece above is really convenient when we are typing in code into a text file. However, if you think about it, we would access the xy coordinates backwards. Consider this part of the data structure, and say we store it in a variable named spam:
   A maneira como entramos os dados que descrevem a forma de cada peça acima é realmente conveniente quando estamos digitando no código em um arquivo de texto. Todavia, se vc pensar sobre isso, deveriamos acessar as coordenadas xy. Considerando esta parte da estrutura de dados e vamos dizer que estamos armazenado isto em uma variável chamada spam:
spam =  ['.....',
         '.....',
         '.OOO.',
         '..O..',
         '.....']

It seems like we could access the individual characters with a spam[x][y] convention, but really we would have to use a spam[y][x] convention. This is because the first index would access the row of the shape (which means the y coordinate) and the second index access the column (which means the x coordinate. Let's say we changed the one of the O characters to an X in spam, so it looks like this:
Vemos que podemos acessar os caracteres individuais com um spam[x][y] convencional, mas, de fato, temos que usar um spam[x][y] convencional. Isto porque o primeiro indíce deve acessar a linha da forma (que significa a coordenada y) e o segundo índice acessa a coluna (que é a coordenada x). Dizemos que mudamos um dos caracteres O para X no spam, veremos isto:
spam =  ['.....',
         '.....',
         '.XOO.',
         '..O..',
         '.....']

The expression spam[2][1] would evaluate to 'X', even though it seems like it should be spam[1][2] since from our perspective the X is at an x coordinate of 1 and y coordinate of 2.
A expressão spam[2][1] seria avaliada para 'X', mesmo que pareça que deveria ser spam[1][2] já que a partir de nossa perspectiva o X está em uma coordenada x de 1 e coordenada y de 2.

This can get confusing for us as we write our program, so let's write some code that changes this around. The following for loops go through each piece, rotation, and then column to switch these values.
Isto pode causar confusão para escrever nosso programa. O seguinte laço "for" percorre cada peça, rotação, e em seguida a coluna para mudar esses valores. """
for p in PIECES: # loop through each piece / Laço que percorre cada peça
    for i in range(len(PIECES[p])): # loop through each rotation of the piece / Laço que percorre cada rotação da peça
        shapeData = []
        for x in range(5): # loop through each column of the rotation of the piece / Laço que percorre cada coluna da rotação da peça
            column = []
            for y in range(5): # loop through each character in the column of the rotation of the piece /Laço que percorre cada caracter na coluna da rotação da peça
                if PIECES[p][i][y][x] == '.':
                    column.append(BLANK)
                else:
                    column.append(1)
            shapeData.append(column)
        PIECES[p][i] = shapeData


def main():
    global MAINCLOCK, MAINSURF, BASICFONT
    """The main() function is where our program begins. (See the last two lines of code to see why.) Because we define MAINCLOCK and MAINSURF inside this function, these are local variables to the main() function and the names MAINCLOCK and MAINSURF won't exist outside of this function. By using a global statement, we can tell Python that we want these variables to be global variables.
    A função main() é onde nosso programa começa. (Ver as duas últimas linhas do código para ver o porque). Porque nós definimos MAINCLOCK e MAINSURF dentro desta função, elas são variáveis locais a função main() e os nomes MAINCLOCK e MAINSURF não existem fora desta função. Usando uma definição global, podemos dizer ao Python que queremos estas variaveis sejam variáveis globais. 

    More information about global and local variables is at http://inventwithpython.com/chapter6.html#VariableScope
    Mais informações sobre variáveis locais e globais em: http://inventwithpython.com/chapter6.html#VariableScope"""
    pygame.init()
    MAINCLOCK = pygame.time.Clock()
    MAINSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Tetromino')
    """pygame.init() needs to be called before any of the other Pygame functions.
    pygame.init() precisa ser chamada antes de qualquer outra função Pygame.

    pygame.time.Clock() returns a pygame.Clock object. We will use this object's tick() method to ensure that the program runs at no faster than 15 frames per second (or whatever integer value we have in the FPS constant.)
    pygame.time.Clock() retorna o objeto pygame.Clock. Usaremos este objeto no metodo tick() para garantir que o programa não seja executado em mais de 15 frames por segundo (ou qualquer outro valor inteiro que temos no FPS constante.)
    
    pygame.display.set_mode() creates the window on the screen and returns a pygame.Surface object. Any drawing done on this Surface object with the pygame.draw.* functions will be displayed on the screen when we call pygame.display.update().
    pygame.display.set_mode() cria a janela na tela e retorna um objeto pygame.Surface. Todo o desenho feito sobre a superfície deste objeto com as funções pygame.draw.* serão mostradas na tela quando chamamos pygame.display.update().
        
    More information about pygame.display.set_mode() is at http://inventwithpython.com/chapter17.html#ThepygamedisplaysetmodeandpygamedisplaysetcaptionFunctions
    Mais informação sobre pygame.display.set_mode() está em: http://inventwithpython.com/chapter17.html#ThepygamedisplaysetmodeandpygamedisplaysetcaptionFunctions

    The call to the pygame.font.Font() constructor function creates a Font object. We will store this Font object in the global variable BASICFONT.
    A chamada a função pygame.font.Font() cria um obejto Font. Amazenaremos este objeto Font na variável global BASICFONT."""
    
    # Start of the game:
    showTextScreen('Tetromino')
    while True:
        """First we will randomly pick which music to play as the background music, either tetrisb.mid or tetrisc.mid
        Primeiro vamos escolher aleatoriamente qual a música tocará como música de fundo, tetrisb.mid ou tetrisc.mid"""
        
        if random.randint(0, 1) == 0:
            pygame.mixer.music.load('tetrisb.mid')
        else:
            pygame.mixer.music.load('tetrisc.mid')
        pygame.mixer.music.play(-1, 0.0)
        """The pygame.mixer.music.play() function will start playing the background music that was loaded by the pygame.mixer.music.load() function. The first parameter is how many times to repeat the music after the first time it plays (with -1 meaning an infinite number of plays). The second parameter describes the starting point of the music in seconds. 0.0 means that the music should start playing from the beginning. A value of, say, 5.0 for this parameter would mean that the music should start playing at 5 seconds after the start of the music.
        A função pygame.mixer.music.play() começará jogando a música de fundo que foi lida pela função pygame.mixer.music.load(). O primeiro parâmetro é  quantas vezes a musica vai repetir depois da primeira vez que ela executa (com -1 significa um número infinito de execuções). O segundo parâmetro descreve o ponto de partida da música em segundos. 0.0 significa que a música deveria começar a execução a partir do começo. Um valor de, por exemplo, 5.0 para este parâmetro pode significar que a música deveria iniciar a exeução em 5 segundos depois do início da musica. """

        gameLoop()

        pygame.mixer.music.stop()
        """The pygame.mixer.music.stop() function will halt the background music.
           A função pygame.mixer.music.stop() interromperá a música de fundo. """
        showTextScreen('Game Over')
    """The above code handles showing the start screen, then goes into a repeating loop of playing the main game and then showing the "Game Over" screen when the game is over. After that, it loops back to playing the game again. This will keep happening until the player shuts off the program (which is done from inside the gameLoop() or showTextScreen() functions, explained later.)
       O código acima manipula e mostra a tela inicial, depois entra em um loop de repetição jogando o jogo principal e depois, mostra o "Game Over" na tela quando o jogo acabou. Depois disto, o loop volta a jogar o game outra vez. Isto continua acontecendo até o jogador desligar o programa (que é feito dentro das funções gameLoop() ou showTextScreen() explicadas mais tarde.)"""

def showTextScreen(text):
    # This function displays large text in the center of the screen. / Esta função mostra textos grandes no centro da tela.
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    """There are six steps to making text display on the screen in Pygame. The first is to create a pygame.font.Font object (which we will just call a Font object for short). In this case, we create a Font object from the "freesansbold.ttf" font file (this font comes with Pygame) and we want the size of the Font to be at 100 points.
    Existem seis passos para fazer o texto aparecer na tela em Pygame. O primeiro é criar um objeto pygame.font.Font (que chamaremos apenas de objeto Font). Neste caso, nós criamos um objeto Font a partir do arquivo fonte "freesansbold.ttf" (este fonte vem com o Pygame) e queremos que o tamanho da Font seja 100 pontos. 

    If you want to draw text in other fonts or sizes, you must create a new Font object for each one.
    Se você quer desenhar o texto em outras fontes, vc deve criar um novo objeto Font para cada uma."""

    titleSurf = titleFont.render(text, True, WHITE)
    """The second step is to call the Font object's render() method, which will return a Surface object with the text drawn on it. The fourth parameter provides the background color on the Surface. If you don't provide this fourth parameter, then the Surface object will have a transparent background.
    O segundo passo é chamar o objeto Font pelo método render(), que retorna um objeto Surface com o texto desenhado nele. O quarto parâmetro fornece a cor de fundo na Surface (superficie). Se vc não fornecer este quarto parâmetro, então o objeto Surface terá um fundo transparente.

    There is more info on anti-aliasing at http://inventwithpython.com/chapter17.html#TherenderMethodforFontObjects
    Há mais informações sobre anti-aliasing em http://inventwithpython.com/chapter17.html#TherenderMethodforFontObjects
    
    Remember that the font size information is already stored in the pygame.font object stored in our global variable named BASICFONT.
    Lembrando que a informação sobre o tamanho da fonte está anteriormente armazenada no objeto pygame.font armazenado em nossa variável global chamada BASICFONT"""

    titleRect = titleSurf.get_rect()
    """The third step is to get a Rect object from the Surface object, so we can set the position of the text on the screen. The Surface object's get_rect() method will return a Rect object for the surface with the text on it.
       O terceiro passo é pegar um objeto Rect a partir do objeto Surface, assim podemos definir a posição do texto na tela. O objeto Surface pelo método get_rect() retornará um objeto Rect para a superfície com o texto sobre ela."""

    titleRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))
    """The fourth step is to set the position of the text. Above we are setting the center of the Rect to an x coordinate of int(WINDOWWIDTH / 2) (that is, the horizontal middle of the window (since the window is WINDOWWIDTH pixels long)) and a y coordinate of int(WINDOWWIDTH / 2) (the vertical middle of the window.)
    O quarto passo é definir a posição do texto. Acima nós definimos o centro do Rect em uma coordenada x de int(WINDOWWIDTH / 2) (isto é, o meio horizontal da janela (já que a janela é WINDOWWIDTH pixels de comprimento)) e uma coordenada y de int(WINDOWWIDTH / 2 (o meio vertical da janela.)"""

    MAINSURF.blit(titleSurf, titleRect)
    """The fifth step is to draw the Surface object containing the text at the position on the screen specified by the Rect object with the blit() method. The sixth step is to call pygame.display.update(). These are done a few lines down.
       O quinto passo é desenhar o objeto Surface contendo o texto na posição sobre a tela especificada pelo objeto Rect com o método blit(). O sexto passo é chamar pygame.display.update(). Isto é feito em poucas linhas abaixo."""

    pressKeySurf = BASICFONT.render('Press a key to play.', True, WHITE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) + 100)
    MAINSURF.blit(pressKeySurf, pressKeyRect)
    """We repeat these steps for the "Press a key to play." text, which uses a different Font object (the 18 point font we stored in the BASICFONT global variable.)
       Repetimos esses passos para o texto "Press a key to play." que usa um diferente objeto Font (a fonte de 18 pontos armazenamos na variável global BASICFONT.) """

    while checkForKeyPress() == None:
        pygame.display.update()
        MAINCLOCK.tick()
        """The call to pygame.display.update() takes everything drawn on the MAINSURF surface and draws it on the screen. The call to MAINCLOCK.tick() will then cause the program to wait for a fraction of a second. If we didn't have this call, then the program would draw frames of this animation as fast as possible. This means our game would run very fast on fast computers, and very slow on slow computers.
        A chamada a pygame.display.update() pega tudo desenhado na superfície MAINSURF e desenha na tela. A chamada a MAINCLOCK.tick() fará o programa aguardar por uma fração de segundo. Se não temos essa chamada, o programa vai desenhar frames desta animação o mais rápido possível. Isto significa que nosso jogo irá rodar muito rápido em computadores rápidos e muito lento em computadores lentos. 

        Here, we call our checkForKeyPress() function (which we will define later) to see if the user has pressed any key. If this function returns None, then we know a key has not been pressed and we should continue to loop.
        Aqui chamamos nossa função checkForKeyPress() (que definiremos mais tarde) para ver se o usuário pressionou alguma tecla. Se está função retorna None, então sabemos que uma tecla não foi pressionada e devemos continuar o loop.
        """

def terminate():
    pygame.quit()
    sys.exit()
    """In order to terminate the program, we must call both pygame.quit() (to shut down the Pygame engine) and sys.exit() (to shut down the program.) Calling sys.exit() without calling pygame.quit() first probably won't harm anything, though it does give IDLE some problems if the user runs this program from it. It's just considered a graceful way to shut down the Pygame library.
    Com o objetivo de terminar o programa, devemos chamar ambos pygame.quit() (para desligar o mecanismo Pygame) e sys.exit() (para desligar o programa.) Chamar sys.exit() sem primeiro chamar pygame.quit() provavelmente não vai prejudicar nada, embora ele dê alguns problemas IDLE se o usuário executar este programa a partir dele. É apenas considerada uma maneira graciosa para encerrar a biblioteca Pygame. """


def gameLoop():
    """This is where the main part of the game takes place. We have an infinite loop (the "while True:" loop) that handles player input, updating the state of the game world, and displaying the game world on the screen. The part before the infinite loop sets up variables for the start of a game. When the game is over, we return from this function.
    Aqui é onde a parte principal do game está localizada. Temos um loop infinito (o loop "while True:") que  manipula a entrada do jogador, atualizando o estado do game, e mostrando o mundo do jogo na tela. A parte anterior do loop infinito define variáveis para iniciar o game. Quando o jogo acabar, retornamos a partir desta função."""

    # beginning of the game setup: 
    board = getNewBoard()
    """We need a brand new data structure to represent the board, which we can get from the getNewBoard() function. We will start with a new board data structure each time the game begins.
       Precisamos de uma nova marca da estrutura de dados para representar o tabuleiro, que podemos obter a partir da função getNewBoard(). Começaremos com um novo tabuleiro cada vez que o jogo começa. """

    lastMoveDownTime = time.time()
    lastMoveSidewaysTime = time.time()
    lastFallTime = time.time()
    """We will keep track of when it is time to move a piece down or sideways (if the arrow keys are held down) or if the piece needs to naturally fall with the lastMoveDownTime, lastmoveSidewaysTime, and lastFallTime variables. These will contain floating point numbers of the seconds since Jan 1, 1970 (the "unix epoch"). This number is returned by time.time().
     Vamos acompanhar de quando é a hora de mover uma peça para baixo ou para o lado(se as teclas de seta são mantidas para baixo) ou se as peças precisam naturalmente cair com  as variáves lastMoveDownTime, lastmoveSidewaysTime e lastFallTime. Isto conterá números em ponto flutuante desde 1 Jan de 1970 (a "época unix"). Este número é retornado por time.time(). """

    movingDown = False
    movingLeft = False
    movingRight = False
    """To keep track if the down, left, or right arrow key has been held down (or their S, A, D key equivalents), we will have boolean values to track this. Note that these variables track if the keyboard key is held down, while the last* variables above keep track of the time of the last piece movement.
       Para acompanhar se as setas para baixo, para esquerda ou para direita foram pressionadas(ou suas teclas equivalentes S,A,D), teremos valores boleanos. Note que essas variáveis acompanham se a é pressionada, enquanto as variaveis last* acima acompanham o tempo do movimento da última peça."""

    score = 0
    level = calculateLevel(score)
    fallFreq = calculateFallFreq(level)
    """The score starts off at 0 and will increase by 1 each time a line is complete (though you could change the code to a new system). The level and how fast the pieces fall ("fall frequency") are calculated based on what the score or level are. The level will increase by 1 for every 10 points scored. The fallFreq variable holds a floating point number of how many seconds between each fall of a piece. The lower this number becomes, the faster and more frequently the pieces fall.
       A pontuação começa em 0 e é aumentada por 1 cada vez que uma linha é completada (embora vc pode alterar o código para um novo sistema). O nível e quão rápido as peças vão cair ("frequencia de queda") são calculados com base na pontuação. O nível aumentará de 1 a cada 10 pontos. A variável fallFreq possui um número em ponto flutuante de quantos segundos entre cada queda de uma peça. Quanto menor esse número se tornar, mais rápido e mais freqüentemente caem as peças."""

    currentPiece = getNewPiece()
    nextPiece = getNewPiece()
    """The current piece and next piece will be stored in these two varaibles. getNewPiece() will return a data structure of a randomly generated piece.
       A peça atual e a próxima peça serão armazenadas nestas duas variáveis. getNewPiece() retornará uma extrutura de dados de uma peça gerada aleatoriamente. """

    # main game loop while in play
    while True:
        """This is the main game loop. The code in this loop is constantly executed over and over again, updating the state of the board, reading any keyboard key presses, and drawing the board to the screen. When the player quits or loses the game, the program execution will leave this loop.
         Este é o loop principal do jogo. O código neste loop(laço) é executado constantemente repetidas vezes, atualizando o estado do tabuleiro, lendo qualquer tecla pressionada do teclado e desenhando o tabuleiro na tela. Quando o jogador sai ou perde o jogo, a execução do programa sairá do laço."""

        if currentPiece == None:
            # start a new piece at the top of the board
            """currentPiece will be set to None immediately after the piece has "landed" and settled at the bottom of the board. This is how we know to set currentPiece to nextPiece and then get a new piece for nextPiece.
               currentPiece será definida None imediatamente após a peça ter sido depositada no fundo do tabuleiro. Assim é como nós sabemos definir currentPiece para nextPiece e então obter uma nova peça para nextPiece. """
            currentPiece = nextPiece
            nextPiece = getNewPiece()
            lastFallTime = time.time() # reset lastFallTime

            if not isValidPosition(board, currentPiece):
                """If the initial position of the new piece that has just started to fall is invalid, then we know that the board must be filled up all the way to the top and the player has lost. We call break to break out of the main game loop.
                   Se a posição inicial da nova peça que acaba de começar a cair é inválida, então sabemos que o tabuleiro deve ser preenchido por todo o caminho até o topo e que o jogador perdeu. Chamamos a pausa para sair do loop principal do jogo."""
                break # game over

        # handle any input from the player
        for event in pygame.event.get():
            """Here we loop through all the events in the event queue. The pygame.event.get() function will return a list of pygame.event.Event objects that have been generated since the last time pygame.event.get() was called. An Event object is generated whenever the player presses a key, clicks the mouse, tries to shut down the program, move sthe mouse, and many other situations.
            Aqui vamos percorrer todos os eventos na fila de eventos. A função pygame.event.get() retornará uma lista de objetos pygame.event.Event que têm sido gerados desde a última vez que pygame.event.get() foi chamada. Um objeto Event gerado sempre que o jogador pressiona uma tecla, clica o mouse, tenta desligar o programa, move o mouse e em muitas outras situações.

            More info on events can be found here: http://inventwithpython.com/chapter18.html#EventsandHandlingtheKEYDOWNEvent
            Mais informação sobre eventos podem ser encontradas em: http://inventwithpython.com/chapter18.html#EventsandHandlingtheKEYDOWNEvent  """
            if event.type == QUIT:
                terminate()
                """The QUIT event is created when the user tries to shut down the program by clicking the X in the top right corner, or by killing the program from the task manager or some other means. Note that QUIT comes from pygame.locals.QUIT, but we can simply type QUIT because we used "from pygame.locals import *" instead of "import pygame.locals". The same applies for MOUSEMOTION, MOUSEBUTTONUP, KEYDOWN, and the keyboard constants such as K_ESCAPE and K_p since these values are also in pygame.locals.
                   O evento QUIT é criado quando o usuário tenta desligar o programa clicando em X no canto direito do topo, ou matando o programa através do gerenciador de tarefas ou por algum outro meio. Note que QUIT vem de pygame.locals.QUIT, mas podemos digitar apenas QUIT porque usamos  "from pygame.locals import *" em vez de "import pygame.locals". O mesmo se aplica para MOUSEMOTION, MOUSEBUTTONUP, KEYDOWN e para constantes do teclado como K_ESCAPE e K_p já que esses valores estão também em pygame.locals."""
            elif event.type == KEYUP:
                if (event.key == K_p):
                    # Pausing the game
                    MAINSURF.fill(BGCOLOR)
                    """When the game is paused, we want to hide the board from the player, so we fill the entire main surface with the background color. This is so that the player can't pause the game and take their time to decide where a piece should go.
                       Quando o jogo é parado, queremos esconder o tabuleiro do jogador, por isso preenchemos toda a superfície principal com a cor de fundo.  Isto é para que o jogador não possa pausar o jogo e ganhar tempo para decidir onde uma peça deve ir."""
                    showTextScreen('Paused')
                    """By calling showTextScreen(), we can stop the program from continuing until the player has pressed a button.
                       Chamando showTextScreen(), podemos parar o programa até que o jogador tenha pressionado algum botão."""
                    lastFallTime = time.time()
                    lastMoveDownTime = time.time()
                    lastMoveSidewaysTime = time.time()
                    """After unpausing the game, we need to reset the various last*Time variables, since the old values are in the potentially much distant past by the time the player unpauses the game.
                       Depois de despausar o jogo, precisamos redefinir as várias variáveis last*Time, já que os valores velhos estão potencialmente em um passado muito distante devido ao tempo em que o jogador pausou o jogo."""

                if (event.key == K_LEFT or event.key == K_a):
                    movingLeft = False
                if (event.key == K_RIGHT or event.key == K_d):
                    movingRight = False
                if (event.key == K_DOWN or event.key == K_s):
                    movingDown = False
                """If the player lets go of one of the arrow keys, we should set the corresponding direction variable to False to show that that key isn't being held down anymore. Notice that the player can either ues the arrow keys on the keyboard (represented by the Pygame constants K_LEFT, K_RIGHT, and K_DOWN) or the WASD keys (with a for left, d for right, and s for down.)
                   Se o jogador solta uma das teclas de seta, devemos definir a variável de direção correspondente a False para mostrar que essa tecla não está sendo pressionada mais. Note que o jogador pode usar ou as teclas de seta ou as teclas do teclado (representada pelas constantes  K_LEFT, K_RIGHT, and K_DOWN) ou teclas WASD (com a para esquerda, d para direita e s para abaixo.) """

            elif event.type == KEYDOWN:
                # moving the block sideways (Movendo o bloco para os lados)
                if (event.key == K_LEFT or event.key == K_a) and isValidPosition(board, currentPiece, adjX=-1):
                    currentPiece['x'] -= 1
                    lastMoveSidewaysTime = time.time()
                    movingLeft = True
                    movingRight = False
                    lastMoveSidewaysTime = time.time()
                if (event.key == K_RIGHT or event.key == K_d) and isValidPosition(board, currentPiece, adjX=1):
                    currentPiece['x'] += 1
                    movingRight = True
                    movingLeft = False
                    lastMoveSidewaysTime = time.time()
                """When we first push the left or right keys, we want to move the current piece over by 1 block position (but only if this new position is a valid one, which is why we call isValidPosition()). Then we want to set the direction variable to True, while setting the opposite direction variable to False. This way holding down both arrow keys results in moving in the direction of the last key pushed down, instead of canceling each other out.
                   Quando começamos a empurrar as teclas esquerda ou direita, queremos movimentar a peça atual em uma posição (mas só se essa nova posição é válida, é por isso que chamamos isValidPosition ()). Então queremos definir a variável de direção como True, enquanto definimos a variável de direção oposta para False. Desta forma, pressionando ambas as teclas de seta resulta em mover na direção da última tecla empurrado para baixo, em vez de anular-se mutuamente.
                 Then we reset the lastmoveSidewaysTime variable to the current time.
                 Então redefinimos a variável lastmoveSidewaysTime para o tempo atual. """

                # rotating the block (if allowed) (Rotacionando o bloco (se permitido) )
                if (event.key == K_UP or event.key == K_w):
                    currentPiece['rotation'] = (currentPiece['rotation'] + 1) % len(PIECES[currentPiece['shape']])
                    if not isValidPosition(board, currentPiece):
                        currentPiece['rotation'] = (currentPiece['rotation'] - 1) % len(PIECES[currentPiece['shape']])
                if (event.key == K_q):
                    currentPiece['rotation'] = (currentPiece['rotation'] - 1) % len(PIECES[currentPiece['shape']])
                    if not isValidPosition(board, currentPiece):
                        currentPiece['rotation'] = (currentPiece['rotation'] + 1) % len(PIECES[currentPiece['shape']])
                """These lines of code are similar to the left and right key presses above. Instead, we handle rotating the pieces clockwise or counterclockwise. We rotate the piece, then check if its new position is a valid one, and if not, then we rotate it back.
                   Estas linhas de código são similares a pressionar as teclas direita e esquerda. Em vez disso, lidamos com a rotação das peças no sentido horário ou anti-horário. Rotacionamos a peça, em seguida, verificamos se sua nova posição é válida e, se não, então rotacionamos de volta."""

                # making the block fall faster (Fazendo o bloco cair mais rápido)
                if (event.key == K_DOWN or event.key == K_s):
                    movingDown = True
                    if isValidPosition(board, currentPiece, adjY=1):
                        currentPiece['y'] += 1
                    lastMoveDownTime = time.time()
                if event.key == K_SPACE:
                    # move the current block all the way down 
                    movingDown = False
                    movingLeft = False
                    movingRight = False
                    for i in range(1, BOARDHEIGHT):
                        if not isValidPosition(board, currentPiece, adjY=i):
                            break
                    currentPiece['y'] += (i-1)
                    """The space key will automatically drop the current piece all the way to the bottom. We do this by looping through 1 to the total height of the board, checking to see if that the current piece were moved down by an incremental amount would result in an invalid position on the board (that is, past the bottom or overlapping with other blocks.) Once we find this point, we just set the current piece the the row above that point.
                       A tecla de espaço vai descer automaticamente a peça atual por todo o caminho até o fundo. Fazemos isso percorrendo de 1 até a altura total do tabuleiro, verificando para ver se aquela peça atual foi movida para baixo por uma quantidade adicional que resultaria em uma posição inválida no tabuleiro (isto é, passado o fundo ou se sobrepondo aos outros blocos.) Uma vez que encontramos esse ponto, basta definir a peça atual na linha acima desse ponto."""

                if event.key == K_ESCAPE:
                    terminate()

        # handle moving the block
        if (movingLeft or movingRight) and time.time() - lastMoveSidewaysTime > MOVESIDEWAYSFREQ:
            """The code above merely sets the movingLeft and movingRight variables. It doesn't actually move the blocks. This code here will do this. First we check if moveLeft or moveRight is set to True, and if more than MOVESIDEWAYSFREQ (a floating point number) seconds has elapsed since the last sideways move. Afterwards, we check if the new position of the piece would be valid and if so, we move the piece there.
            O código acima simplesmente define as variáveis movingLeft and movingRight. Na verdade, não move os blocos. Esse código aqui vai fazer isso. Primeiro vamos verificar se MoveLeft ou MoveRight estão definidos como True, e se mais de MOVESIDEWAYSFREQ (um número em ponto flutuante) segundos têm decorrido desde o último movimento para o lado. Depois, verificamos se a nova posição da peça seria válida e, nesse caso, movemos a peça para lá.
            Afterwards, we reset lastMoveSidewaysTime to the current time.
            Depois disso, redefinimos lastMoveSidewaysTime para o tempo atual. """
            if movingLeft and isValidPosition(board, currentPiece, adjX=-1):
                currentPiece['x'] -= 1
            if movingRight and isValidPosition(board, currentPiece, adjX=1):
                currentPiece['x'] += 1
            lastMoveSidewaysTime = time.time()

        if movingDown and time.time() - lastMoveDownTime > MOVEDOWNFREQ and isValidPosition(board, currentPiece, adjY=1):
            currentPiece['y'] += 1
            lastMoveDownTime = time.time()
            """Moving the piece downward is similar: we check if the down arrow key is pressed by looking at the movingDown varaible and if more than MOVEDOWNFREQ seconds have elapsed since the last time the piece moved down. And finally, if the new position is valid, the piece will fall down and we will reset lastMoveDownTime to the current time.
              Mover uma peça para baixo é semelhante: Verificamos se a seta para baixo foi pressionada olhando para a variável movingDown e se mais de MOVEDOWNFREQ segundos se passaram desde a última vez que a peça foi movida para baixo. E finalmente, se a nova posição é válida, a peça vai cair e vamos redefinir lastMoveDownTime para o tempo atual."""
        # let the piece fall if it is time to
        if time.time() - lastFallTime > fallFreq:
            # see if the piece has hit the bottom
            """While the above code moves the piece down if the player has pushed down the down arrow key, this code deals with the gradual falling that the piece does even if the player doesn't push anything. We call this "falling" in our code. (This is why we have two different variables to track the time: lastMoveDownTime and lastFallTime.)
               Enquanto o código acima move a peça para baixo se o jogador tiver empurrado para baixo a seta para baixo, este código trata da queda gradual que a peça faz mesmo se o jogador não forçar nada. Chamamos isso de "falling" no nosso código. (É por isso que temos duas variáveis diferentes para controlar o tempo:. lastMoveDownTime e lastFallTime).
               """
            if hasHitBottom(board, currentPiece):
                # set the piece on the board, and update the score, level, and fallFreq
                addToBoard(board, currentPiece)
                score += deleteCompleteLines(board)
                level = calculateLevel(score)
                fallFreq = calculateFallFreq(level)
                currentPiece = None
                """If the piece has landed on the bottom of the board or on top of the other piece, we need to copy it to the board data structure. Then we call deleteCompleteLines(), which handles getting rid of any complete lines and moving the blocks on top of that line down. The deleteCompleteLines() function will return an integer of how many lines were deleted, ranging from 0 (for no lines at all) to 4 (a full "tetris" move made with the long skinny "I" piece).
                   Se a peça foi parar no fundo do tabuleiro ou em cima de outra peça, é preciso copiá-la para a estrutura de dados do tabuleiro. Então chamamos deleteCompleteLines (), que trata de se livrar de todas as linhas completas e move os blocos de em cima da linha para baixo. A função deleteCompleteLines () irá retornar um número inteiro de quantas linhas foram excluídas, variando de 0 (nenhum em todas as linhas) a 4. 

                When this is done, we increase the score and recalculate the values for the level and fallFreq. Finally, we set currentPiece to None, which will tell the code at the beginning of the loop that we need to load a new current piece.
                Quando isto é feito, aumentamos a pontuação e recalculamos os valores para o nível e fallFreq. Finalmente, definimos currentPiece para None, que dirá ao código no início do loop que nós precisamos carregar uma nova peça. 
                """
            else:
                # just move the block down
                currentPiece['y'] += 1
                lastFallTime = time.time()
                """If the block hasn't landed, then we just push it down by one row and reset lastFallTime to the current time.
                   Se o bloco não tenha sido depositado, então apenas empurramos para baixo por uma linha e redefinimos lastFallTime para o tempo atual."""

        # drawing everything on the screen
        MAINSURF.fill(BGCOLOR)
        drawBoard(board)
        drawStatus(score, level)
        drawNextPiece(nextPiece)
        if currentPiece != None:
            drawPiece(currentPiece)
        """At the end of the main game loop, we draw the state of the board onto the screen. First we fill the entire MAINSURF surface with the background color so that we erase the image that was on it previously. Then we call our functions that draw the board, status text, next piece, and (if the current piece hasn't just landed) the current piece.
           No final do loop principal do jogo, desenhamos o estado do tabuleiro na tela. Primeiro preenchemos a superfície MAINSURF inteira com a cor de fundo para que possamos apagar a imagem que estava sobre ela anteriormente. Então chamamos as nossas funções que desenham o tabuleiro, o status do texto, a próxima peça, e (se a peça atual não foi depositada)a peça atual."""

        pygame.display.update()
        MAINCLOCK.tick(FPS)
        """Then we call pygame.display.update() to update the screen, and call MAINCLOCK.tick(FPS) to pause the program a little bit so the game doesn't run too fast.
           Então chamamos pygame.display.update() para atualizar a tela, e chamamos MAINCLOCK.tick(FPS) para suspender o programa um pouco para que o jogo não execute muito rápido."""


def calculateLevel(score):
    return int(score / 10) + 1


def calculateFallFreq(level):
    return 0.27 - (level * 0.02)

"""The code to calculate the level and falling frequency is done based on a simple equation.
   O código para calcular o nível e a frequência de queda é feita baseada em uma simples equação."""

def getNewPiece():
    # return a random new piece in a random rotation and color
    shape = random.choice(list(PIECES.keys()))
    """When generating a new random piece, first we randomly decide on which shape to use for the new piece. The keys() dictionary method will return a list of all the key values in the dictionary.
      Ao gerar uma nova peça aleatória, primeiro decidimos aleatoriamente sobre qual forma usar para a nova peça. O método keys() dictionary retornará uma lista de todos os valores-chave no dicionário. """
    newPiece = {'shape': shape,
                'rotation': random.randint(0, len(PIECES[shape]) - 1),
                'x': int(BOARDWIDTH / 2) - 2,
                'y': -2,
                'color': random.randint(0, len(COLORS)-1)}
    return newPiece


def addToBoard(board, piece):
    # fill in the spots on the board based on piece's location, shape, and rotation
    """Once the piece has landed, it needs to be added to the board's data structure. Using nested loops, we go through each of the 25 block spaces in the 5x5 data structure of the piece, and then add it to the corresponding spot on the board.
       Assim que a peça foi depositada, ele precisa ser adicionado à estrutura de dados do tabuleiro. Usando loops aninhados, passamos por cada um dos 25 espaços do bloco na estrutura de dados 5x5 da peça, e depois o adicionamos ao ponto correspondente no tabuleiro."""
    for x in range(5):
        for y in range(5):
            if PIECES[piece['shape']][piece['rotation']][x][y] != BLANK:
                """Note that PIECES is the large global dictionary that contains all the piece data. piece['shape'] stores the letter that corresponds to the piece type (such as 'S' or 'J'), so PIECES[piece['shape']] returns a list of all the different rotations of that shape. piece['rotation'] contains the index in this list of the specific rotation of a shape.
                Note que PIECES é o grande dicionário global que contém todos os dados da peça. piece['shape'] armazena a letra que corresponde ao tipo de peça (como o 'S' ou 'J'), assim PIECES[piece['shape']] retorna uma lista de todas as diferentes rotações daquela forma. piece['rotation'] contém o índice na lista da rotação específica de uma forma.
                So PIECES[piece['shape']][piece['rotation']] contains a value such as this one (remember, -1 (the value in the BLANK constant) represents a blank spot and a 1 value represents a filled spot:
                Então, PIECES[piece['shape']][piece['rotation']] contém um valor como este (lembre-se, -1 (o valor da constante BLANK) representa um ponto vazio e um valor 1 representa um ponto cheio:
               [[-1, -1, -1, -1, -1],
                [-1,  1,  1, -1, -1],
                [-1, -1,  1,  1, -1],
                [-1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1]]

              (This is after we transformed the block data from this value:)
               (Isto é depois que transformamos o bloco de dados a partir deste valor:)
               ['.....',
                '.OO..',
                '..OO.',
                '.....',
                '.....']

                Then the [x][y] indexes after it get the particular character in this data. If this value is BLANK, the the code continues on. Otherwise, the color integer of the piece is written to the corresponding xy coordinate on the board.
                 Então, os índices [x][y] após obter o caractere especial neste dados. Se esse valor estiver em branco, o código continua. Caso contrário, a cor da peça é escrita na correspondente coordenada xy no tabuleiro. """
                board[x + piece['x']][y + piece['y']] = piece['color']
                """The actual value that is added to the board is an integer representing the piece's color.
                   O valor atual que é adicionado ao tabuleiro é um inteiro que representa a cor da peça"""


def checkForKeyPress():
    # keep looping until the player has pressed a key
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                terminate()
            return event.key
    return None
    """This function will look at the event queue for any key press events and return the first one it finds. It also checks if the program is trying to quit, in which case, it calls terminate() to end the program.
     Esta função olhará em uma lista de eventos para todos os eventos teclados e retornará o primeiro que encontrar. Ele também verifica se o programa está tentando parar e, nesse caso, ele chama terminate () para finalizar o programa.
    You can also call this function and ignore the return value if you just want to pause the program until the user presses a key.
    Vc também pode chamar esta função e ignorar o valor de retorno se vc somente quer pausar o programa até o usuário pressionar uma tecla."""


def getNewBoard():
    # create and return a new blank board data structure
    board = []
    for i in range(BOARDWIDTH):
        board.append([BLANK] * BOARDHEIGHT)
    return board


def hasHitBottom(board, piece):
    # Returns True if the piece's bottom is currently on top of something
    for x in range(5):
        for y in range(5):
            if PIECES[piece['shape']][piece['rotation']][x][y] == BLANK or y + piece['y'] + 1 < 0:
                continue
            if y + piece['y'] + 1 == BOARDHEIGHT:
                return True
            if board[x + piece['x']][y + piece['y'] + 1] != BLANK:
                return True
    return False


def isOnBoard(x, y):
    # Returns True if the xy coordinates point to a block space that is on the board, and returns False if they are outside of the board.
    return x >= 0 and x < BOARDWIDTH and y < BOARDHEIGHT


def isValidPosition(board, piece, adjX=0, adjY=0):
    # Return True if the piece is within the board and not colliding with any blocks on the board.
    for x in range(5):
        for y in range(5):
            if y + piece['y'] + adjY < 0 or PIECES[piece['shape']][piece['rotation']][x][y] == BLANK:
                continue
            if not isOnBoard(x + piece['x'] + adjX, y + piece['y'] + adjY):
                return False
            if board[x + piece['x'] + adjX][y + piece['y'] + adjY] != BLANK:
                return False
    return True


def isCompleteLine(board, y):
    # Return True if the yth line from the top is filled with blocks with no gaps.
    for x in range(BOARDWIDTH):
        """The for loop checks each column in the y row to see if there are any blank spots. On the first blank spot it finds, it returns False.
           O laço for checa cada coluna na linha y para ver se existe algum ponto branco. No primeiro ponto branco encontrado, ele retorna False."""
        if board[x][y] == BLANK:
            return False
    return True
    """If the program execution gets past the loop, then we know that the y row is completely filled with blocks and will return True.
    Se a execução do programa passa o loop, então sabemos que a linha y está completamente preenchida com blocos e retornará True."""


def deleteCompleteLines(board):
    # Remove any completed lines on the board, move everything above them down, and return the number of complete lines.
    linesDeleted = 0
    y = BOARDHEIGHT - 1
    while y >= 0:
        if isCompleteLine(board, y):
            # Remove the line and pull everything above it down by one line.
            linesDeleted += 1
            for pullDownY in range(y, 0, -1):
                for x in range(BOARDWIDTH):
                    board[x][pullDownY] = board[x][pullDownY-1]
            # Set very top line to blank.
            for x in range(BOARDWIDTH):
                board[x][0] = BLANK
        else:
            y -= 1
    return linesDeleted

def convertToPixelCoords(x, y):
    # Convert the given xy coordinates of the board to xy coordinates of the location on the screen.
    return (XMARGIN + (x * BLOCKSIZE)), (TOPOFBOARD + (y * BLOCKSIZE))
    """Remember that we are dealing with two cartesian coordinate systems here. One for the block spaces on the board, which go from 0 to BOARDWIDTH and 0 to BOARDHEIGHT. And another system for the pixels on the window, going from 0 to WINDOWWIDTH and 0 to WINDOWHEIGHT. We use the block coordinates for the board data structure, but Pygame only understands the window coordinates whenever we want to draw something to the screen.
    Lembrando que estamos lidando com dois sistemas de coordenadas cartesianas aqui. Um para o espaço de blocos no tabuleiro, que vai de 0 até BOARDWIDTH e de 0 até BOARDHEIGHT. E o outro sistema para os pixels na janela, indo desde 0 até WINDOWWIDTH e de 0 até WINDOWHEIGHT. Usamos as coordenadas do bloco para a estrutura de dados do tabuleiro, mas Pygame somente entende as coordenadas da janela quando queremos desenhar alguma coisa na tela.

    This is where convertToPixelCoords comes in. It takes an xy coordinate values from the block coordinate system and converts them to the pixel xy coordinates that the window and Pygame drawing functions use.
    Este é o lugar onde convertToPixelCoords vem. Pega-se os valores xy das coordenadas a partir sistema de coordenadas do bloco e converte-os para as coordenadas xy de pixel daquela janela e o Pygame desenha as funções em uso"""


def drawBoardBorder():
    # draw the border around the board
    pygame.draw.rect(MAINSURF, BORDERCOLOR, (XMARGIN - 3, TOPOFBOARD - 7, (BOARDWIDTH * BLOCKSIZE) + 8, (BOARDHEIGHT * BLOCKSIZE) + 8), 5)
    """This line draws a solid rectangle of the background color over the board, erasing any previous drawing.
    Esta linha desenha um retângulo sólido da cor de fundo sobre o tabuleiro, apagando desenhos anteriores.
    
    The parameters for pygame.draw.rect are: the pygame.Surface object to draw the rectangle on, the color to use, a tuple of four number values (top, left, width, and height in pixels), and optionally the width of the rectangle's line. If the line width parameter is omitted, then a solid rectangle will be drawn instead of just an outline.
    Os parâmetros para pygame.draw.rect  são: o objeto pygame.Surface para desenhar o retangulo, a cor para usar, uma tupla de 4 números (topo, esquerda, largura, e altura em pixels), e, opcionalmente, a largura da linha do retângulo. Se o parâmetro da largura da linha é omitido, então um retângulo sólido será desenhado em vez de somente o contorno."""

def drawBoard(board):
    drawBoardBorder()
    # fill the background of the board
    pygame.draw.rect(MAINSURF, BGCOLOR, (XMARGIN, TOPOFBOARD, BLOCKSIZE * BOARDWIDTH, BLOCKSIZE * BOARDHEIGHT))
    # draw the individual blocks on the board
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if board[x][y] != BLANK:
                pixelx, pixely = convertToPixelCoords(x, y)
                pygame.draw.rect(MAINSURF, COLORS[board[x][y]], (pixelx+1, pixely+1, BLOCKSIZE-1, BLOCKSIZE-1))
                """Next, we want to draw each block that is on the board. Recall that the board data structure is a list of list such that the value at board[x][y] is set to BLANK if the xy block space does not have a block in it, and set to an integer which is an index in the COLORS list if there is a block. The specific integer determines what color the block at that position is.
                Em seguida, queremos desenhar cada bloco que está sobre o tabuleiro. Lembre-se que a estrutura de dados do tabuleiro é uma lista de listas na qual o valor em board[x][y] definido como BLANK se o espaço de blocos em xy não tem o bloco nele, e definimos para um inteiro que é um índice na lista COLORS se existe um bloco. O inteiro especifico determina qual a cor do bloco e em qual posição está. 

                The two nested for loops will loop through every possible xy board coordinate. If the block space is blank, then the if statement's condition (board[x][u] != BLANK) will be False and the code simply continues to the next iteration. Otherwise, after converting from board coordinates to the pixel coordinates, we draw the block in the correct position with the correct color. Note that the blocks are always BLOCKSIZE in pixels for width and height.
                Os dois loops for aninhados percorrerão todas as possíveis direções de coordenadas xy. Se o espaço do bloco está em branco, então a condição if (board[x][u]!= BLANK) será False e o código simplesmente continua até a próxima iteração. Caso contrário, após a conversão das coordenadas do tabuleiro para as coordenadas do pixel, desenhamos o bloco na posição correta com a cor correta. Observe que os blocos são sempre BLOCKSIZE em pixels para a largura e altura. """

def drawStatus(score, level):
    # draw the score text
    """The code to render and draw the text is similar to the code in showTextScreen(), except here we do it to display the current score and level that the player is on.
       O código para processar e desenhar o texto é similar ao código em showTextScreen(), exceto que aqui fazemos isto para mostrar a pontuação atual e o nível que o jogador está."""
    scoreSurf = BASICFONT.render('Score: %s' % score, True, WHITE)
    scoreRect = scoreSurf.get_rect()

    scoreRect.topleft = (WINDOWWIDTH - 150, 20)
    MAINSURF.blit(scoreSurf, scoreRect)

    # draw the level text
    levelSurf = BASICFONT.render('Level: %s' % level, True, WHITE)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (WINDOWWIDTH - 150, 50)
    MAINSURF.blit(levelSurf, levelRect)

def drawNextPiece(piece):
    # draw the "next" text
    """This function is similar to the drawPiece() function, except that ignores the location data in the piece data structure (since the "next piece" is not drawn on the board) and instead calls drawPiece() with some custom coordinates.
    Esta função é similar a função drawPiece(), exceto que ignora a localização dos dados na estrutura de dados da peça (uma vez que "next piece" não é desenhado no tabuleiro) e em vez disso chamando drawPiece() com algumas coordenadas personalizadas.

    The code that draws the "Next:" text is similar to the code in showTextScreen() and drawStatus().
    O código que desenha o texto "Next:" é similiar ao código em showTextScreen() and drawStatus()."""
    nextSurf = BASICFONT.render('Next:', True, WHITE)
    nextRect = nextSurf.get_rect()
    nextRect.topleft = (WINDOWWIDTH - 120, 80)
    MAINSURF.blit(nextSurf, nextRect)

    drawPiece(piece, customCoords=(WINDOWWIDTH-120, 100))

def drawPiece(piece, customCoords=(None, None)):
    """Normally drawPiece() will draw the piece based on the board xy coordinates that are stored inside the piece data structure itself. However, for the "next piece" piece, we want to draw it at a specific xy pixel coordinates on the window, rather than convert the board xy coordinates to pixel coordinates.
    Normalmente drawPiece()desenhará a peça baseada nas coordenadas xy que estão armazenadas dentro da propria estrutura de dados da peça. Todavia, para a peça "next piece", queremos desenhá-la em coordenada de pixel especifica sobre a janela, ao invés de converter as coordenadas xy do tabuleiro para as coordenadas de pixels.

    This is where the customCoords parameter comes in. If the function call to drawPiece() does not include a second parameter, then the customCoords parameter will by default have the value (None, None). This will indicate to the if statement that the coordinates to use are stored in the piece data structure (which will have to be converted to the pixel coordinates with convertToPixelCoords().
    Aqui é onde o parâmetro customCoords vem. Se a função que chama drawPiece() não inclui um segundo parâmetro, então o parâmetro customCoords será default e terá o valor (None, None). Isto indica se a declaração que as coordenadas para utilização está armazenada na estrutura de dados da peça (que terá de ser convertido para as coordenadas do pixel com convertToPixelCoords ()."""
    shapeToDraw = PIECES[piece['shape']][piece['rotation']]
    if customCoords == (None, None):
        # if customCoords hasn't been specified, use the location stored in the piece data structure
        pixelx, pixely = convertToPixelCoords(piece['x'], piece['y'])
    else:
        pixelx, pixely = customCoords

    # draw each of the blocks that make up the piece
    for x in range(5):
        for y in range(5):
            """These nested for loops will go through all 25 of the possible block spaces in the piece data structure, and for all non-blank values it will draw the block to the screen using Pygame's pygame.draw.rect() function.
             Estes loops for aninhados percorrerão todos os 25 possíveis espaços na estrutura de dados da peça, e para todos os valores não-brancos desenhará o bloco na tela usando a função pygame.draw.rect()."""
            if shapeToDraw[x][y] != BLANK:
                pygame.draw.rect(MAINSURF, COLORS[piece['color']], (pixelx + (x * BLOCKSIZE) + 1, pixely + (y * BLOCKSIZE) + 1, BLOCKSIZE-1, BLOCKSIZE-1))


if __name__ == '__main__':
    main()
