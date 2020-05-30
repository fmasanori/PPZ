# Simulate (A Simon Clone)
# http://inventwithpython.com/blog
# By Al Sweigart al@inventwithpython.com

"""
Welcome to the Code Comments for Simulate. Code Comments is a series of simple games with detailed comments in the source code, so you can see how the game works.
Bem vindo aos Códigos Comentados para Simulate. Códigos Comentados é uma série de jogos simples com comentários detalhados no código fonte, assim você pode ver como o jogo trabalha.

The text in between the triple-double-quotes are comments. The Python interpreter ignores any text in between them, so we can add any comments about the source code without affecting the program. In general for Code Comments, the comments will describe the lines of code above the comment. It helps to view this file either on the Code Comments site or with a text editor that does "syntax highlighting", so that the comments appear in a separate color and are easier to distinguish from the code.
O texto entre aspas duplas-triplas são comentários. O interpretador do Python ignora qualquer texto entre eles, assim nós podemos adicionar qualquer comentário sobre o código fonte sem afetar o programa. Em geral, para os Códigos Comentados, os comentários descreverão as linhas de código acima do comentário. Isto ajuda a visualizar esse arquivo no site Code Comments ou com um editor de texto que faz "sintaxe destacada", de modo que os comentários aparecem em cores distintas e são mais fáceis de distinguir no código. 

This Code Comments assumes you know some basic Python programming. If you are a beginner and would like to learn computer programming, there is a free book online called "Invent Your Own Computer Games with Python" at http://inventwithpython.com
Este código comentado assume que você tenha algum conhecimento básico sobre a linguagem Python. Se você é um iniciante e gostaria de aprender programação de computadores, existe um livro grátis (free) online chamado "Invent Your Own Computer Games with Python" disponível no site http://inventwithpython.com

The Code Comments programs make references to sections of this book throughout the program. This Code Comments can also teach you how to use the Pygame library to make your own games with graphics, animation, and sound. You can download Pygame from http://pygame.org and view its documentation at http://pygame.org/docs/
Os programas dos Códigos Comentados fazem referência à seções deste livro em todo o programa. Estes Códigos Comentados também podem te ensinar  a como usar a biblioteca Pygame para fazer seus próprios games com gráficos, animações e sons. Vc pode fazer o download do Pygame no site: http://pygame.org e visualizar sua documentação em: http://pygame.org/docs/

HOW TO PLAY SIMULATE:
COMO JOGAR O SIMULATE:

The four colored buttons will light up in a certain pattern. After they are done, click on the buttons in the same order as the pattern. Each time you complete the pattern, the pattern will increase in length. Do not take too long to click the buttons once you have begun. If you pause in the middle of repeating a pattern for several seconds, you will lose the game.
Os quatros botões coloridos acenderão em um certo padrão. Depois deles estarem prontos, clique sobre os botões na mesma ordem que o padrão. Cada vez que você completar o padrão, o padrão aumentará de tamanho. Não demore muito tempo para clicar nos botões depois que você começou. Se vc pausar no meio de um padrão repetindo por vários segundos,  voce perderá o jogo.
"""

import random
import time
import pygame
import sys
from pygame.locals import *
"""Here we import modules that our game needs. random has random number functions, time has the sleep() function, sys has the exit() function, and pygame contains all the pygame-related functions.
Aqui nós importamos os módulos que nosso game precisa. O módulo "random" tem funções de números aleatórios, "time" tem a função sleep(), "sys" tem a função exit() e "pygame" contém todas as funções relacionadas ao paygame.

pygame.locals contains constants like MOUSEMOTION and MOUSEBUTTONUP and QUIT for the events. It's easier to type MOUSEBUTTONUP instead of pygame.locals.MOUSEBUTTONUP, so we use the "from pygame.locals import *" format to import these to the local namespace.
"pygame.locals" contém constantes como MOUSEMOTION e MOUSEBUTTONUP e QUIT para os eventos. É mais fácil digitar  MOUSEBUTTONUP em vez de pygame.locals.MOUSEBUTTONUP, assim usamos o formato "from pygame.locals import *" para importá-los para o "namespace" local.
"""

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FLASHSPEED = 0.5
FLASHDELAY = 0.2
BUTTONSIZE = 200
BUTTONGAPSIZE = 20
TIMEOUT = 4
"""These constant variables (the uppercase names means we shouldn't change the values stored in them) set some standard values for our game. You can play around with different values for them (though some values might cause bugs in the game.) By using constants instead of the values directly, it is easier to make changes since we only have to change them in one place.
Estas variáveis constantes (os nomes em letras maiúsculas significa que não podemos mudar o valor armazenado nelas) define alguns valores padrão para o nosso jogo. Vc pode jogar com valores diferentes pra eles (no entanto alguns valores podem causar erros no jogo). Usando constantes ao invés dos valores diretamente, é mais fácil fazar mudanças e então somente temos que mudá-las em um lugar.

For example, if we used 200 instead of BUTTONSIZE, then if we wanted to change our code later we'd have to change every place in the code we find 200. This is trickier than just changing the one line where MAXLIFE is originally set.
Por exemplo, se usarmos 200 em vez de BUTTONSIZE, se queremos mudar nosso código mais tarde, teremos que mudar em todos os lugares onde tem 200. Isto é muito mais dificil do que mudar somente uma linha onde o MAXLIFE está originalmente definido.

More information about constants is at http://inventwithpython.com/chapter9.html#ConstantVariables
Mais informações sobre constantes em: http://inventwithpython.com/chapter9.html#ConstantVariables 
"""

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BRIGHTRED = (255, 0, 0)
RED = (155, 0, 0)
BRIGHTGREEN = (0, 255, 0)
GREEN = (0, 155, 0)
BRIGHTBLUE = (0, 0, 255)
BLUE = (0, 0, 155)
BRIGHTYELLOW = (255, 255, 0)
YELLOW = (155, 155, 0)
DARKGRAY = (40, 40, 40)

BGCOLOR = BLACK
"""We also set up some constant values for different colors. Pygame uses tuples of three integers to represent color. The integers represent the amount of red, green, and blue in the color (this is commonly called a RGB). 0 means there is none of the primary color in the color, and 255 means there is the maximum amount. So (255, 0, 0) is red, since it has the maximum amount of red but no green or blue. But (255, 0, 255) adds the max amount of blue with the red, creating purple.
Também podemos definir algumas valores constantes para diferentes cores. Pygame usa tuplas de 3 inteiros para representar a cor. Os inteiros representam a quantidade de vermelho, verde e azul na cor (isto é comumente chamado RGB). 0 significa que não existe nada de cor primária na cor e 255 significa que existe uma quantidade máxima. Assim, (255, 0, 0) é vermelho, já que ele tem a quantidade máxima de vermelho e não tem nada de verde ou azul. Mas, (255, 0, 255) adiciona a quantidade máxima de azul com vermelho, criando a cor pupura.

Here we have the four colors we will use for the four buttons: yellow, blue, red, and green. We also have slightly darker versions of each of these colors. Note that we store the background color we will use for the game in BGCOLOR.
Aqui temos quatro cores que usaremos para os quatro botões: yellow (amarelo), blue(azul), red (vermelho) e green (verde). Temos também versões um pouco mais escura de cada uma destas cores. Note que armazenaremos a cor de fundo que vamos usar em BGCOLOR. 

Note that BGCOLOR will actually have its value changed in our program. I've decided to go with the all caps convention because it is a global variable like all the constants. It's just a preference I made.
Note que BGCOLOR terá efetivamente seu valor alterado em nosso programa. Eu decidi ir com todas as convenções porque ela é uma variável global como todas as outras constantes. Isto é apenas um preferência que eu fiz.

More information about colors is at http://inventwithpython.com/chapter17.html#ColorsinPygame
Mais informação sobre cores em: http://inventwithpython.com/chapter17.html#ColorsinPygame
"""

