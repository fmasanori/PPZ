# Slide Puzzle
# http://inventwithpython.com/blog
# By Al Sweigart al@inventwithpython.com

"""
Welcome to the Code Comments for Puzzle. Code Comments is a series of simple games with detailed comments in the source code, so you can see how the game works.
Bem vindo aos Códigos Comentados para Puzzle. Códigos Comentados é uma série de games(jogos) simples com comentários detalhados no código fonte, assim você pode ver como o game(jogo) trabalha.

The text in between the triple-double-quotes are comments. The Python interpreter ignores any text in between them, so we can add any comments about the source code without affecting the program. In general for Code Comments, the comments will describe the lines of code above the comment. It helps to view this file either on the Code Comments site or with a text editor that does "syntax highlighting", so that the comments appear in a separate color and are easier to distinguish from the code.
O texto entre aspas duplas-triplas são comentários. O interpretador do Python ignora qualquer texto entre elas, assim nós podemos adicionar qualquer comentário sobre o código fonte sem afetar o programa. Em geral nos Códigos Comentados, os comentários descreverão as linhas do código acima do comentário. Isto irá ajudá-lo a visualizar este arquivo no site Code Comments ou com um editor de texto que destaca a sintaxe, de modo que os comentários aparecem em uma cor diferente e são fáceis de distinguí-los do código.

This Code Comments assumes you know some basic Python programming. If you are a beginner and would like to learn computer programming, there is a free book online called "Invent Your Own Computer Games with Python" at http://inventwithpython.com
Este Código Comentado assume que você tenha algum conhecimento básico sobre a linguagem Python. Se você é um iniciante e gostaria de aprender programação de computadores, existe um livro grátis(free) online chamado "Invent Your Own Computer Games with Python" disponível no site http://inventwithpython.com

The Code Comments programs make references to sections of this book throughout the program. This Code Comments can also teach you how to use the Pygame library to make your own games with graphics, animation, and sound. You can download Pygame from http://pygame.org and view its documentation at http://pygame.org/docs/
Os programas dos Códigos Comentados fazem referência à seções deste livro em todo o programa. Estes Códigos Comentados também podem te ensinar  a como usar a biblioteca Pygame para fazer seus próprios games com gráficos, animações e sons. Você pode fazer o download do Pygame no site: http://pygame.org e visualizar sua documentação em: http://pygame.org/docs/

HOW TO PLAY SLIDE PUZZLE
Como jogar PUZZLE
There are 15 tiles in a 4x4 grid. At the start of the game, the tiles are randomly switched around the board to generate a new puzzle. When the puzzle is ready, start sliding around the tilees to reorder the tiles.
Existem 15 peças em uma grade 4 x 4. Ao iniciar o jogo, as peças são aleatoriamente distribuidas no tabulero para gerar um novo quebra-cabeça. Quando o quebra-cabeça está pronto, começe a deslizar as peças para reodená-las.
"""

import pygame, sys, random, time
from pygame.locals import *
"""Here we import modules that our game needs. random has random number functions, time has the sleep() function, sys has the exit() function, and pygame contains all the pygame-related functions.
Aqui nós importamos módulos que ser game precisa. random tem funções de números aleatórios, time tem a função sleep(), sys tem a função exit(), e pygame contém todas as funções relacionadas ao paygame.

pygame.locals contains constants like MOUSEMOTION and MOUSEBUTTONUP and QUIT for the events. It's easier to type MOUSEBUTTONUP instead of pygame.locals.MOUSEBUTTONUP, so we use the "from pygame.locals import *" format to import these to the local namespace.
pygame.locals contém constantes como MOUSEMOTION e MOUSEBUTTONUP e QUIT para os eventos. É mais fácil digitar  MOUSEBUTTONUP em vez de pygame.locals.MOUSEBUTTONUP, assim usamos o formato "from pygame.locals import *" para importar estes para o local namespace.
"""

# Create the constants (change these to different values to modify the game.)
COLS = 4
ROWS = 4
TILESIZE = 80
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FPS = 30
"""These constant variables (the uppercase names means we shouldn't change the values stored in them) set some standard values for our game. You can play around with different values for them (though some values might cause bugs in the game.) By using constants instead of the values directly, it is easier to make changes since we only have to change them in one place.
Estas variáveis constantes (os nomes em letras maiúsculas significa que não podemos mudar o valor armazenado nelas) define alguns valores padrão para o nosso jogo. Você pode jogar com valores diferentes para eles (no entanto alguns valores podem causar erros no jogo). Usando constantes ao invés dos valores diretamente, é mais fácil fazar mudanças e então somente temos que mudá-las em um lugar.

For example, if we used 80 instead of TILESIZE, then if we wanted to change our code later we'd have to change every place in the code we find 80. This is trickier than just changing the one line where MAXLIFE is originally set.
Por exemplo, se usamos 80 ao invés de TILESIZE, então se quisermos mudar nosso código mais tarde, teremos que mudar todos os lugares no código onde encontramos 80. Isto é mais complicado do que apenas mudar a linha onde o MAXLIFE está originalmente definido.

More information about constants is at http://inventwithpython.com/chapter9.html#ConstantVariables
Mais informação sobre constantes em: http://inventwithpython.com/chapter9.html#ConstantVariables
"""

# Create the color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BRIGHTBLUE = (0, 50, 255)
BLUE = (0, 153, 153)
GREEN = (0, 204, 0)

BGCOLOR = BLUE
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BORDERCOLOR = BRIGHTBLUE
FONTSIZE = 20

BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK
MESSAGECOLOR = WHITE
"""We also set up some constant values for different colors. Pygame uses tuples of three integers to represent color. The integers represent the amount of red, green, and blue in the color (this is commonly called a RGB). 0 means there is none of the primary color in the color, and 255 means there is the maximum amount. So (255, 0, 0) is red, since it has the maximum amount of red but no green or blue. But (255, 0, 255) adds the max amount of blue with the red, creating purple.
Também podemos definir alguns valores constantes para diferentes cores. Pygame usa tuplas de 3 inteiros para representar a cor. Os inteiros representam a quantidade de vermelho, verde e azul na cor (isto é comumente chamado RGB). 0 significa que não existe nada de cor primária na cor e 255 significa que existe uma quantidade máxima. Assim, (255, 0, 0) é vermelho, já que ele tem a quantidade máxima de vermelho e não tem nada de verde ou azul. Mas, (255, 0, 255) adiciona a quantidade máxima de azul com vermelho, criando a cor pupura.

More information about colors is at http://inventwithpython.com/chapter17.html#ColorsinPygame
Mais informação sobre cores está disponível em: http://inventwithpython.com/chapter17.html#ColorsinPygame

"""

# Other constants and global variables.
RESET_SURF = None
RESET_RECT = None
NEW_SURF = None
NEW_RECT = None
SOLVE_SURF = None
SOLVE_RECT = None