XMARGIN = int((WINDOWWIDTH - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)
YMARGIN = int((WINDOWHEIGHT - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)

YELLOWRECT = pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE)
BLUERECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE)
REDRECT = pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
GREENRECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
"""These pygame.Rect objects represent the regions on the window for the yellow, blue, red, and green buttons. Since they never move around and are only four of them, we just calculate the coordinates once and save it to these pygame.Rect objects.
   Estes objetos pygame.Rect representam regiões da janela para os botões amarelo (yellow), azul (blue), vermelho(red) e verde(gree). Uma vez que eles nunca se movem e são apenas quatro deles, apenas calculamos as coordenadas uma vez e salvamos nos objetos pygame.Rect."""

def main():
    global MAINCLOCK, MAINSURF, FONT, BEEP1, BEEP2, BEEP3, BEEP4
    """The main() function is where our program begins. (See the last two lines of code to see why.) Because we define MAINCLOCK and MAINSURF inside this function, these are local variables to the main() function and the names MAINCLOCK and MAINSURF won't exist outside of this function. By using a global statement, we can tell Python that we want these variables to be global variables.
     A função main() é onde nosso programa começa. (Veja as duas ultimas linhas do código para entender porque). Normalmente, porque definimos MAINCLOCK e MAINSURF  dentro desta função, elas são variáveis locais a função main() e os nomes MAINCLOCK e MAINSURF não existem fora desta função. Ao usar uma declaração global, podemos dizer ao Python que queremos que estas variáveis sejam variáveis globais.
   
    More information about global and local variables is at http://inventwithpython.com/chapter6.html#VariableScope
    Mais informação sobre variáveis locais e globais em: http://inventwithpython.com/chapter6.html#VariableScope 
    """

    pygame.init()
    MAINCLOCK = pygame.time.Clock()
    MAINSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Simulate')
    """pygame.init() needs to be called before any of the other Pygame functions.
    pygame.init() precisa ser chamado antes de qualquer outra função Pygame.

    pygame.time.Clock() returns a pygame.Clock object. We will use this object's tick() method to ensure that the program runs at no faster than 30 frames per second (or whatever integer value we have in the FPS constant.)
    pygame.time.Clock() retorna o objeto pygame.Clock. Usaremos este objeto no metodo tick() para garantir que o programa não seja executado em mais de 15 frames por secundo (ou qualquer outro valor inteiro que temos no FPS constante.)
    
    pygame.display.set_mode() creates the window on the screen and returns a pygame.Surface object. Any drawing done on this Surface object with the pygame.draw.* functions will be displayed on the screen when we call pygame.display.update().
    pygame.display.set_mode() cria a janela na tela e retorna um objeto pygame.Surface. Todo o desenho feito sobre a superfície deste objeto com as funções pygame.draw.* serão mostradas na tela quando chamamos pygame.display.update().
    
    More information about pygame.display.set_mode() is at http://inventwithpython.com/chapter17.html#ThepygamedisplaysetmodeandpygamedisplaysetcaptionFunctions
    Mais informações sobre pygame.display.set_mode() em: http://inventwithpython.com/chapter17.html#ThepygamedisplaysetmodeandpygamedisplaysetcaptionFunctions"""

    FONT = pygame.font.Font('freesansbold.ttf', 16)
    """This line loads a font to use for drawing text. Since our game only uses one font (and at one size, 16 points) we only have to make one call to the pygame.font.Font() constructor function. We will store this font in the global variable FONT.
       Esta linha carrega uma fonte usada para desenhar o texto. Já que nosso jogo usa somente uma fonte (e em um tamanho, 16 points) somente temos que fazer uma chamada a função pygame.font.Font(). Armazenaremos esta fonte na variável global FONT. """
 

    BEEP1 = pygame.mixer.Sound('beep1.ogg')
    BEEP2 = pygame.mixer.Sound('beep2.ogg')
    BEEP3 = pygame.mixer.Sound('beep3.ogg')
    BEEP4 = pygame.mixer.Sound('beep4.ogg')
    """The pygame.mixer.Sound() constructor function creates a new pygame.mixer.Sound object. We call it once for each sound file we want to load. Pygame can play wav, mp3, and ogg files. However, wav files are uncompressed and take up a lot of disk space. And Pygame has limited support for playing mp3s. The Ogg Vorbis format has tiny file sizes like MP3s with similar quality levels, so we will use that format.
    A função pygame.mixer.Sound() cria um novo objeto pygame.mixer.Sound. Chamamos uma vez para cada arquivo de som que quisermos carregar. Pygame pode tocar arquivos wav, mp3 e ogg. Todavia, arquivos wav não são compactados e ocupam muito espaço em disco. E Pygame tem suporte limitado para jogos em mp3s. O formato Ogg Vorbis tem arquivos de tamanho pequeno, como MP3 e com níveis de qualidade semelhante, por isso vamos usar esse formato.

    You can download these files from:
    Você pode fazer o dowload desses arquivos a partir de:
    
        http://inventwithpython.com/resources/beep1.ogg
        http://inventwithpython.com/resources/beep2.ogg
        http://inventwithpython.com/resources/beep3.ogg
        http://inventwithpython.com/resources/beep4.ogg

    Be sure that these .ogg files are in the same folder as simulate.py, or else your program will not be able to load them.
    Certifique-se que estes arquivos .ogg estão no mesmo diretório que simulate.py, porque se não, seu programa não poderá carregá-los.

    If you want to record your own sounds, or convert file formats between wav, mp3, and ogg, there is a free sound editor software called Audacity that you can download from http://audacity.sourceforge.net/
    Se você deseja gravar seu próprio som, ou converter formatos de arquivos entre wav, mp3 e ogg, existe um software grátis de editor de som chamado Audacity que você pode fazer o download em : http://audacity.sourceforge.net/
    """

    pattern = []
    currentStep = 0
    waitingForInput = False
    lastClickTime = 0
    score = 0
    """These five variables will keep track of the state of the game.
    Estas cinco variáveis acompanharão o estado do jogo.
    
    pattern is a list of color tuples (specifcally, the YELLO, BLUE, RED, and GREEN values). The pattern will increase in length when we add more color values to it.
    pattern é uma lista de tuplas de cores (especificamente, os valores amarelo azul, vermelho e verde). O padrão aumentará o tamanho quando adicionarmos mais valores de cores a ele.

    Note that whenever we add a new color value to the list, such as pattern.append(BLUE), we are really adding the tuple value (0, 0, 255) to the list. We could instead have the integers, say, 0 for yellow, 1 for blue, 2 for green, and 3 for red. Then we'd only have to append a single integer for each color instead of three integers and our program would use less memory. But considering that reusing the YELLOW, BLUE, GREEN, RED constants makes the program easier to understand, it would be preferable to use those constants. And we'd only be wasting less than a hundred bytes anyway, which is nothing for modern computers.
    Note que sempre que adicionamos um novo valor de cor a lista, tal como o pattern.append(BLUE), estamos efetivamente adicionando a tupla com o valor (0, 0, 255) à lista.  Podemos ao invés disso ter inteiros, assim, 0 para amarelo, 1 para azul, 2 para verde e 3 para o vermelho. Então somente teremos que adicionar um único inteiro para cada cor ao invés de três inteiros e nosso programa usará menos memória. Mas considerando o reuso das constantes YELLOW, BLUE, GREEN, RED faz o programa mais fácil de ser entendido, por isso é preferível o uso destas constantes. E só estariamos desperdiçando menos de uma centena de bytes de qualquer maneira, que não é nada para os modernos computadores. 

    waitingForInput is a bool. When it is set to False, that means the program is currently playing the pattern to the user. After it is done, it will set waitingForInput to True which tells the program that it is accepting button presses from the player.
    waitingForInput é uma boleana. Quando ela está definida como False, significa que o programa está jogando o padrão para o usuário. Depois de estar pronto, definirá waitingForInput para True que diz ao programa  que está aceitando o botão ser pressionado pelo jogador.

    lastClickTime stores the latest time that the player clicked a button. This is so we can track if the player has taken too long to press the next button in the pattern. Time is stored as an integer of the number of seconds since January 1, 1970 (this is commonly called the UNIX epoch). We can get the number of seconds since the UNIX epoch to the current time by calling time.time().
    lastClickTime aramazena a última vez que o jogador clicou sobre o botão. Isto é para que possamos monitorar se o jogador teve bastante tempo para pressionar o próximo botão no padrão.O tempo é armazenado como um inteiro de segundos desde January 1, 1970 (isto é normamente chamado época UNIX). Podemos obter o número de segundos desde a época UNIX para o momento atual chamando time.time(). 

    score will just contain the score. Each time the player completes a pattern, we increase it by 1.
    score conterá somente a pontuação. Cada vez que o jogador completa um padrão, incrementamos em 1."""

    while True:
        clicked = None
        """This is the main game loop, which constantly loops while the program is playing. In this loop, we display the board on the screen and also handle any input events from the player. clicked will store a color value of the last button that was clicked on. We reset the value to None each time the game loop loops.
         Este é o laço principal do jogo, que constantemente estará em execução enquanto o programa está jogando. Neste laço, mostramos o quadro na tela  e também lidamos com os eventos de entrada do jogador. clicked irá armazenar o valor da cor do último botão que foi clicado. Nós redefinimos o valor para nada "None" cada vez que jogo entra no loop."""

        MAINSURF.fill(BGCOLOR)
        drawButtons()
        """The MAINSURF.fill() call simply paints the entire screen with the background color, to erase any previous drawings made.
        A chamada MAINSURF.fill() simplesmente pinta a tela inteira com a cor de fundo, para apagar qualquer desenho feito anteriormente.

        drawButtons() will draw the four colored buttons on the MAINSURF surface. Remember that they will not show up on the screen until pygame.display.update() is called.
        drawButtons() desenhará os quatro botões coloridos na superfície MAINSURF. Lembre-se que eles não vão aparecer na tela até que pygame.display.update() seja chamado. """

        scoreSurf = FONT.render('Score: ' + str(score), True, WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WINDOWWIDTH - 100, 10)
        MAINSURF.blit(scoreSurf, scoreRect)

        infoSurf = FONT.render('Match the pattern by clicking on the button or using the 8, 9, 5, 6 keys.', True, DARKGRAY)
        infoRect = infoSurf.get_rect()
        infoRect.topleft = (10, WINDOWHEIGHT - 25)
        MAINSURF.blit(infoSurf, infoRect)
        """Next we need to draw some text onto the screen. One piece of text will show the player the score. The other piece of text will show some directions, telling the player that they can also use the 5, 6, 8, and 9 keys on the keyboard to play instead of just the mouse.
        Em seguida precisamos desenhar algum texto na tela. Uma parte do texto mostrará ao jogador a pontuação. A outra parte do texto mostrará algumas direções, dizendo ao jogador que ele pode também usar as teclas 5, 6, 8 e 9 do teclado para jogar em vez de somente o mouse.

        We take the pygame.font.Font object we stored in FONT (remember, it is the "free sans bold" font with a size of 16 points) and call the Font object's render() method. This method has three parameters: the text we want, whether we want it to look smooth or not, and the color of the text. The "smoothness" is called "anti-aliasing". There is more information about anti-aliasing at http://inventwithpython.com/chapter17.html#TherenderMethodforFontObjects
        Pegamos o objeto pygame.font.Font armazenado em FONT (lembrando, ele é a fonte "free sans bold" com tamanho 16 ) e chamamos o ojeto FONT pelo metódo render(). Este método tem três parâmetros: o texto que queremos, se queremos vê-lo suave ou não e a cor do texto. A suavização é chamada  "anti-aliasing". Existem mais informações sobre anti-aliasing em: http://inventwithpython.com/chapter17.html#TherenderMethodforFontObjects
        
        The render() method returns a pygame.Surface object. We can place the text at a specific place in the window by getting the Surface object's get_rect() method to return a pygame.Rect rectangle object for the surface, and then setting the (x, y) coordinates of the topleft corner of the rectangle. This way, when we "blit" it (that is, draw it) to the MAINSURF surface (which is the surface object for the window), we can pass the rectangle object to tell it where on the MAINSURF surface to draw the text.
        O método render() retorna um objeto pygame.Surface. Podemos localizar o texto em um lugar específico na janela obtendo o objeto Surface pelo método get_rect() para retornar um objeto retangulo pygame.Rect para a superfície e então definindo as coordenadas (x,y) do canto superior esquerdo do retângulo. Desta maneira, quando nós "blit" (isto é, desenhamos ele) a superficie MAINSURF (que é o objeto superfície para a janela), podemos passar o objeto retângulo para dizer onde na superficie MAINSURF desenhamos o texto.

        We do this twice. Once for the score text, and once for the directions.
        Fazemos isto duas vezes. Uma para o texto com a pontuação e uma para as direções. """

        if not waitingForInput:
            pygame.display.update()
            time.sleep(1)
            pattern.append(random.choice((YELLOW, BLUE, RED, GREEN)))
            """At the start of the game (and after the player has successfully entered the pattern), we will pause for a bit, add another color to the pattern, and then play the pattern back to the player. The random.choice() function takes a list or tuple, and returns one value in that list. It's an easy way to randomly select one of the colors to be the next color in the pattern.
            No começo do jogo (e depois do jogador ter acertado o padrão), pausaremos um pouco, adicionamos outra cor ao padrão e então enviamos o padrão devolta ao jogador.  A função random.choice() pega uma lista ou tupla e retorna um valor da lista. Esta é uma maneira fácil de selecionar aleatoriamente uma das cores para ser a próxima cor no padrão.

            Note that when the game first starts, pattern is just the blank list. So the append() call adds the first color of the pattern here.
            Note que quando o jogo primeiramente começa, o padrão é exatamente uma lista branca. Então, a chamada a append() adiciona a primeira cor no padrão aqui."""

            # Play the pattern.
            for button in pattern:
                flashButtonAnimation(button)
                time.sleep(FLASHDELAY)
            """Next, to play the pattern we have a for loop go through the color values in pattern and make each color flash in turn (with a slight delay in between them caused by the call to time.sleep()). See the code in the flashButtonAnimation() function for how we do this. Note that that function also contains the code to play the sounds when the button flashes.
               Em seguida, para jogar o padrão temos um laço "for" percorrendo os valores das cores no padrão e fazendo flash de cada cor (com um leve atraso entre eles causado pela chamada a função time.sleep()). Veja o código na função flashButtonAnimation() para saber como isto é feito. Note que a função também contém o código para reproduzir os sons quando o botão pisca. """

            waitingForInput = True
            """After playing the sequence, we want the game to accept button presses from the player so we set waitingForInput to True to tell the other part of the program that we are now expecting button presses.
             Depois de percorrer a sequência, queremos que o game aceite o botão pressionado pelo jogador e definimos waitingForInput para True para dizer as outras partes do programa que agora estamos esperando o botão pressionado. """

        # Handle any events.
        for event in pygame.event.get():
            """The pygame.event.get() function returns a list of pygame.Event objects of events that have happened since the last call to pygame.event.get(). This loop uses the same code to handle each event in this list.
            A função pygame.event.get() retorna uma lista de objetos pygame.Event de eventos que ocorreram desde a última chamada ao pygame.event.get(). Este laço usa o mesmo código para tratar cada evento nesta lista. """
            if event.type == QUIT:
                """The QUIT event is created when the user tries to shut down the program by clicking the X in the top right corner, or by killing the program from the task manager or some other means. Note that QUIT comes from pygame.locals.QUIT, but we can simply type QUIT because we used "from pygame.locals import *" instead of "import pygame.locals". The same applies for MOUSEMOTION, MOUSEBUTTONUP, KEYDOWN, and the keyboard constants such as K_ESCAPE and K_8 since these values are also in pygame.locals.
                O evento QUIT é criado quando o usuário tenta fechar o programa clicando em X no canto superior direito, ou  matando o programa a partir do gerenciador de tarefas ou outros meios. Note que QUIT vem de pygame.locals.QUIT, mas podemos simplesmente digitar QUIT porque usamos "from pygame.locals import *" ao invés de "import pygame.locals". O mesmo se aplica para MOUSEMOTION, MOUSEBUTTONUP, KEYDOWN e as constantes do teclado, tais como K_ESCAPE and K_8 uma vez que estes valores estão também em pygame.locals. """
                terminate()
            if event.type == MOUSEMOTION:
                """A MOUSEMOTION event is created whenever the user moves the mouse over the window. The Event object created has a pos attribute that is a tuple of the two xy integer coordinates for where the mouse is located. We will save these values off to mousex and mousey.
                Um evento MOUSEMOTION é criado sempre que o usuário move o mouse sobre a janela. O objeto "Event" criado tem um atributo "pos" que é uma tupla das duas coordenadas inteiras xy onde o mouse está localizado. Vamos salvar esses valores off em  mousex e mousey."""
                mousex, mousey = event.pos
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                clicked = getButtonClicked(mousex, mousey)
                """When the MOUSEBUTTONUP is created, we check if the mouse is currently over one of the color palettes (otherwise we can ignore it.) The bulk of this is implemented inside our getButtonClicked() function. This function returns None if the mouse wasn't over a button, or it returns the color value of the button.
                  Quando o MOUSEBUTTONUP é criado, vamos verificar se o mouse está atualmente sobre uma das paletas de cores (caso contrário podemos ignorá-lo.) A maior parte disto é implementado dentro da nossa função getButtonClicked(). Esta função retorna nada (None) se o mouse não estava sobre um botão, ou ela retorna o valor da cor do botão. """
            if event.type == KEYDOWN:
                """The KEYDOWN event is created when the user presses any key on the keyboard. We can tell which key the user pressed by looking at the value in event.key
                O evento KeyDown é criado quando o usuário pressiona uma tecla no teclado. Podemos dizer qual a tecla pressionada pelo usuário olhando o valor em event.key."""
                if event.key == K_ESCAPE:
                    terminate()
                    """The user can quit the game by clicking on the X button at the top of the window, or by hitting the Esc key. This just makes the program convenient to the player.
                       O usuário pode sair do jogo clicando no botão X na parte superior da janela, ou pressionando a tecla Esc. Isso faz o programa ser mais conveniente para o jogador."""
                if event.key == K_q or event.key == K_8:
                    clicked = YELLOW
                    """Pressing the 8 key or the q key will be the same as though the player clicked on the yellow button with the mouse. Notice that these are shorcuts. The player can either use the mouse, or use the 5, 6, 8, or 9 keys (or the q, w, a, or s keys) to enter the pattern. Note that the keys correspond to the position of the buttons drawn in the window:
                       Pressionando a tecla 8 ou a tecla q, seria o equivalente a se o jogador clicar no botão amarelo com o mouse. Observe que estes são cortes curtos. O jogador pode usar o mouse ou usar as teclas 5, 6, 8 ou 9 (ou do q, w, a ou as teclas s) para fornecer o padrão. Note que as chaves correspondem à posição dos botões desenhados na janela:

                        YELLOW  BLUE        8  9        q  w
                        RED     GREEN       5  6        a  s
                    """
                if event.key == K_w or event.key == K_9:
                    clicked = BLUE
                if event.key == K_a or event.key == K_5:
                    clicked = RED
                if event.key == K_s or event.key == K_6:
                    clicked = GREEN

        if waitingForInput:
            """If the program isn't playing the pattern to the player, then it is expecting the player to input button presses. The clicked variable will contain the color value of the most recent button that was clicked (if nothing was clicked, then clicked contains None). We need to handle what happens if the player clicked on the correct button and the incorrect button.
            Se o programa não está fornecendo o padrão ao jogador, então ele está esperando que o jogador pressione o botão de entrada. A variável clicada irá conter o valor da cor do botão mais recente que foi clicado (se nada foi clicado, então "clicked" não contém nada (None)). Precisamos tratar o que acontece se o jogador clicar no botão correto e no botão errado."""
            if clicked and clicked == pattern[currentStep]:
                """At the very beginning of entering the pattern, currentStep is equal to 0. We've set up our code so that this means the program is expecting the player to push the button corresponding to the color stored in pattern[0]. (Remember that 0 refers to the first item in the list, 1 refers to the second, and so on.)
                Bem no início de inserir o padrão, currentStep é igual a 0. Nós configuramos nosso código de modo que isso signifique que o programa espera o jogador apertar o botão correspondente à cor armazenada no pattern[0]. (Lembre-se que 0 refere-se ao primeiro item na lista, 1 refere-se ao segundo, e assim por diante.)

                Portanto, se o usuário clicou em um botão (ou seja, clicked contém algum valor) e a cor do botão que o jogador clicou é a mesma que se espera, então vamos dar um flash nesse botão e, em seguida incrementar currentStep para que o programa espere que o usuário clique no próximo botão do padrão.
                So if the user has clicked a button (meaning clicked does not contain None) and the color of the button the player clicked is the same one as is expected, then we will flash that button and then increment currentStep so the program expects the user to click the next button in the pattern."""
                # pushed the correct button
                flashButtonAnimation(clicked)
                currentStep += 1
                lastClickTime = time.time()
                """We set lastClickTime to the current time so we can tell if the player is taking too long to enter the next color.
                Definimos lastClickTime para o tempo atual, assim podemos dizer se o jogador está demorando muito para inserir a próxima cor."""

                if currentStep == len(pattern):
                    # pushed the last button
                    changeBackgroundAnimation()
                    score += 1
                    waitingForInput = False
                    currentStep = 0
                    """If currentStep has incremented to the same integer as the length of the pattern list, then we know the player just entered the last color of the pattern. We will change the background color (just for a nice decoration), increase the score by one point, reset currentStep back to 0 (so that once again we expect the player to enter the first color of the pattern), and set waitingForInput to False so that the program knows to display the pattern to the player.
                    Se currentStep tem incrementado ao mesmo número inteiro igual ao comprimento da lista pattern (padrão), então sabemos que o jogador inseriu a última cor do padrão. Mudaremos a cor de fundo (apenas para uma decoração agradável), aumentamos a pontuação em um ponto, reiniciamos currentStep voltando a 0 (para mais uma vez esperarmos o jogador inserir a primeira cor do padrão) e definimos "waitingForInput" como "False" para que o programa saiba mostrar o padrão ao jogador.

                    Lembre-se que, se nós temos 5 cores na lista pattern, então len(pattern) retornará 5, mas os índices das cores são 0-4 (isto é,pattenr[0], pattenr[1], pattenr[2],  pattern[3] e pattern[4].) É por isso que sabemos o que o jogador fez quando currentStep é igual a 5 e não igual a 4, mesmo que 4 é o índice da última cor no padrão. ""
                    Remember that if we have 5 colors in the pattern list, then len(pattern) will return 5, but the indexes of the colors are from 0 to 4 (that is, pattern[0], pattern[1], pattern[2], pattern[3] and pattern[4].) This is why we know the player is done when currentStep is equal to 5 and not equal to 4, even though 4 is the index of the last color in the pattern."""

            elif (clicked and clicked != pattern[currentStep]) or (currentStep != 0 and time.time() - TIMEOUT > lastClickTime):
                # pushed the incorrect button, or has timed out
                """The two main pieces in this rather long condition are separate by the or keyword:
                As duas partes principais nesta condição bastante longa são separadas pela palavra reservada "or":
                
                        1. (clicked and clicked != pattern[currentStep]) 
                        2. (currentStep != 0 and lastClickTime < time.time() - TIMEOUT)

                Let's look at these separately. Remember, since they are connected by the or keyword, only one of them has to be True for the code in this elif block to be executed.
                Vamos olhar para isto separadamente. Lembre-se, uma vez que eles estão conectados pela palavra reservada "or", apenas um deles tem que ser verdadeiro para que o código deste bloco "elif" seja executado.

                In the first part, clicked must be a non-False value (such as None) so we know that some button was clicked. Also, the button clicked must not be the color in the pattern we were currently expecting. This covers the case of if the player pressed the wrong button.
                Na primeira parte, "clicked" deve ser um valor não-falso (como None) e assim saberemos que algum botão foi clicado. Além disso, o botão clicado não deve ser a cor do padrão que estávamos esperando atualmente. Isto abrange o caso de se o jogador apertou o botão errado.

                In the second part, if we are not on the first step, and the current time minus the TIMEOUT value is greater than the time of the last button press. This covers the case where the player has not entered a color in a while, and so the player "times out" and loses. But we don't want the player to be able to time out on the first step (but once the player has begun entering steps, then currentStep will no longer be 0 and we expect them to keep up the pace.)
                Na segunda parte, se não estamos no primeiro passo e o tempo atual menos o valor do TIMEOUT é maior do que o tempo que foi pressionado o último botão. Isso abrange o caso em que o jogador não inseriu nenhuma cor em um espaço de tempo, e assim o tempo expira e o jogador perde. Mas nós não queremos que o jogador sofra "time out" já na primeira etapa (mas uma vez que o jogador começou a inserir passos, então "currentStep" deixará de ser 0 e esperamos que ele mantenham o ritmo. """

                gameOverAnimation()
                pattern = []
                currentStep = 0
                waitingForInput = False
                score = 0
                time.sleep(1)
                """Here we reset the game so that the player can start over. The pattern list is set to be empty, currentStep is back to 0, waitingForInput is False (so that we show the initial pattern to the player), and setting the score back to 0. On the next iteration of the game loop, it will be as though the player just started playing.
                   Aqui vamos reiniciar o jogo, então o jogador pode começar de novo. Define-se a lista "pattern" como sendo vazia, "currentStep" volta a ser 0, "waitingForInput" é False (falso) (para que possamos mostrar o padrão inicial para o jogador), e definindo a pontuação para 0. Na próxima iteração do laço do jogo, será como se o jogador tivesse apenas começado a jogar. """
        pygame.display.update()
        MAINCLOCK.tick(FPS)
        """A call to pygame.display.update() causes any drawing functions done to the MAINSURF pygame.Surface object to be drawn to the screen. Unlike other pygame.Surface object, the object stored in MAINSURF was the one returned by the pygame.display.set_mode() call, which is why it is the Surface object that is drawn to the screen when pygame.display.update() is called.
        Uma chamada a pygame.display.update() faz todas as funções de desenho feitas para o objeto pygame.Surface MAINSURF serem desenhadas na tela. Ao contrário de outros objetos pygame.Surface, o objeto armazenado em MAINSURF foi o retornado pela chamada a pygame.display.set_mode (), que é por isso que o objeto Surface é desenhado na tela quando pygame.display.update() é chamada.

        The call to MAINCLOCK.tick(FPS) will introduce a pause to the game so that the program doesn't run faster than 30 frames per second. (30 is the value we stored inside the FPS constant.) This is so that our program doesn't run too fast on very powerful computer.
        A chamada a MAINCLOCK.tick (FPS) introduzirá uma pausa no jogo para que o programa não seja executado mais rápido do que 30 frames (quadros) por segundo. (30 é o valor que foi armazenado dentro da constante FPS.) É por isso que nosso programa não é executado muito rápido em computadores muito potente."""