XMARGIN = int((WINDOWWIDTH - (TILESIZE * COLS + (COLS - 1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (TILESIZE * ROWS + (ROWS - 1))) / 2)
"""We need to calculate the amount of space that is on the side of the tiles. We do this by taking the size of the window, subtract the width of the tiles (times the number of columns of tiles). But we also want to take into account the pixels in between the tiles. These gaps are one pixel in size each, and there are (COLS - 1) of them. So we subtract this value from the window width too. Then, since there are two margins on either side of the tiles, we divide the number we have by 2.
Precisamos calcular a quantidade de espaço que está sobre o lado das peças. Fazemos isto pegando o tamanho da janela, subtraindo a largura das peças (vezes o número de colunas das peças). Mas também queremos pegar a quantidade de pixels entre as peças. Estas lacunas são um pixel em cada tamanho e existem (COLS -1) deles. Assim, subtraimos este valor da largura da janela também. Então, já que existem duas margens sobre o lado das peças, dividimos o número que temos por 2.

We do the same for the Y margin.
Fazemos o mesmo para a margem Y. """

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

"""We need values for each of the directions up, down, left, and right in our program. These can be any four distinct values, as long as they are used consistently it won't matter to our program. We could use the strings 'up', 'down', etc. Instead, we'll use constant variables.
Precisamos de valores para cada direção acima, abaixo, esquerda e direita em nosso programa. Estes podem ser quaisquer quatro valores distintos, enquanto eles forem utilizados de forma consistente não causará problemas para nosso programa. Poderiamos usar as strings 'up','down', etc. Mas, em vez disso usaremos variáveis constantes.

The difference is if we make a typo using the strings, Python won't crash but it will still cause a bug. For instance, if we had this bit of code:
    if direction == 'dwon':
    A diferença é que se cometermos um erro de digitação usando string, Python não vai parar a execução, mas seguirá com o erro. Por exemplo, se temos este bit de código:
    if direction == 'dwon':

...então o programa continuará executando, mas contém um erro porque se a variável direção foi definida como 'down', esta condição vai ser avaliada como False (que não é como queremos que o código se comporte).

...then the program will still run, but it would contain a bug because if the direction variable was set to 'down', this condition would still evaluate to False (which is not how we'd want the code to behave).

But if we use constant values instead and make a similar typo:
    if direction == DWON:
    Mas se em vez disso usarmos valores constantes e cometermos um erro similar de digitação:
    if direction == DWON:

... então Python falha quando se depara com esta linha porque não há variavel definida como DWON, mas somente como DOWN. Porque está falha seria uma coisa boa? Bem, não é, mas neste caso seria porque imediatamente vai alertar-nos que há um problema e nós poderemos consertá-lo. Se tivessemos usado uma string ao invés disso, isto poderia demorar algum tempo até descobrirmos onde estava a causa do erro. Usando constantes desta maneira, nos ajudará a garantir que nosso programa trabalhe corretamente.
...then Python crashes when it comes across this line because there is no such variable as DWON, just DOWN. Why is crashing a good thing? Well, it's not, but in this case it would immediately alert us that there is a problem, and we could fix it. If we had used a string instead, it might take a while to track down where the bug is caused. Using constants in this way helps us ensure that our program works correctly.
"""

def main():
    global MAINCLOCK, MAINSURF, FONT, RESET_SURF, RESET_RECT, NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT
    """The main() function is where our program begins. (See the last two lines of code to see why.) Because we define MAINCLOCK and MAINSURF inside this function, these are local variables to the main() function and the names MAINCLOCK and MAINSURF won't exist outside of this function. By using a global statement, we can tell Python that we want these variables to be global variables.
    A função main() é onde nosso programa começa. (Veja as duas ultimas linhas do código para entender o porquê). Porque definimos MAINCLOCK e MAINSURF  dentro desta função, elas são variáveis locais a função main() e os nomes MAINCLOCK e MAINSURF não existem fora desta função. Ao usar uma declaração global, podemos dizer ao Python que queremos que estas variáveis sejam variáveis globais.

    More information about global and local variables is at http://inventwithpython.com/chapter6.html#VariableScope
    Mais informação sobre variáveis locais e globais em :  http://inventwithpython.com/chapter6.html#VariableScope
    
    """

    pygame.init()
    MAINCLOCK = pygame.time.Clock()
    MAINSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Slide Puzzle')

    """pygame.init() needs to be called before any of the other Pygame functions.
    pygame.init() precisa ser chamado antes de qualquer outra função Pygame.
    
    pygame.time.Clock() returns a pygame.Clock object. We will use this object's tick() method to ensure that the program runs at no faster than 30 frames per second (or whatever integer value we have in the FPS constant.)
    pygame.time.Clock() retorna o objeto pygame.Clock. Usaremos este objeto com o metodo tick() para garantir que o programa não seja executado em mais de 30 frames por segundo (ou qualquer outro valor inteiro que temos na constante FPS.)
    
    pygame.display.set_mode() creates the window on the screen and returns a pygame.Surface object. Any drawing done on this Surface object with the pygame.draw.* functions will be displayed on the screen when we call pygame.display.update().
    pygame.display.set_mode() cria a janela na tela e retorna um objeto pygame.Surface. Todo o desenho feito sobre a superfície deste objeto com as funções pygame.draw.* serão mostradas na tela quando chamamos pygame.display.update().
    
    More information about pygame.display.set_mode() is at http://inventwithpython.com/chapter17.html#ThepygamedisplaysetmodeandpygamedisplaysetcaptionFunctions
    Mais informação sobre pygame.display.set_mode() está em: http://inventwithpython.com/chapter17.html#ThepygamedisplaysetmodeandpygamedisplaysetcaptionFunctions"""

    FONT = pygame.font.Font('freesansbold.ttf', FONTSIZE)
    """This line loads a font to use for drawing text. Since our game only uses one font (and at one size, 16 points) we only have to make one call to the pygame.font.Font() constructor function. We will store this font in the global variable FONT.
       Esta linha carrega uma fonte para usar para desenhar o texto. Já que nosso jogo usa somente uma fonte (e em um tamanho, 16 points) somente temos que fazer uma chamada a função pygame.font.Font(). Armazenaremos esta fonte na variável global FONT. """
    
    # Store the option buttons and their rectangles in OPTIONS.
    RESET_SURF, RESET_RECT = makeText('Reset', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 90)
    NEW_SURF, NEW_RECT = makeText('New Game', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 60)
    SOLVE_SURF, SOLVE_RECT = makeText('Solve', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 30)
    """Our program needs three buttons for reset the game, starting a new game, and solving the current puzzle. The data for these buttons will be made by our makeText() function, which is described later. makeText() will return two objects, a surface object that contains the text and a rectangle object that contains the position and size data of the button.
     Nosso prgrama precisa de três botões: um para reiniciar o jogo, um para iniciar um novo jogo e outro para resolver o atual quebra-cabeça. Os dados para esses botões serão definidos pela nossa função makeText(), que será descrito mais tarde. makeText() retornará dois objetos, o objeto superfície que contém o texto e um objeto retângulo que contém a posição e o tamanho dos dados do botão.

     Here we are just creating the objects for the button. We will display them on the screen in the drawBoard() function.
    Aqui nós criamos os objetos para o botão. Mostraremos eles na tela na função drawBoard()."""

    mainBoard, solutionSeq = generateNewPuzzle(80)
    """generateNewPuzzle() will create a new puzzle by creating a new data structure for our board and then randomly sliding the puzzle around 100 times. It will remember the sequence of slides it made and return that along with the board data structure.
       generateNewPuzzle() criará um novo quebra-cabeça criando uma nova estrutura de dados para nosso tabuleiro e então deslizando aleatoriamente o quebra-cabeça em torno de 100 vezes. Lembrará a sequência de slides que fez e retorna juntamente com a estrutura de dados do tabuleiro.
       
    The structure of the board data structure is described in detail in generateNewPuzzle(), but basically it's a list of list of integers, where the integers correspond to the number on the tile and the 0 integer stands for the blank space.
    A estrutura da estrutura de dados do tabuleiro é descrita em detalhes em generateNewPuzzle(), mas basicamente ela é uma lista de inteiros, onde os inteiros correspondem ao número sobre o ladrilho e o inteiro 0 para o espaço em branco.
    
    Since we keep a record of the slides that were made, we could always do the reverse of those slides to get the board back to its original state. This is how we "solve" the board when the player pushes on the Solve button.
    Já que mantemos um registro dos deslocamentos que foram feitos, sempre podemos fazer o inverso destes deslocamentos para obter o tabuleiro de volta ao seu estado original. Isto é como "resolvemos" o tabuleiro quando o jogador pressiona o botão Solve."""                                             
    
    solvedBoard = getStartingBoard() # a solved board is the same as the board in a start state.
    """We're going to make a board that is in the ordered, starting state around so we can compare it to the board that is displayed on the screen (that is, mainBoard). If these two boards are equal, we know that the player has solved the board.
       Vamos fazer um tabuleiro que está no pedido, iniciando em torno do estado para que possamos compará-lo ao tabuleiro que é exibido na tela (ou seja, tabuleiro-principal). Se estes dois tabuleiros são iguais, sabemos que o jogador resolveu o tabuleiro."""
         
    seq = []
    """We are also going to keep a record of the player's slides, so we can revert back to the start of the puzzle if the player wants. (We also need to know this if we want to automatically solve the puzzle.
       Também vamos manter um registro dos deslocamentos do jogador, para que possamos voltar ao início do quebra-cabeça se o jogador quiser.(Também precisamos saber disto, caso desejarmos automaticamente resolver o quebra-cabeça). """
       
    while True:
        # The main game loop.
        sliding = None
        msg = ''
        if mainBoard == solvedBoard:
            msg = 'Solved!'
        """This is the main game loop, which constantly loops while the program is playing. In this loop, we display the board on the screen and also handle any input events from the player. The sliding variable will keep track of which direction we should slide the tiles. We have a separate variable for this so that we can treat input from the mouse and the keyboard the same way.
        Este é o laço (loop) principal do jogo, que constantemente executa enquanto o programa está jogando. Neste laço, mostramos o tabuleiro na tela e também lidamos com os eventos de entrada do jogador. A variável de deslocamento irá acompanhar a direção que devemos deslocar as peças. Temos uma variável específica para isso, para que possamos tratar a entrada do mouse e do teclado da mesma forma.
        We also want to display a text message at the top left corner of the window for various reasons. We will use the msg variable to store this string. If the board happens to be in the solved state, then we want the text message to be Solved!
        Também queremos mostrar uma mensagem de texto no canto superior esquerdo da janela por varias razões. Usaremos a variável msg para armazenar esta string. Se o tabuleiro passar a estar no estado resolvido, então queremos que a mensagem de texto seja "resolvido"(Solved)!"""
        
        drawBoard(mainBoard, message=msg)
        """On each iteration we want to draw the current state of the board on the screen (along with any text message). Since the game loop runs 30 times a seconds (unless the computer is too slow or yo have changed the value in the FPS variable), we are constantly drawing the latest board to the screen.
          Sobre cada iteração desejamos desenhar o estado atual do tabuleiro na tela (juntamente com qualquer mensagem de texto). Uma vez que o laço do jogo é executado 30 vezes por segundo (a menos que o computador esteja muito lento ou você tenha alterado o valor na variável FPS), estamos constantemente desenhando o último tabuleiro na tela."""  
          
        # Handle any events.
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == MOUSEBUTTONUP:
                spotClicked = getSpotClicked(mainBoard, event.pos[0], event.pos[1])
                """When the MOUSEBUTTONUP is created, we check if the mouse is currently over one of the tiles (otherwise we can ignore it.) The bulk of this is implemented inside our getSpotClicked() function. This function returns None if the mouse wasn't over a button, or it returns the color value of the button.
                Quando o MOUSEBUTTONUP é criado, checamos se o mouse está atualmente sobre um dos ladrilhos (caso contrário podemos ignorá-lo). A maior parte disto está implementada dentro da nossa função getSpotClicked(). Esta função retorna nada (none) se o mouse não estiver sobre nenhum botão, ou retorna o valor da cor do botão"""
                
                if spotClicked is not None:
                    spotx, spoty = spotClicked
                    """If getSpotClicked() did not return None, then this means the place on the window the player clicked was a spot (as opposed to somewhere in the margins).
                       Se getSpotClicked() retornar nada, então isto significa que o lugar clicado na janela do jogador foi um ponto (como oposto a algum lugar nas margens)."""
                    blankx, blanky = getBlankPosition(mainBoard)
                    """We also need to find out where the blank spot currently is on the board. We'll get the xy coordinates of this spot from getBlankPosition().
                       Também precisamos encontrar onde está o ponto vazio atualmente no tabuleiro. Pegamos as coordenadas xy deste ponto a partir de getBlankPosition()."""

                    if spotx == blankx + 1 and spoty == blanky:
                        sliding = LEFT
                    if spotx == blankx - 1 and spoty == blanky:
                        sliding = RIGHT
                    if spotx == blankx and spoty == blanky + 1:
                        sliding = UP
                    if spotx == blankx and spoty == blanky - 1:
                        sliding = DOWN
                    """Now we find out if the spot that the player clicked on is located next to the blank spot. We should slide a tile to the left if the blank spot is on its left, and slide the tile up if the blank space is above it, and so on.
                       Agora encontraremos se o ponto clicado pelo jogador está localizado próximo ao ponto vazio. Devemos deslocar uma peça para a esquerda, se o espaço em branco está em sua esquerda, e deslizar a peça até o espaço em branco, se está acima dela e assim por diante."""
                else:
                    # check if the user clicked on one of the option buttons
                    if RESET_RECT.collidepoint(event.pos[0], event.pos[1]):
                        resetAnimation(mainBoard, seq)
                        seq = []
                        """Here we use the pygame.Rect object's collidepoint() method to find out if the x and y coordinates of the mouse click (which are in event.pos[0] and event.pos[1], respectively) are inside the rectangular area that the "reset" button occupies. If so, then we want to reset all the tiles back to their original configuration. We do this by passing resetAnimation() the sequence of moves made by the player so far (which is in the seq list). Of course, afterwards we'll want to set the seq list back to a blank list, since now the board is as though the player never made any moves at all.
                           Aqui usamos o objeto pygame.Rect do método collidepoint() para encontrar se as coordenadas x e y do clique do mouse (que estão em event.pos[0] e event.pos[1], respectivamente) estão dentro da área retangular que o botão "reset" ocupa. Se sim, queremos então reiniciar todos os ladrilhos e voltar a sua configuração original.Fazemos isto passando resetAnimation() a sequencia de movimentos feitos pelo jogador até o momento (que está na lista seq). É claro, depois vamos querer definir a lista seq de volta como uma lista vazia, a partir de agora é tabuleiro está como se o jogador nunca tivesse feito qualquer movimento em tudo. """
                                                
                    if NEW_RECT.collidepoint(event.pos[0], event.pos[1]):
                        mainBoard, solutionSeq = generateNewPuzzle(80)
                        seq = []
                        """This code handles what happens when the user's mouse click was inside the "new game" button. Here we are going to start a brand new game, so we replace the board data structure stored in mainBoard and the sequence of moves to solve it in the solutionSeq list. We also want to reset the seq list since the player is starting a new game.
                           Este codigo manipula o que acontece quando o usuário clica o mouse no botão "new game". Aqui vamos começar um novo jogo, por isso substituimos a estrutura de dados do tabuleiro armazenada no tabuleiro principal e a sequência de movimentos para resolvê-la na lista solutionSeq. Também queremos reiniciar a lista "seq" já que o jogador está começando um novo jogo."""
                           
                    if SOLVE_RECT.collidepoint(event.pos[0], event.pos[1]):
                        resetAnimation(mainBoard, solutionSeq + seq)
                        seq = []
                        """Here we check if the player has clicked on the "solve" button, in which case we do almost the same code as the "reset" button case. Except for this, instead of just reseting the sequence of steps the player has made (that is, the seq list) we reset the steps of the solution including the steps the player has made (solutionSeq + seq). This will reset the board back to the ordered starting board.
                       Aqui checamos se o jogador clicou sobre o botão "solve", em que fazemos quase o mesmo código conforme o caso do botão "reset". Exceto por isto, ao invés de somente reiniciar a sequência de passos que o jogador fez (isto é, a lista seq) reiniciamos os passos da solução incluindo os passos feitos pelo jogador (solutionSeq + seq). Isto irá redefinir o tabuleiro e voltará a iniciar o tabuleiro ordenado.
                           
                        If the player wants a new puzzle, they will have to click the "new game" button to generate a new random puzzle.
                        Se o jogador deseja um novo quebra-cabeça, ele terá que clicar no botão "new game" para gerar um novo quebra-cabeça aleatório."""

            if event.type == KEYUP:
                """The previous code checked what happens in the event that the user clicked the mouse (MOUSEBUTTONUP), while this code will handle what happens when the user presses a keyboard key. The key value that you can compare event.key to is stored in Pygame's own set of constants that have the format K_*, where the * is the letter of the key. In the case of the Esc key, it is K_ESCAPE.
                   O código anterior checa o que ocorre no evento que o usuário clicou o mouse (MOUSEBUTTONUP), enquanto este código manipulará o que ocorre quando o usuário pressiona uma tecla do teclado. O valor da tecla event.key que vc pode comparar está armazenada no Pygame's no conjunto de constantes que têm o formato K_*. onde o * é a letra da tecla. No caso da tecla Esc, ela é K_ESCAPE.  
                   
                We need to call isValidMove() to make sure that the board is in a state where this move is allowed. Otherwise we would start sliding tiles off the board and cause bugs.                                    
                Precisamos chamar isValidMove() para garantir que o tabuleiro está em um estado onde este movimento é permitido. Caso contrário teriamos que começar a deslizar peças do tabuleiro e causaria erros. """

                if (event.key == K_LEFT or event.key == K_a) and isValidMove(mainBoard, LEFT):
                    sliding = LEFT
                if (event.key == K_RIGHT or event.key == K_d) and isValidMove(mainBoard, RIGHT):
                    sliding = RIGHT
                if (event.key == K_UP or event.key == K_w) and isValidMove(mainBoard, UP):
                    sliding = UP
                if (event.key == K_DOWN or event.key == K_s) and isValidMove(mainBoard, DOWN):
                    sliding = DOWN
                if event.key == K_ESCAPE:
                    terminate()
                if event.key == K_r:
                    resetAnimation(board, moves)

        if sliding:
            slideAnimation(mainBoard, sliding)
            makeMove(mainBoard, sliding)
            seq.append(sliding)
            """The sliding variable will not be None if the player specified (either through the keyboard or with the mouse) that we should slide the tiles. First we play the animation of the tile moving over, then we update the board data structure, and then we add this recent move to the list of moves the player has made in the seq list.
               A variável sliding não será vazia (None) se o jogador especificar (ou através do teclado ou com o mouse) que deveremos deslizar as peças. Primeiro jogamos uma animação da peça se movendo, então atualizamos a estrutura de dados do tabuleiro e então adicionamos este recente movimento a lista de movimentos que o jogador tem feito na lista seq."""
        pygame.display.update()
        MAINCLOCK.tick(FPS)


def terminate():
    """In order to terminate the program, we must call both pygame.quit() (to shut down the Pygame engine) and sys.exit() (to shut down the program.) Calling sys.exit() without calling pygame.quit() first probably won't harm anything, though it does give IDLE some problems if the user runs this program from it. It's just considered a graceful way to shut down the Pygame library.
       Com o objetivo de terminar o programa, devemos chamar ambos pygame.quit() (para desligar o mecanismo Pygame) e sys.exit() (para desligar o programa). Chamar sys.exit() sem primeiro chamar pygame.quit() provavelmente não vai prejudicar nada, embora ele dê alguns problemas IDLE se o usuário executar este programa a partir dele. É apenas considerada uma maneira graciosa para encerrar a biblioteca Pygame. """
         
    pygame.quit()
    sys.exit()


def getStartingBoard():
    """This function creates a data structure that represents a state of the board. We will use a list of list of integers, where theBoard[2][3] would contain the integer that represents the spot on the board that is 3rd from the left and 4th from the top (remember, the indexes start at 0.) This mimics the coordinate system used by the screen, where the 0, 0 origin is at the top left corner.
       Esta função cria uma estrutura de dados que representa um estado do tabuleiro. Usaremos uma lista de lista de inteiros, onde theBoard[2][3] deve conter o inteiro que representa o ponto do tabuleiro que é 3rd a partir da esquerda e 4th desde o topo (lembrando, o índice começa em 0 .) Isto imita o sistema de coordenadas usado pela tela, onde a origem 0, 0 está no canto superior esquerdo.
       
    The integers represent the numbered tiles, so if theBoard[2][3] held the integer 12, then the "12" tile is located at the spot 3rd from the left and 4th from the top. The 0 integer will be used to represent the blank spot.
    Os inteiros representam as peças numeradas, assim se theBoard[2][3] contém o inteiro 12, então a peça "12" está localizada no ponto 3rd a partir da esquerda e 4th desde o topo. O inteiro 0 será usado para representar o ponto vazio.
    
    Since this function creates a brand new board, we will want the tiles in order. So the data structure we want to create looks like:
    Uma vez que está função cria um novo tabuleiro, queremos as peças em ordem. Assim a estrutura de dados que queremos criar se parece com:
    
        theBoard[0][0] == 1    theBoard[1][0] == 2    theBoard[2][0] == 3    theBoard[3][0] == 4
        theBoard[0][1] == 5    theBoard[1][1] == 6    theBoard[2][1] == 7    theBoard[3][1] == 8
        theBoard[0][2] == 9    theBoard[1][2] == 10   theBoard[2][2] == 11   theBoard[3][2] == 12
        theBoard[0][3] == 13   theBoard[1][3] == 14   theBoard[2][3] == 15   theBoard[3][3] == 0
    """

    counter = 1
    board = []
    for i in range(COLS):
        column = []
        """Because the inner lists represent each column, we have to add the integers in this pattern: first 1, 5, 9, 13, then second 2, 6, 10, 14, and so on.
         Devido as listas interiores representarem cada coluna, temos que adicionar inteiros neste padrão: primeiro 1, 5, 9, 13 e segundo 2, 6, 10, 14 e assim por diante.

        Notice that this follows the pattern of increasing by the number of columns, and then subtracts TODO
        Note que isto segue o padrão de aumentar o número de colunas, e então subtrair TODO"""
        for j in range(ROWS):
            column.append(counter)
            counter += COLS
        board.append(column)
        counter -= COLS * (ROWS - 1) + COLS - 1

    board[COLS-1][ROWS-1] = 0
    return board


def generateNewPuzzle(numSlides):
    """This function takes a board that has its tiles in the starting position and performs several random slides on it to create the puzzle that the player needs to solve.
       Esta função pega um tabuleiro que tinha suas peças na posição inicial e realiza vários deslocamentos aleatórios sobre ele para criar o quebra-cabeça que o jogador precisa resolver."""
    sequence = []
    """We'll want to keep track of the slides done when creating the new puzzle, so we'll store them in the sequence list.
       Queremos acompanhar os movimentos feitos quando criamos um novo quebra-cabeça, então os armazenaremos na lista sequence """
    board = getStartingBoard()
    drawBoard(board)
    pygame.display.update()
    time.sleep(0.5)
    """Note that we first draw the starting board to the screen by calling drawBoard() and then pygame.display.update(), and then pause the program for half of a second. This is to give the player enough to recognize the starting board before we start making random slides.
       Note que primeiro desenhamos o tabuleiro inicial na tela chamando drawBoard() e então pygame.display.update(), e então pausamos o programa por meio segundo. Isto é para dar ao jogador tempo suficiente para reconhecer o tabuleiro inicial antes de começarmos a fazer o deslizamento aleatório. """
    lastMove = None
    """We'll store the previous move made in the lastMove variable. This is so we don't end up doing a pointless set of slides, like sliding up and then immediately sliding down. But for the first time, we'll just store None in lastMove.
       Armazenaremos os movimentos feitos anteriormente na variável lastMove. É assim que nós não acabamos fazendo um conjunto inútil de deslizamentos, como deslizar para cima e logo em seguida deslizar para baixo. Mas, na primeira vez, somente guardaremos vazio (None) no lastMove."""
    for i in range(numSlides):
        move = getRandomMove(board, lastMove)
        slideAnimation(board, move, animationSpeed=int(TILESIZE / 3), message='Generating new puzzle...')
        """We'll go through this loop however many times was specified in the integer variable numSlides. Each time, we get a random move and then perform the slide animation for that move.
        Vamos passar por este laço muitas vezes, quantas foram especificadas na variável inteira numSlides. Cada vez, pegamos um movimento aleatório e executamos a animação para aquele movimento."""
        makeMove(board, move)
        """Remember, the slideAnimation() function only does the graphics for the slide, it doesn't actually alter the board data structure. So we'll alter the data structure in the above line with the makeMove() function.
           Lembrando, a função slideAnimation() somente  faz o gráfico para o slide, ele não altera a estrutura de dados do tabuleiro. Assim, alteraremos a estrutura de dados na linha acima com a função  makeMove()."""
        
        sequence.append(move)
        """We need to remember the series of random moves we did, so append the move to the sequence list.
           Precisamos lembrar que a serie aleatória de movimentos que fizemos, acrescenta o movimento na lista sequence. """
        lastMove = move
        """Store this move as the new value for lastMove.
           Armazena este movimento como um novo valor para lastMove."""
    return (board, sequence)
    """Return the board data structure as it now is (after all those random slides) and the sequence of slides that produced it. (We'll need the sequence info later if we want to solve the puzzle by undoing the slides.
       Retorna a estrutura de dados do tabuleiro como ele está agora (depois de todos aqueles deslocamentos aleatórios) e a sequência de slides produzidos. (Vamos precisar da informação da sequência mais tarde se quisermos resolver o quebra-cabeça desfazendo os movimentos. )"""


def makeMove(board, move):
    # This function does not check if the move is valid.
    blankx, blanky = getBlankPosition(board)

    if move == UP:
        board[blankx][blanky], board[blankx][blanky + 1] = board[blankx][blanky + 1], board[blankx][blanky]
    elif move == DOWN:
        board[blankx][blanky], board[blankx][blanky - 1] = board[blankx][blanky - 1], board[blankx][blanky]
    elif move == LEFT:
        board[blankx][blanky], board[blankx + 1][blanky] = board[blankx + 1][blanky], board[blankx][blanky]
    elif move == RIGHT:
        board[blankx][blanky], board[blankx - 1][blanky] = board[blankx - 1][blanky], board[blankx][blanky]
    """Making a move on the board is just a matter of swapping the value of the blank spot (the integer 0) with the value of the spot next to the space. We'll use the multiple assignment trick to swap the values. For example, if we had two variables named a and b, we could swap them with this line of code:
       Fazer um movimento no tabuleiro é somente uma questão de trocar o valor do espaço em branco (o inteiro 0) com o valor do ponto próximo ao espaço. Vamos usar a estratégia de atribuição múltipla para trocar os valores. Por exemplo, se temos duas variáveis chamadas a e b, podemos trocá-las com esta linha de código:
    a, b = b, a

    In the above code, we do the same thing, except we use values in the board data structure.
    No código acima, fazemos a mesma coisa, exceto que usamos valores na estrutura de dados do tabuleiro."""


def getLeftTopOfTile(tilex, tiley):
    """Remember from the comments in the getStartingBoard() function that we have two sets of coordinates in this program. The first set are the pixel coordinates, which on the x-axis ranges from 0 to WINDOWWIDTH - 1, and the y-axis ranges from 0 to WINDOWHEIGHT - 1.
       Lembrando que a partir dos comentários na função getStartingBoard() temos dois conjuntos de coordenadas neste programa. O primeiro conjunto são as coordenadas dos pixels, que no intervalo do eixo-x vai de 0 até WINDOWWIDTH - 1 e no intervalo do eixo-y vai de 0 até WINDOWHEIGHT - 1.
       
    The other coordinate system is used to refer to the tiles on the game board. The upper left tile is at 0, 0. The x-axis ranges from 0 to COLS - 1, and the y-axis ranges from 0 to ROWS - 1.
    O outro sistema de coordenadas é usado para se referir as peças do jogo no tabuleiro. A peça superior esquerda está em 0,0. O intervalo do eixo-x vai de 0 até COLS -1, e o intervalo do eixo-y vai de 0 até ROWS -1."""
    left = XMARGIN + (tilex * TILESIZE) + (tilex - 1)
    top = YMARGIN + (tiley * TILESIZE) + (tiley - 1)
    return (left, top)


def isValidMove(board, move):
    """This function, give a board data structure and a proposed move direction (one of the UP, DOWN, LEFT, RIGHT values) will return True if the move is valid for the given board and False if it is not.
       Esta função dá a estrutura de dados do tabuleiro e uma direção proposta para o movimento (uma dos valores UP, DOWN, LEFT, RIGHT) que retornará True se o movimento é válido para um determinado tabuleiro e False se não.
    Some of the moves when the blank spot is on the edge of the board are not valid. For example, if the blank spot is in the top left spot of the board, it is invalid to.
    Alguns desses movimentos quando o espaço vazio está sobre o lado do tabuleiro não é válido. Por exemplo, se o espaço em branco está no ponto superior esquerdo do tabuleiro, ele é inválido. """
    blankx, blanky = getBlankPosition(board)
    return (move == UP and blanky != len(board[0]) - 1) or \
           (move == DOWN and blanky != 0) or \
           (move == LEFT and blankx != len(board) - 1) or \
           (move == RIGHT and blankx != 0)
    """This complicated-looking return statement is really straightforward. Technically the above four lines are just one line of code, but to make it readable, I've lined up the parts of the expression. The \ at the end of the line makes the Python interpreter consider the next line as a continuation of the current line.
       Esta declaração de retorno aparentemente complicada é na verdade simples. Tecnicamente as quatro linhas acima são apenas uma linha de código, mas para torná-la legível eu alinhei as partes da expressão. O \ no fim da linha faz o interpretador Python considerar a próxima linha como uma continuação da linha atual.                         
    Let's look at the first part: (move == UP and blanky != len(board[0]) - 1)
    Veja na primeira parte:  (move == UP and blanky != len(board[0]) - 1)

    This means that if the move is UP, and the y coordinate of the blank spot is not len(board[0]) - 1 (that is, the bottom row), then this part of the expression evaluates to True.
    Isto significa que se o movimento é UP e a coordenada y do ponto em branco não é len(board[0]) - 1 (isto é, a linha inferior), então esta parte da expressão é avaliada como verdadeira (True) 

    Notice that move can either be only one of the UP, DOWN, LEFT, and RIGHT values (we make sure it only ever has one of these values in our code). This will always make three of the four parts of the expression False. That means the remaining part MUST be True if the entire expression is to evaluate to True. Only one part of the four parts of the expression has to be True, because the four parts are all combined together with "or" operators.
    Note que o movimento pode ser somente um dos valores de UP, DOWN, LEFT e RIGHT (temos que ter certeza que só temos um desses valores em nosso código). Isto sempre será três das quatro partes da espressão False. Isto significa que a parte restante deve ser verdadeira (True) se a expressão inteira é avaliada como verdadeira. Somente uma parte das quatros partes da expressão tem que ser verdadeira porque as quatro partes são todas combinadas junto com o operador "or".
    
    So, for example, if move is RIGHT, but the x coordiante of the blank spot (which is stored in blankx) is 0, then we couldn't possibly slide a tile to the right because the blank spot is on the left edge of the board. In that case, isValidMove() would return False.
    Assim, por exemplo, se o movimento é RIGHT, mas a coordenada x do espaço em branco (que é armazenada em blankx) é 0, então não poderiamos deslizar uma peça para a direita porque o espaço vazio está na borda esquerda do tabuleiro.  Neste caso, isValidMove() retornará False."""

def getBlankPosition(board):
    for x in range(len(board[0])):
        for y in range(len(board)):
            """We use these nested for loops to iterate over every possible space in the board data structure.
               Usamos estes laços "for" aninhados para iterar sobre todos os espaços possíveis na estrutura de dados do tabuleiro."""
            if not board[x][y]:
                """Remember that we are using the integer value 0 to mark the blank spot, and the integer 0 maps to False. So the "not board[x][y]" condition here will be True for the blank spot.
                   Lembrando que estamos usando o valor inteiro 0 para marcar o espaço vazio, e o inteiro 0 para False. Assim, a condição  "not board[x][y]" aqui será verdadeira para o espaço em branco."""
                return (x, y)


def drawTile(tilex, tiley, number, adjx=0, adjy=0):
    """This function will draw a tile onto the MAINSURF surface. The calling code just supplies the x and y coordinates of the spot on the board (with tilex and tiley respectively) and the number to draw on the tile.
       Esta função desenhará uma peça sobre a superficie MAINSURF. A chamada ao código simplesmente fornece as coordenadas x e y do espaço no tabuleiro (com tilex e tiley respectivamente) e o número para desenhar sobre a peça. """
    left, top = getLeftTopOfTile(tilex, tiley)
    pygame.draw.rect(MAINSURF, TILECOLOR, (left + adjx, top + adjy, TILESIZE, TILESIZE))
    textSurf = FONT.render(str(number), True, TEXTCOLOR)
    textRect = textSurf.get_rect()
    textRect.center = left + int(TILESIZE / 2) + adjx, top + int(TILESIZE / 2) + adjy
    MAINSURF.blit(textSurf, textRect)


def drawBoard(board, message=''):
    MAINSURF.fill(BGCOLOR)
    if message:
        textSurf, textRect = makeText(message, MESSAGECOLOR, BGCOLOR, 5, 5)
        MAINSURF.blit(textSurf, textRect)

    for tilex in range(len(board[0])):
        for tiley in range(len(board)):
            if board[tilex][tiley]:
                """Just like in getBlankPosition(), we iterate through all the spaces in the board and the integer 0 is used to mark the blank spot. As long as we keep finding non-blank spots we want to call the drawTitle() function for that spot. str(board[tilex][tiley]) evaluates to a string of whatever the tile's number at that spot is.
                   Assim como em getBlankPosition(), iteramos todos os espaços no tabuleiro e o inteiro 0 é usado para marcar o espaço vazio. Enquanto continuarmos encontando pontos não vazios chamaremos a função drawTitle() para aquele espaço. str(board[tilex][tiley]) avalia a string qualquer que seja o número das peças que aquele espaço é. """
                drawTile(tilex, tiley, board[tilex][tiley])

    left, top = getLeftTopOfTile(0, 0)
    width = (COLS * TILESIZE) + (COLS - 1)
    height = (ROWS * TILESIZE) + (ROWS - 1)
    pygame.draw.rect(MAINSURF, BORDERCOLOR, (left - 5, top - 5, width + 9, height + 9), 4)
    """The four lines of code above draw the board around the board on the screen. First, we get the top left coordinates of the top left tile. Then we need to determine the width and height of the board in pixels. We can do this by multiplying the COLS by TILESIZE, and then adding COLS - 1 (to represent the single pixel gap in between each of the tiles, which will be one less than COLS). (The height is determined using ROWS instead of COLS.)
    As quatro linhas do código acima desenha o quadro ao redor do tabuleiro na tela. Primeiro, pegamos as coordenadas superiores esquerda do topo esquerdo da peça. Então precisamos determinar a largura e a altura do tabuleiro em pixels. Podemos fazer isto multiplicando a COLS pelo TILESIZE, e então adicionar COLS -1 (para representar o único pixel na lacuna entre as peças, que serão um a menos que COLS.) (A altura é determinada usando ROWS em vez de COLS.) 

    Then we draw the border using pygame.draw.rect(). Notice that the left and top of the rectangle we are drawing are actually 5 pixels to the left and above the topleft corner of the top left tile. This is because we are going to make a thick border (4 pixels thick actually, which is what the 4 argument stands for.) So we need to offset where we start drawing so we don't draw the border over the tiles themselves. The same for the + 9 to the width and height. (5 of these pixels are to offset the -5 we had earlier, and the other 4 pixels to offset the thickness of the border.)
    Então desenhamos a borda usando pygame.draw.rect(). Note que o lado esquerdo e a parte superior do retangulo nós desenhamos 5 pixels para a esquerda e acima do canto superior esquerdo da peça superior esquerda. Isto porque estamos fazendo uma borda grossa (4 pixels de espessura, que é na verdade, o que o argumento 4 representa.) Assim, precisamos compensar onde começamos a desenhar de modo que não desenhamos a borda sobre as peças. O mesmo para + 9 para a largura e altura. (5 desses pixels são para compensar o -5 que tinhamos anteriormente e os outros 4 pixels para compensar espessura da borda.) """

    MAINSURF.blit(RESET_SURF, RESET_RECT)
    MAINSURF.blit(NEW_SURF, NEW_RECT)
    MAINSURF.blit(SOLVE_SURF, SOLVE_RECT)
    """We want to draw the text of the three buttons (Reset Puzzle, New Puzzle, and Solve Puzzle) on the screen as well. The surface and rect object for each button are stored in the six global variables used above.
    Queremos desenhar o texto dos três botões (Reset Puzzle, New Puzzle e Solve Puzzle) na tela. A superfície e o objeto rect para cada botão são armazenados nas seis variáveis globais usada acima.  

    Notice that we have not called the pygame.display.update() function, so drawBoard() doesn't actually update the image on the computer screen. We'll leave that to whatever code called drawBoard().
    Note que não chamamos a função pygame.display.update(), então drawBoard() não está atualmente atualizando a imagem na tela do computador. Vamos deixar isso para o código chamado drawBoard(). """
    


def slideAnimation(board, direction, animationSpeed=8, message=''):
    # This function does not check if the move is valid.

    """The slideAnimation() function works the following way: First we create a surface object the same size as the window, and draw the board as it would normally look on it. Then, we draw the background color over the tile that is going to slide. This makes the board look like it has two blank spots.
    A função slideAnimation() trabalha da seguinte maneira: Primeiro criamos uma objeto superficie com o mesmo tamanho que a janela e desenhamos o tabuleiro como devemos vê-lo. Então, desenhamos a cor de fundo sobre a peça que vai deslizar. Isso faz com que o tabuleiro pareça ter dois pontos em branco. 
    This surface will be our "base" surface. To do the sliding animation, we will draw this base surface to the screen, and then draw the sliding tile on top of it. The sliding tile will be drawn in a slightly different position for each frame of this animation, so it looks like the tile is moving.
    Esta superfície será a nossa superfície "base". Para fazer o deslizamento da animação, vamos desenhar essa superfície da base na tela, e depois desenhar a peça sobre ela. A peça de deslizamento será desenhada em uma posição ligeiramente diferente para cada quadro dessa animação, com isso parece que a peça está se movendo."""

    # prepare the base surface
    drawBoard(board, message=message)
    baseSurf = MAINSURF.copy()
    blankx, blanky = getBlankPosition(board)
    if direction == UP:
        movex = blankx
        movey = blanky + 1
    elif direction == DOWN:
        movex = blankx
        movey = blanky - 1
    elif direction == LEFT:
        movex = blankx + 1
        movey = blanky
    elif direction == RIGHT:
        movex = blankx - 1
        movey = blanky

    moveLeft, moveTop = getLeftTopOfTile(movex, movey)
    pygame.draw.rect(baseSurf, BGCOLOR, (moveLeft, moveTop, TILESIZE, TILESIZE))

    for i in range(0, TILESIZE, animationSpeed):
        """We will be looping to create the sliding animation. On each iteration of the loop, we draw the tile being slide a bit more than the last iteration.
           Estaremos controlando o laço para criar a animação. Em cada iteração do laço, vamos desenhar a peça sendo deslizada um pouco mais do que a última iteração."""
        checkForQuit()
        """While we are doing this animation, we still want to check if the player has tried to quit the program, so we call our checkForQuit() function.
        Enquanto estamos fazendo esta animação, ainda queremos verificar se o jogador tentou encerrar o programa, por isso chamamos a nossa função checkForQuit (). """
        if direction == UP:
            adjx = 0
            adjy = -i
        if direction == DOWN:
            adjx = 0
            adjy = i
        if direction == LEFT:
            adjx = -i
            adjy = 0
        if direction == RIGHT:
            adjx = i
            adjy = 0
        """We will draw the sliding tile in its normal position, except slightly adjusted by the value in the adjx and adjy variables. This will produce the "sliding" effect because the value in adjx or adjy increases on each iteration in the loop, causing the tile to appear to have slide more.
        Desenharemos a peça deslizando em sua posição normal, exceto ligeiramente ajustada pelo valor das variáveis adjx e adjy. Isto produzirá um efeito "deslizante" porque o valor em adjx ou adjy aumenta em cada iteração no laço, fazendo com que a peça pareça ter deslizado mais.

        Remember that a positive amount will move the tile to the right or down directions, but a negative amount will move it to the left and up directions.
        Lembrando que uma quantidade positiva irá mover a peça para as direções direita ou para baixo, mas a quantidade negativa irá mover para a direção esquerda e para cima.

        Note that we only want to slide along one axis, not both. This is why either adjx or adjy will be 0 no matter which of the UP, DOWN, LEFT, RIGHT directions we are moving.
        Note que somente queremos desliszar ao longo do eixo x, e não em ambos. Isto é porque adjx ou adjy serão 0 e não importa qual das direções UP, DOWN, LEFT, RIGHT estamos movendo."""
        
        MAINSURF.blit(baseSurf, (0, 0))
        """This draws the base surface to the screen, specifically with the top left corner of the base surface at the 0, 0 coordinates in the window.
        Isto desenhha a base da superficie na tela, especificamente com o canto superior esquerdo da base da superficie nas coordenadas 0,0 na janela."""
        drawTile(movex, movey, board[movex][movey], adjx, adjy)
        """Next we draw the sliding tile, slightly adjusted to give it that moving effect.
           Em seguida, desenhamos as peças de deslizamento, ligeiramente adaptadas para dar esse efeito de movimento."""
        pygame.display.update()
        MAINCLOCK.tick(FPS)
        """Then we call pygame.display.update() to update the screen, and call MAINCLOCK.tick(FPS) to pause the screen a little bit.
           Então chamamos pygame.display.update() para atualizar a tela e chamamos MAINCLOCK.tick(FPS) para pausar a tela um pouco. """


def checkForQuit():
    """Sometimes we want to check the event queue for any QUIT events (or if the player has specifically pressed the Esc key to quit), but we don't care about any other events (such as mouse movements or clicks). By passing QUIT to the pygame.event.get() call, we return only QUIT events.
       As vezes queremos checar a fila de eventos para qualquer QUIT events (ou se o jogador especificamente pressionou a tecla esc para encerrar), mas não nos importamos com qualquer outro evento (como movimentos do mouse ou clicks). Passando QUIT ao pygame.event.get(), retornamos somente eventos QUIT (Encerrar). """
    for event in pygame.event.get(QUIT):
        terminate()

    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        """We'll go through the events in the event queue again, this time only looking at KEYUP events (which happen when the player lets go of a keyboard key). If the key they pressed was the Esc key, we'll quit the program.
           Vamos aos eventos na fila de eventos de novo, desta vez somente olhamos nos eventos  KEYUP (que ocorre quando o jogador deixa uma tecla do teclado).  Se a tecla pressionada foi Esc, encerraremos o programa."""
        pygame.event.post(event)
        """If the key was not the escape key, then we want to return the KEYUP event to the event queue by calling pygame.event.post(). This ensures that we don't take out any, say, arrow key presses and then not handle them. The code in the main() function will later pick up these keyboard events, and properly handle them.
           Se a tecla não foi a tecla Esc, então queremos retornar aos eventos KEYUP para a fila de eventos chamando pygame.event.post(). Isto garante que não pegamos qualquer, por exemplo, teclas de seta e depois não conseguimos lidar com elas. O código na função main() mais tarde irá pegar esses eventos de teclado e lidará correctamente com eles."""


def getRandomMove(board, lastMove=None):
    validMoves = [UP, DOWN, LEFT, RIGHT]
    """We want to make sure that the random move this function returns is a valid move to make. So we'll create a list stored in the validMoves variable that contains all four direction values. Then we test each of the four directions to see if it is a valid move. If it is not a valid move, we'll remove that move from the validMoves list.
    Queremos certificar que o movimento aletório retornado desta função é um movimento válido para ser feito. Assim criaremos uma lista armazenada na variável validMoves que contém todos os quatros valores das direções. Então testamos cada uma das quatro direções para ver se o movimento é válido. Se o movimento não é válido, removeremos este movimento da lista validMoves. 

    For example, if the previous move was UP, then we don't want to return DOWN because that would make cancel out the last move.
    Por exemplo, se o movimento anterior foi UP (para cima), então não queremos retornar DOWN (para baixo) porque isso iria cancelar o último movimento.  """
    if lastMove == UP or not isValidMove(board, DOWN):
        validMoves.remove(DOWN)
    if lastMove == DOWN or not isValidMove(board, UP):
        validMoves.remove(UP)
    if lastMove == LEFT or not isValidMove(board, RIGHT):
        validMoves.remove(RIGHT)
    if lastMove == RIGHT or not isValidMove(board, LEFT):
        validMoves.remove(LEFT)

    return random.choice(validMoves)
    """The random.choice() function will take a list or tuple value and return one of values in the list/tuple. We'll use this to randomly pick one of the remaining valid direction values.
       A função random.choice() pegará uma lista ou uma tupla de valores e retornará um dos valores da lista/tupla. Usaremos isso para escolher aleatoriamente um dos valores restantes de direções válidas."""


def getSpotClicked(board, x, y):
    """Remember from the comments in the getStartingBoard() function that we have two sets of coordinates in this program. The first set are the pixel coordinates, which on the x-axis ranges from 0 to WINDOWWIDTH - 1, and the y-axis ranges from 0 to WINDOWHEIGHT - 1.
    Lembrando que a partir dos comentários da função getStartingBoard() temos dois conjuntos de coordenadas neste programa. O primeiro conjunto são as coordenadas do pixel, que o intervalo do eixo-x vai de 0 até WINDOWWIDTH - 1 e o intervalo do eixo-y vai de 0 até WINDOWHEIGHT - 1.  

    The other coordinate system is used to refer to the tiles on the game board. The upper left tile is at 0, 0. The x-axis ranges from 0 to COLS - 1, and the y-axis ranges from 0 to ROWS - 1.
    O outro sistema de coordenadas é usado para referenciar as peças sobre o tabuleiro do jogo. A peça superior esquerda está em 0,0. O intervalo do eixo-x vai de 0 até COLS -1 e o intervalo do eixo-y vai de 0 até ROWS -1."""
    for tilex in range(len(board[0])):
        for tiley in range(len(board)):
            """This set of nested for loops ensures that we run this block of code on each tile in the board. Note that we could have used COLS instead of len(board[0]) and ROWS instead fo len(board), but this way the range of integers we loop on depends on the board data structure rather than the ROWS and COLS global variables.
            Este conjunto de laços "for" aninhados garante que executaremos este bloco de código em cada peça no tabuleiro. Note que poderiamos ter usado COLS ao invés de len(board[0]) e ROWS ao invés de len(board), mas desta maneira o intervalo de inteiros no laço depende da estrutura de dados do tabuleiro em vez de variáveis globais ROWS e COLS.

            This means we could call the getSpotClicked() function and pass board data structures besides the main one we draw on the screen. This makes the function more flexible to use.
            Isto significa que podemos chamar a função getSpotClicked() e passar a estrutura de dados do tabuleiro além do principal que é desenhar na tela. Isto torna a função mais flexivel para uso.""" 
            left, top = getLeftTopOfTile(tilex, tiley)
            rectangle = pygame.Rect(left, top, TILESIZE, TILESIZE)
            """The above code creates a new pygame.Rect object which represents the area on the board that the tile covers.
            O código acima cria um novo objeto pygame.Rect que representa a área no tabuleiro que a peça cobre."""
            if rectangle.collidepoint(x, y):
                return (tilex, tiley)
                """If the pixel coordinate (stored in the x and y parameters) is within the pygame.Rect object that represents the current tile we are iterating on, then the pygame.Rect object's collidepoint() method will return True. In that case, we want to return the coordinates of the tile that was clicked.
                    Se a coordenada do pixel (armazenada nos parametros x e y) está dentro do objeto pygame.Rect que representa a peça atual que estamos iterando, então o objeto pygame.Rect pelo método collidepoint() retornará verdadeiro (True). Neste caso, queremos retornar as coordenadas da peça que foi clicada. """
                
    return None
    """If none of the tiles were clicked on, then the click must have been off the board entirely (or the blank spot was clicked) and we'll signify this by returning the None value.
        Se nenhuma das peças foram clicadas, então o click deve ter sido totalmente fora do tabuleiro (ou o espaço em branco foi clicado) e vamos mostrar isto retornando o valor None."""


def resetAnimation(board, sequence):
    """Sometimes we will want to "undo" a sequence of slides, such as when we want to undo all the moves a player has made (which we do when the player clicks the "reset" button) or when we want to undo all the slides back to the starting, solved board (which we do when the player clicks on the "solve" button).
    As vezes queremos "desfazer" uma sequência de deslocamentos, tal como quando queremos desfazer todos os movimentos que o jogador fez (que fazemos quando o jogador clica sobre o botão "reset") ou quando queremos desfazer todos os deslizamentos e voltar ao começo, resolvendo o tabuleiro (que fazemos quando o jogador clica sobre o botão "solve").

    First we will want to take the sequence of slides and reverse the order of them. Then, we want to do the opposite of the moves in the sequence (for example, go down if the move was UP).
    Primeiro queremos pegar a sequência de deslizamentos e inverter a ordem deles. Então, queremos fazer o oposto dos movimentos na sequencia (por exemplo, indo para baixo se o movimento foi para cima)."""
    revSequence = sequence[:]
    """The [:] is a Python trick for copying the values in a list. Note that we cannot copy lists like we can copy values in other variables, because the variable does not contain the list but a reference to the list.
    O [:] é uma estratégia do Python para copiar os valores na lista. Note que não podemos copiar as listas como podemos copiar os outros valores das variáveis, porque as variáveis não contém a lista mas a referência da lista.  

    More info on lists and list references can be found at http://inventwithpython.com/chapter10.html#ListReferences
    Mais informações sobre listas e referências de listas podem ser obtidos em: http://inventwithpython.com/chapter10.html#ListReferences

    The [:] after sequence is technically a list slice. A slice is a sublist of the values in a list, much like an index just points to a single value in a list. For example, if we have this list:
    O [:] depois da sequência é tecnicamente uma fatia da lista. Uma fatia é uma sub-lista dos valores na lista, assim como um índice somente aponta para um único valor na lista. Por exemplo, se temos esta lista: 
        spam = [42, 10, 5, 100, 99]
    Then the index spam[2] refers to the integer 5 (remember, the indexes start a 0. 0 refers to the first item (42), 1 refers to the second item (10), 2 refers to the third itme (5), etc.)
    Então o índice spam[2] refere-se ao inteiro 5 (Lembrando que os indices começam em 0. 0 refere-se ao primeiro item (42), 1 refere-se ao segundo item (10), 2 refere-se ao terceiro item (5), etc.)

    More info on slices and slicing can be found at http://inventwithpython.com/chapter9.html#SlicesandSlicing
    Mais informações sobre fatias e cortes podem ser encontradas em: http://inventwithpython.com/chapter9.html#SlicesandSlicing

    But a slice uses a colon to grab multiple values:
    Mas uma fatia usa dois pontos para pegar múltiplos valores:
        eggs = spam[2:4]

    The above would put the list [5, 100] in the variable eggs. That is, it creates a new list and puts the values starting at (and including) index 2 and up to (but not including) the value at index 4. The integer before the colon is the starting index, and the integer after the colon is the ending index.
    O comando acima colocaria a lista [5, 100] na varável eggs. Isto é, ele cria uma nova lista e coloca os valores começando no(e incluindo) índice 2 e até (mas não incluindo) o valor do índice 4. O inteiro antes dos dois pontos é o índice inicial, e o inteiro depois dos dois pontos é o índice final.

    If we leave out the first index in a slice, then Python interprets this as 0 (which is the first item.)
    Se deixamos fora o primeiro índice na fatia, então Python interpreta isto como 0 (que é o primeiro item)
            bagels = spam[:4]

    The above line would put [42, 10, 5, 100] in the bagels variable.
    A linha acima colocaria [42, 10, 5, 100] na variável bagels.
    
    If we leave out the second index in a slice, then Python interprets this as meaning past the last index in the list:
    Se deixarmos fora o segundo índice na fatia, Python interpreta isto como o útimo índice da lista: 
        pancakes = spam[2:]
        
    The above line would put [5, 100, 99] in the pancakes variable.
    A linha acima colocaria [5, 100, 99] na variável pancakes.

    If we don't specify either index in a slice, then the ENTIRE list is copied. This is a quick way to copy a list, rather than just copying a list reference.
    Se não especificarmos nenhum índice na fatia, então a lista INTEIRA é copiada. Está é uma maneira rápida de copiar uma lista, ao invés de apenas copiar uma lista de referência.
    """
    revSequence.reverse()
    """All list variables have a reverse() method that will flip the order of the items in a list, so we call that method here.
      Todas as variáveis da lista tem um método inverso() que irá inverter a ordem dos itens em uma lista, por isso chamamos o método aqui"""

    for move in revSequence:
        if move == UP:
            oppositeMove = DOWN
        elif move == DOWN:
            oppositeMove = UP
        elif move == RIGHT:
            oppositeMove = LEFT
        elif move == LEFT:
            oppositeMove = RIGHT
        """For each move in the flipped (that is, reversed) sequence (revSequence) we want to get the opposite move. The opposite of UP is DOWN and the opposite of LEFT is RIGHT, so we set the oppositeMove variable accordingly.
           Para cada movimento na sequência virada (isto é, invertida) (revSequence) queremos pegar o movimento oposto. O oposto de UP (acima) é DOWN (abaixo) e o oposto de LEFT (esquerda) é RIGHT (direita), assim definimos a variável  oppositeMove adequadamente."""

        slideAnimation(board, oppositeMove, animationSpeed=int(TILESIZE / 2))
        makeMove(board, oppositeMove)
        """Now we make the move by calling slideAnimation() (to display the sliding on the screen) and makeMove() (to actually update the board data structure). This is just like how we do in the main() and generateNewPuzzle() functions when the player makes a move.
           Agora fazemos o movimento chamando slideAnimation() (para mostrar o deslizamento sobre a tela) e makeMove() (para atualizar a estrutura de dados do tabuleiro). Isto é justamente como fazemos nas funções main() e generateNewPuzzle() quando o jogador faz um movimento"""


def makeText(text, color, bgcolor, top, left):
    textSurf = FONT.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    """The makeText() function has three lines of code that we call over and over again each time we want to create a bit of text. The first line creates a new pygame.Surface object with the text we provide drawn on it. Of course, we also have to provide the color of the text and the background color of the surface object. The True argument to the render() method specifies that we want to use anti-aliasing (which makes the text look a little less blocky.)
      A função makeText() tem três linhas de código que chamamos uma e outra vez cada vez que queremos criar um pequeno texto. A primeira linha cria um novo objeto pygame.Surface com o texto desenhado nele. É claro, também temos que fornecer a cor do texto e a cor do fundo ao objeto superfície. O argumento True para o método render() especifica que queremos usar anti-aliasing (que torna o texto um pouco mais suave.)

    There is more info on anti-aliasing at http://inventwithpython.com/chapter17.html#TherenderMethodforFontObjects
    Existe mais informação sobre anti-aliasing em http://inventwithpython.com/chapter17.html#TherenderMethodforFontObjects

    Remember that the font size information is already stored in the pygame.font object stored in our global variable named FONT.
    Lembrando que a informação do tamanho da fonte é anteriormente armazenada no objeto pygame.font em nossa variável global chamada FONT. 

    In order to tell where we want this text to appear on the screen, we need to get a pygame.Rect object for this surface (this is what the "textRect = textSurf.get_rect()" line does) and set the top left corner to a specific position (this is what the "textRect.topleft = (top, left)" line does).
    Com o objetivo de dizer onde queremos que o texto aparece na tela, precisamos pegar o objeto pygame.Rect para esta superfície (isto é o que a linha "textRect = textSurf.get_rect() faz ) e definimos a posição do canto superior esquerdo (isto é feito pela linha "textRect.topleft = (top, left)"). """

  
    return (textSurf, textRect)


if __name__ == '__main__':
    main()