def terminate():
    """In order to terminate the program, we must call both pygame.quit() (to shut down the Pygame engine) and sys.exit() (to shut down the program.) Calling sys.exit() without calling pygame.quit() first probably won't harm anything, though it does give IDLE some problems if the user runs this program from it. It's just considered a graceful way to shut down the Pygame library.
    Com o objetivo de terminar o programa, devemos chamar ambos pygame.quit() (para desligar o mecanismo Pygame) e sys.exit() (para desligar o programa). Chamar sys.exit() sem primeiro chamar pygame.quit() provavelmente não vai prejudicar nada, embora ele dê alguns problemas IDLE se o usuário executar este programa a partir dele. É apenas considerada uma maneira graciosa para encerrar a biblioteca Pygame. """
       
    pygame.quit()
    sys.exit()


def flashButtonAnimation(color, animationSpeed=50):
    if color == YELLOW:
        sound = BEEP1
        flashColor = BRIGHTYELLOW
        rectangle = YELLOWRECT
    if color == BLUE:
        sound = BEEP2
        flashColor = BRIGHTBLUE
        rectangle = BLUERECT
    if color == RED:
        sound = BEEP3
        flashColor = BRIGHTRED
        rectangle = REDRECT
    if color == GREEN:
        sound = BEEP4
        flashColor = BRIGHTGREEN
        rectangle = GREENRECT
    """Before we can make one of the buttons appear to "flash" on the screen and play a sound, we need to know which button it is. Depending on the color passed as the parameter to flashButtonAnimation(), we set the sound, flashColor, and rectangle variables accordingly.
       Antes de podermos fazer um dos botões aparecerem como "flash" na tela e tocar um som, precisamos saber qual botão é. Dependendo da cor passada como parâmetro para flashButtonAnimation(), vamos definir o som, flashColor e as variáveis em conformidade com o retângulo."""
    origSurf = MAINSURF.copy()
    """We will produce the button flashing effect this way: First, we save a copy of MAINSURF away as it looks before we flash the button.
       Produziremos o efeito piscante do botão desta maneira: primeiro, salvamos uma cópia do MAINSURF diferente de como parece, antes de piscar o botão."""
    flashSurf = pygame.Surface((BUTTONSIZE, BUTTONSIZE))
    """Second, we will then create a new surface the same size as the MAINSURF surface.
       Segundo, criaremos uma nova superfície do mesmo tamanho da superfície MAINSURF."""
    flashSurf = flashSurf.convert_alpha()
    """Third, we allow this surface to have semi-transparent pixels on it by calling its convert_alpha() method. Normally surfaces have completely opaque pixels, so if we blit (that is, draw) a surface onto another, it completely overlaps the lower surface. With transparent pixels, we can "see through" the pixels and see the pixels on the lower surface. This will look a lot like seeing something through stained glass.
    Terceiro, permitimos que esta superfície tenha pixels semi-transparente sobre ela, chamando o método convert_alpha(). Normalmente, as superfícies têm pixels completamente opacos, assim podemos desenhar uma superfície sobre a outra, e ela sobrepõe completamente a superfície inferior. Com pixels transparentes, podemos "ver através" dos pixels e ver os pixels na superfície inferior. """
    r, g, b = flashColor
    """In order to create a color will a certain level of transparency, we first need the red, green, and blue values of the "flash color". Since flashColor is really a tuple of three integers, we can use the multiple assignment trick to grab the values out of the tuple.
    Com o objetivo de criar uma cor com um certo nível de transparência, primeiro precisamos dos valores vermelho, verde e azul dos "flash color". Uma vez que flashColor é uma tupla de inteiros, podemos usar a declaração múltipla para gravar os valores fora da tupla.

    More information on the multiple assignment trick is at http://inventwithpython.com/chapter9.html#MultipleAssignment
    Mais informações sobre a estratégia de declaração múltipla em : http://inventwithpython.com/chapter9.html#MultipleAssignment
    """
    sound.play()
    """We play the appropriate beep noise with the pygame.mixer.Sound object's play() method. Notice that this sound will play in the background. The program will not stop until the sound has finished playing, rather it will start playing the sound and then immediately continue on to the next line of code. This is why we want to call play() before we start the flashing animation, rather than after it.
    Tocamos o ruído sonoro apropriado com o objeto pygame.mixer.Sound  e o método play(). Note que este som vai tocar no fundo. O programa não vai parar até o som terminar de tocar, em vez disso, começará a tocar o som e então, imediatamente continua na próxima linha do código. Isto é porque queremos chamar play() antes de começar a animação de flash, ao invés de depois."""
    for start, end, step in ((0, 255, 1), (255, 0, -1)):
        """In order to pull off the flashing effect, we will first repeatedly show the brighter button color with increasing levels of opaque-ness. The "alpha" value of a pixel is how opaque it is. An alpha value of 255 is a maximumly solid, opaque color that you cannot see through at all. An alpha value of 0 means the color is completely invisible and you can see perfectly through it. Think of any color with an alpha value of 0 as the "color of glass".
        Com o objetivo de tirar os efeitos do flash, primeiro mostraremos repetidamente a cor do botão brilhante com níveis crescentes de ness-opacos. O valor "alpha" de um pixel é como se fosse opaco. Um alpha de 255 é uma máxima sólida, cor opaca que você não pode ver através de tudo. Um valor alpha de 0 significa que a cor é completamente invisível e você pode ver perfeitamente através dela. Pense em qualquer cor com um valor de alpha 0 como a "cor do vidro."
        
        We then want to repeatedly show the brighter-colored surface with decreasing levels of alpha values. This will be the button returning to its normal color. In effect, the outer for loop will always loop twice. The first time, it sets the start, end, and step variables will be set to 0, 255, and 1 respectively. Then on the second iteration through the outer for loop, start, end, and step will be set to 255, 0, and -1 respectively.
        Assim, queremos repetidamente mostrar a superfície colorida e mais brilhante com os valores alpha em níveis decrescentes. Isto fará o botão retornar a sua cor normal. Na verdade, o laço "for" de fora sempre será duas vezes o laço(loop). A primeira vez, ele define as variáveis "start", "end" e "step" que serão definidos com 0, 255 e 1 respectivamente. Então, na segunda iteração percorrendo o laço "for" de fora, "start", "end" e "step" serão definidos como 255, 0 e -1 respectivamente. 
        
        These values will control the inner for loop.
        Estes valores controlarão o loop interno."""
        for alpha in range(start, end, animationSpeed * step):
            """This is the inner for loop. Notice that instead of providing integers to the range() variable like we normally do, we have provided variables. Remember that the three parameters of range() are the starting value, the ending value, and the step value.
            Este é o laço "for" interno. Note que ao invés de fornecer inteiros para a variável range() como normalmente fazemos, nós fornecemos variáveis. Lembre-se que os três parâmetros de range() são o valor inicial, o valor final e o valor do passo.

            So range(0, 10, 2) would iterate through 0, 2, 4, 6, and 8. (It loops up to, but not including, the end value.)
            Então range(0, 10, 2) deve iterar percorrendo 0, 2, 4, 6 e 8. (Ele percorre até o fim, mas não inclue o valor final.)

            The values never go at or beyond the end value. So range(0, 10, 4) would go through 0, 4, and 8 only.
            Os valores nunca vão até ou além do valor final. Assim range(0, 10, 4) vai até 0, 4 e o somente.
             
            In effect, the first time the program encounters the inner for loop, we will evaluate range(0, 255,  50 * 1) (unless some other value is provided for flashButtonAnimation()'s animationSpeed parameter). So the integers it goes through will be 0, 50, 100, 150, 200, and 250.
            Na verdade, a primeira vez que o programa encontra o loop "for" interno, avaliaremos range(0, 255, 50 * 1) (a menos que um outro valor seja fornecido pelo parâmetro flashButtonAnimation()'s animationSpeed). Assim os números inteiros percorridos serão 0, 50, 100, 150, 200 e 250.
            
            The second time the program encounters the inner for loop, it will evaluate range(255, 0, 50 * -1). This means that the step value will be -50, and the integers will decrease rather than increase. So the integers it goes through will be 255, 195, 145, 95, and finally 45.
            A segunda vez que o programa encontra o laço "for" interno, avaliaremos o range(255, 0, 50 * -1). Isto significa que o valor da variável "step" será -50, e os inteiros diminuirão ao invés de aumentarem. Então os números inteiros percorridos serão 255, 195, 145, 95 e finalmente 45.

            This will provide the increasing, and then decreasing, alpha values for our button flash animation.
            Isto fornecerá o aumento e então a diminuição dos valores alpha para nosso botão de animação em flash."""
            checkForQuit()
            """While the buttons are flashing, we just want to check for any QUIT events in case the player wants to stop the game in the middle of a pattern that is being played. Our chekcForQuit() function does exactly this.
            Enquanto os botões estão piscando, somente queremos checar os eventos QUIT no caso do jogador querer parar o jogo no meio do padrão que foi começado. Nossa função chekcForQuit() faz exatamente isto."""
            flashSurf.fill((r, g, b, alpha))
            """Now we fill the flashSurf with this color with a certain level of transparency. Colors in Pygame are usually represented as a tuple of three integers (for the red, green, and blue values of the color.) However, you can also use tuples of four integers, with the fourth integer being the alpha value. Remember in this for loop, through the iterations the alpha value first starts low and then increases, and then starts high and decreases.
            Agora preenchemos a flashSurf com esta cor com um certo nível de transparência. Cores no Pygame são normalmente representadas como uma tupla de três inteiros (para os valores vermelho, verde e azul da cor.) No entanto, vc também pode usar tuplas de quatro inteiros, com o quarto inteiro sendo o valor alpha. Lembre-se que neste laço "for" , através das iterações o valor de alfa primeiro começa baixo e depois aumenta, e então começa alto e diminui.

            Imagine this layer as painted entirely with the color in flashColor (where we got the RGB values) except as stain glass that you can slightly see through (depending on the alpha vlaue).
            Imagine esta camada pintada inteiramente com a cor em flashColor(onde usamos os valores RGB) exceto como "vidro colorido" que podemos ver ligeiramente através dele(dependendo do valor de alpha)."""
            MAINSURF.blit(origSurf, (0, 0))
            """Next we draw how MAINSURF originally looked (which we saved off a copy of to a pygame.Surface object in origSurf) onto the window. (Though it doesn't actually show up on the screen until we call pygame.display.update()).
            Em seguida desenhamos como MAINSURF originalmente será vista (a qual salvamos uma cópia do objeto pygame.Surface em origSurf) na janela. (Embora ela realmente não aparecerá na tela até que chamamos pygame.display.update())."""
            MAINSURF.blit(flashSurf, rectangle.topleft)
            """Then, on top of the original-looking MAINSURF, we draw the semi-transparent color on top of it.
            Então, na parte superior da MAINSURF, desenhamos em cores semi-transparente sobre o topo dela. """
            pygame.display.update()
            MAINCLOCK.tick(FPS)
            """Now we display our surface on the screen, and call MAINCLOCK.tick() to handle the timing issue to introduce the needed amount of pause time.
            Agora mostaremos nossa superfície na tela, e chamamos MAINCLOCK.tick() para tratar o problema de tempo para introduzir a quantidade necessária de tempo de pausa."""
    MAINSURF.blit(origSurf, (0, 0))
    """At this point, we're done with the flashing button animation, and we redraw the original-looking surface back onto MAINSURF.
    Neste ponto, estamos prontos com a botão de animaçao dos flashs e re-desenhamos a superfície original de volta em MAINSURF."""


def changeBackgroundAnimation(animationSpeed=40):
    global BGCOLOR
    """This animation routine will change the color of the background by fading into the background color to the new (and randomly chosen) background color. This fading effect will be done in a similar way that we did the button flashing animation: draw the new color surface on top of the original surface with increasing alpha values.
    Esta rotina de animação mudará a cor do fundo substituindo-a pela nova cor (aleatoriamente escolhida). Este efeito descolorante será feito de uma maneira similar a que fizemos com o botão da animação do flash. Desenhamos a nova superficie colorida na parte superior da superfície orginal aumentando o valor de alpha.
    Since we are altering the value stored in BGCOLOR (which is a global variable since it was first defined outside of any function) we need to have the "global BGCOLOR" statement at the top of the function. Otherwise Python will think we are creating a new local variable that just happens to have the same name as BGCOLOR.
    Já que estamos alterando o valor armazenado em BGCOLOR (que é uma variável global e que primeiro foi definida fora de qualquer função), precisamos ter a declaração "global BGCOLOR" no topo da função. Caso contrário Python pensará que estamos criando uma nova variável local, que é o que justamente ocorre se tivermos o mesmo nome BGCOLOR."""
    newBgColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    """We store the new background color in newBgColor. The three integers for the RGB values are randomly generated with calls to random.randint().
    Armazenamos a nova cor de fundo em "newBgColor". Os três inteiros para os valores RGB são aleatoriamente gerados com chamadas a random.randint()."""

    newBgSurf = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT))
    newBgSurf = newBgSurf.convert_alpha()
    """We will need a new surface to draw the semi-transparent pixels to. By calling the surface's convert_alpha() method, we will allow it to have transparent pixels on it.
    Precisamos de uma nova superfície para desenhar os pixels semi-transparentes. Chamando o método surface's convert_alpha(),  permitiremos ter pixels transparentes sobre ela."""
    r, g, b = newBgColor
    for alpha in range(0, 255, animationSpeed):
        checkForQuit()
        MAINSURF.fill(BGCOLOR)

        newBgSurf.fill((r, g, b, alpha))
        MAINSURF.blit(newBgSurf, (0, 0))

        drawButtons()
        """This is a simple four step process to produce the final surface. First, we fill the entire MAINSURF surface with the old background color.
        Isto é um simples de quatros passos para produzir a superficie final. Primeiro, preenchemos totalmente a superfície MAINSURF  com a cor de fundo antiga.

        Second, we draw the new background color (with a certain alpha value) on a different surface called newBgSurf.
        Segundo, desenhamos a nova cor de fundo (com um certo valor de alpha) sobre uma superficie diferente chamando newBgSurf.
        
        Third, we draw this new surface on top of MAINSURF, which colors the old background much like stain glass would.
        Terceiro, desenhamos esta nova superfície na parte superior da MAINSURF, com as cores antigas do fundo como um vidro manchado.

        Finally, we draw the four buttons on top of this, so that they are not affected by the transparent pixels (so only the background undergoes the fade effect, no the buttons.)
        Finalmente, desenhamos quatro botões na parte superior disto, de modo que eles não sejam afetados pelos pixels transparentes (então somente o fundo sofre o efeito de descoloramento, não os botões)

        Note that the Score and Directions text is not drawn during this animation, so they temporarily don't appear on the screen while the program execution is in this function.
        Note que a pontuação e o texto das direções (Directions text) não são desenhados durante esta animação, assim, eles temporariamente não aparecem na tela, enquanto a execução do programa está nesta função."""
        pygame.display.update()
        MAINCLOCK.tick(FPS)
    BGCOLOR = newBgColor
    """Finally, we set the background color to be the new background color.
    Finalmente, definimos a cor de fundo para ser a nova cor de fundo."""


def gameOverAnimation(color=WHITE, animationSpeed=50):
    """The code for this animation is almost identical to flashButtonAnimation(), so we will omit the comments here.
    O código para esta animação é muito parecido ao flashButtonAnimation(), então omitiremos os comentários aqui."""
    # play all beeps at once, then flash the background
    origSurf = MAINSURF.copy()
    flashSurf = pygame.Surface(MAINSURF.get_size())
    flashSurf = flashSurf.convert_alpha()
    BEEP1.play()
    BEEP2.play()
    BEEP3.play()
    BEEP4.play()
    """Note that at the start of the Game Over animation, we play all four beeps at once. Really, we begin playing them one at a time, but the computer starts them so fast after each other that it basically sounds like they are being played at the same time.
    Note que no começo da animação Game Over, tocamos todos os quatro sonidos de uma vez. Na verdade, começamos tocando-os em um tempo, mas o computador começa tão rápido cada um deles que é basicamente como se fossem tocados no mesmo tempo."""
    r, g, b = color
    for i in range(3):
        for start, end, step in ((0, 255, 1), (255, 0, -1)):
            for alpha in range(start, end, animationSpeed * step):
                checkForQuit()
                flashSurf.fill((r, g, b, alpha))
                MAINSURF.blit(origSurf, (0, 0))
                MAINSURF.blit(flashSurf, (0, 0))
                drawButtons()
                pygame.display.update()
                MAINCLOCK.tick(FPS)
        MAINSURF.blit(origSurf, (0, 0))


def drawButtons():
    """This function simply draws the four colored buttons to the MAINSURF surface. Remember, of course, that this will not appear on the screen until pygame.display.update() is called. (And it is not called inside this function.)
    Esta função simplesmente desenha os quatro botões coloridos na superfície MAINSURF. Lembre-se, é claro, que isto não aparecerá na tela até que pygame.display.update() seja chamada. (E ela não é chamada dentro desta função.)"""
    pygame.draw.rect(MAINSURF, YELLOW, YELLOWRECT)
    pygame.draw.rect(MAINSURF, BLUE, BLUERECT)
    pygame.draw.rect(MAINSURF, RED, REDRECT)
    pygame.draw.rect(MAINSURF, GREEN, GREENRECT)


def getButtonClicked(x, y):
    """The getButtonClicked() value gets the x and y coordinates of a mouse click, and determines if the click took place inside one of the four buttons. Remember that the YELLOWRECT variables holds a pygame.Rect object that stores the location and size information for the yellow button on the screen. (And the same for the other three buttons.)
    Os valores getButtonClicked() pega os valores das coordenadas x e y do clique do mouse e determina se o clique está localizado dentro de um dos quatro botões. Lembre-se que as variáveis YELLOWRECT mantém um objeto pygame.Rect que armazena as informações sobre a localização e o tamanho do botão amarelo na tela. (E o mesmo para cada um dos outros três botões.) 

    We pass a tuple of the (x, y) values of the mouse click to the pygame.Rect object's collidepoint() method, which returns True if the point is inside the rectangle and False if it is not. This function then returns the color value of the button's color. If the point is not in any of the four buttons, this function returns None.
    Passamos a tupla dos valores (x,y) do clique do mouse para o objeto pygame.Rect pelo método collidepoint(), que retorna (True) verdadeiro se o ponto está dentro do retângulo e (False) falso se não. Está função retorna então o valor da cor dos botões coloridos. Se o ponto não está em nenhum dos quatro botões, está função retorna vazio (None)."""
    if YELLOWRECT.collidepoint( (x, y) ):
        return YELLOW
    if BLUERECT.collidepoint( (x, y) ):
        return BLUE
    if REDRECT.collidepoint( (x, y) ):
        return RED
    if GREENRECT.collidepoint( (x, y) ):
        return GREEN

    return None


def checkForQuit():
    for event in pygame.event.get(QUIT):
        """This function checks for any pygame.event.Event objects generated, except by passing QUIT to pygame.event.get() we only pull out any QUIT events, and ignore any mouse clicks or keyboard presses. This is handy since we only want to check for QUIT events. Note though, that if the user presses the Escape key, we won't terminate the program.
         Esta função checa para qualquer objeto pygame.event.Event gerado, exceto passando QUIT para o pygame.event.get() somente deixamos fora quaisquer eventos QUIT e ignoramos quaisquer cliques do mouse ou pressionadas do teclado. Isto é útil, uma vez que só queremos checar os eventos QUIT. Note porém, que se o usuário pressionar a tecla Escape, não vamos encerrar o programa."""
        if event.type == QUIT:
            terminate()


if __name__ == '__main__':
    main()
    """This if statement is actually the first line of code that is run in our program (aside from the import statements and the constant variable assignments. __name__ is a special variable that is created for all Python programs implicitly. The value stored in this variable is the string '__main__', but only when the script is run by itself. If this script is imported by another script's import statement, then the value of __name__ will be the name of the file (if this script still has the name simulate.py, then the __name__ variable will contain 'simulate').
    Esta declaração "if" é efetivamente a primeira linha de código que é executada em nosso programa (além das declarações de importação e as atribuições de variável constantes. __name__  é uma variável especial que é criada implicitamente para todos os programas Python. O valor armazenado nesta variável é a string '__main__', mas somente o script é executado por si mesmo). Se este script é importado por outro script importado, então o valor de __name__ será o nome do arquivo (se este script tem o nome simulate.py, então a variável __name__ contém 'simulate').

    This is really handy if we ever want to use the functions that are in this program in another program. By having this if statement here, which then runs the main() function, we could have another program use "import simulate" and make use of any of the functions we've already written. Or if you want to test individual functions by calling them from the interactive shell, you could call them without running the game program. This trick is really handy for code reuse.
    Isso é realmente útil se quisermos usar as funções que estão neste programa em outro programa. Por ter essa instrução "if" aqui, que executa a função main (), poderíamos ter um outro programa usando "import simulate" e fazer uso de qualquer uma das funções que já escrevemos anteriormente. Ou se você quiser testar funções individuais, chamando-as a partir do shell interativo, você poderia chamá-las sem rodar o programa do jogo. Esta estratégia é realmente útil para a reutilização do código."""
