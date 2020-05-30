# Flippy (an "Othello" or "Reversi" clone)
# http://inventwithpython.com/blog
# By Al Sweigart al@inventwithpython.com

"""IMPORTANT NOTE: All of the "logic" part of this program (the code for the AI player and code that handles game play) is basically copied and pasted from the text-based Othello game that was featured in the "Invent Your Own Computer Games with Python" book (freely available at http://inventwithpython.com).

You might want to read through that code and chapter 15 of the book before looking through this code, because I really only cover the Pygame parts in the source code. http://inventwithpython.com/chapter15.html

Basically, this program == (old text-based othello program) - (text & keyboard stuff) + (Pygame graphics & mouse stuff).

You should compare the code between these two programs to see how you could go about reusing other people's code and giving it a new makeover.
"""

"""
Welcome to the Code Comments for Flippy, an Othello clone. Code Comments is a series of simple games with detailed comments in the source code, so you can see how the game works.

The text in between the triple-double-quotes are comments. The Python interpreter ignores any text in between them, so we can add any comments about the source code without affecting the program. In general for Code Comments, the comments will describe the lines of code above the comment. It helps to view this file either on the Code Comments site or with a text editor that does "syntax highlighting", so that the comments appear in a separate color and are easier to distinguish from the code.

This Code Comments assumes you know some basic Python programming. If you are a beginner and would like to learn computer programming, there is a free book online called "Invent Your Own Computer Games with Python" at http://inventwithpython.com

The Code Comments programs make references to sections of this book throughout the program. This Code Comments can also teach you how to use the Pygame library to make your own games with graphics, animation, and sound. You can download Pygame from http://pygame.org and view its documentation at http://pygame.org/docs/

HOW TO PLAY FLIPPY
Place down tiles so that you have your opponent's tiles in between your newly placed tile and one of your existing tiles. All of your opponent's surrounded tiles will be flipped to become your colored tiles. You and the computer take turns placing down tiles until no more moves can be made. The player with the most tiles of their color on the board at the end wins.

Note that tiles on the side of the board are less likely to be surrounded, and any tiles on the corners can never be flipped.

There is a hints mode which can be toggled on to show you every valid move you can make on the board.
"""


import random
import sys
import pygame
from pygame.locals import *
import time
"""Here we import modules that our game needs. random has random number functions, time has the sleep() function, sys has the exit() function, and pygame contains all the pygame-related functions.

pygame.locals contains constants like MOUSEMOTION and MOUSEBUTTONUP and QUIT for the events. It's easier to type MOUSEBUTTONUP instead of pygame.locals.MOUSEBUTTONUP, so we use the "from pygame.locals import *" format to import these to the local namespace.
"""

FPS = 10 # frames per second to update the screen
WINDOWWIDTH = 640 # width of the program's window, in pixels
WINDOWHEIGHT = 480 # height in pixels
SPACESIZE = 50 # width & height of each space on the board, in pixels
BOARDWIDTH = 8 # how many columns of spaces on the game board
BOARDHEIGHT = 8 # how many rows of spaces on the game board
"""These constant variables (the uppercase names means we shouldn't change the values stored in them) set some standard values for our game. You can play around with different values for them (though some values might cause bugs in the game.) By using constants instead of the values directly, it is easier to make changes since we only have to change them in one place.

For example, if we used 20 instead of SPACESIZE, then if we wanted to change our code later we'd have to change every place in the code we find 20. This is trickier than just changing the one line where SPACESIZE is originally set.

WINDOWWIDTH and WINDOWHEIGHT give the size of the window in pixels. FPS is how often we redraw the image to the screen in frames per second. SPACESIZE is the size (in pixels) of the individual space that make up the tetromino pieces. Because the spaces are squares, SPACESIZE will be used for both the space width and height.

BOARDWIDTH and BOARDHEIGHT give the size of the playing board, in blocks. An 8 x 8 board is 64 spaces big (that is, 8 times 8).

More information about constants is at http://inventwithpython.com/chapter9.html#ConstantVariables
"""

# Amount of space on the left & right side (XMARGIN) or above and below (YMARGIN) the game board, in pixels.
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * SPACESIZE)) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * SPACESIZE)) / 2)
"""XMARGIN and YMARGIN are technically constants, since the values in these variables never change. The value we put inside of these constants are calculated from the values of other constants.

We want to calculate how much horizontal space is on either side of the board. This depends on the width of the window, the width of the board, and the size of each space. We take the full width of the window, and want to subtract the width of the board in pixels (which is BOARDWIDTH * BLOCKSIZE). This gives us the amount of space on either side of the board, so we divide by two to get the width of just one of these margins. We do the same for the margin on top and on the bottom of the board."""

# Colors used in the game
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 155, 0)
BRIGHTBLUE = (0, 50, 255)
BROWN = (174, 94, 0)

BGCOLOR = BRIGHTBLUE
BOARDBGCOLOR = GREEN
GRIDLINECOLOR = BLACK
TEXTCOLOR = WHITE
XPLAYERCOLOR = WHITE
OPLAYERCOLOR = BLACK
HINTCOLOR = BROWN
"""We also set up some constant values for different colors. Pygame uses tuples of three integers to represent color. The integers represent the amount of red, green, and blue in the color (this is commonly called a RGB). 0 means there == None of the primary color in the color, and 255 means there is the maximum amount. So (255, 0, 0) is red, since it has the maximum amount of red but no green or blue. But (255, 0, 255) adds the max amount of blue with the red, creating purple.

First we set some color constants with the 3-tuple values, and then assign other constants to these color constants. It is much easier to see that the background color is bright blue with BGCOLOR = BRIGHTBLUE rather than BGCOLOR = (0, 50, 255)

BGCOLOR will store the color we use for behind the game board. BOARDBGCOLOR is the color of the board itself, and GRIDLINECOLOR is the color used for the lines in between each space.

All the text in the game will be the same color (stored in TEXTCOLOR). We will be using the 'X' and 'O' string values (mostly because it is simple and this was how it was done in the text version of this program) but we will want XPLAYERCOLOR and OPLAYERCOLOR to remember what colors 'X' and 'O' stand for. HINTCOLOR is the size of the small boxes that appear in hint mod.

More information about colors is at http://inventwithpython.com/chapter17.html#ColorsinPygame
"""

def main():
    global MAINCLOCK, MAINSURF, FONT, BIGFONT
    """The main() function is where our program begins. (See the last two lines of code to see why.) Because we define MAINCLOCK, MAINSURF, FONT, and BIGFONT inside this function, these are local variables to the main() function and the names MAINSURF and such won't exist outside of this function. By using a global statement, we can tell Python that we want these variables to be global variables.

    More information about global and local variables is at http://inventwithpython.com/chapter6.html#VariableScope
    """

    pygame.init()
    MAINCLOCK = pygame.time.Clock()
    MAINSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Flippy')
    FONT = pygame.font.Font('freesansbold.ttf', 16)
    BIGFONT = pygame.font.Font('freesansbold.ttf', 32)
    """pygame.init() needs to be called before any of the other Pygame functions.

    pygame.time.Clock() returns a pygame.Clock object. We will use this object's tick() method to ensure that the program runs at no faster than 15 frames per second (or whatever integer value we have in the FPS constant.)

    pygame.display.set_mode() creates the window on the screen and returns a pygame.Surface object. Any drawing done on this Surface object with the pygame.draw.* functions will be displayed on the screen when we call pygame.display.update().

    More information about pygame.display.set_mode() is at http://inventwithpython.com/chapter17.html#ThepygamedisplaysetmodeandpygamedisplaysetcaptionFunctions

    The call to the pygame.font.Font() constructor function creates a Font object. We will store this Font object in the global variable FONT (and make a different Font object to store in BIGFONT)."""

    while playGame() == True:
        pass
        """This is a rather unusual piece of code. What we want to do is keep calling playGame() as long as the call to playGame() returns True (which indicates that the player wants to play another game.) So when this while statement's condition is first evaluated, we call playGame() which goes through an entire game of Flippy with the player. When that game is over, playGame() will either return True or False. If it returns False, then the while statement's condition will evaluate to False and program execution will jump past the while loop. (This will be at the end of the main() function, meaning that the function returns and eventually the program terminates.)

        If playGame() returns True, then that indicates that the player wants to play another game. So the while statement's condition will also evaluate to True and program execution jumps inside the while loop's block. But the only piece of code inside this block is a pass statment.

        The pass statement does absolutely nothing (just like a comment does nothing.) After executing the pass statement (that is, after doing nothing), we reach the end of the while loop so we jump back to and reevaluate the while loop's condition. Of course, in the process of evaluating the condition again, the playGame() function is called and an entire game of Flippy is played out again.

        The reason we need a pass statement here is because the Python interpreter expects SOMETHING inside the while loop block. If we just had nothing after the while statement, then the next line of code would be interpretted as the first line of the while loop. Most likely this line of code would have the wrong level of indentation, and this would cause an error in our program.

        Alternatively, we could replace this code with the following which would do the exact same as above:

        while True:
            if playGame() == True:
                break

        But this form would be a bit more verbose, and we can simplify it as the above code."""

def playGame():
    # Plays a single game of reversi each time this function is called.

    # Reset the board and game.
    mainBoard = getNewBoard()
    resetBoard(mainBoard)
    showHints = False
    turn = whoGoesFirst()
    """This code sets up the beginning of a new game. We generate a blank board data structure by calling getNewBoard(). Of course, the start of a game of Flippy isn't a blank board, but has four tiles already placed at the center of the board. The resetBoard() function will handle this for us.

    Then we start off with hints mode disabled (represented by the False value in the showHints variable.) Then we call whoGoesFirst() to randomly determine if the human player or the computer gets to go first."""

    # Draw the starting board and ask the player what color they want to be.
    drawBoard(mainBoard)
    playerTile, computerTile = enterPlayerTile()
    """We do an initial drawing of the starting board to the screen, and then we display the menu that asks what color the player wants to be."""

    # Make the text for the "New Game" and "Hints" buttons
    newGameSurf = FONT.render('New Game', True, TEXTCOLOR, BOARDBGCOLOR)
    newGameRect = newGameSurf.get_rect()
    newGameRect.topright = (WINDOWWIDTH - 8, 10)
    hintsSurf = FONT.render('Hints', True, TEXTCOLOR, BOARDBGCOLOR)
    hintsRect = hintsSurf.get_rect()
    hintsRect.topright = (WINDOWWIDTH - 8, 40)
    """These six lines create the pygame.Surface and pygame.Rect objects we will use to draw the "New Game" and "Hints" buttons on the screen. First we call FONT.render() to create a pygame.Surface object that has the text written on it. We store this object in newGameSurf (or hintsSurf for the "Hints" button).

    Next we get a pygame.Rect() object that represents the size and position of this surface object, and store this in newGameRect (or hintsRect).

    Third, we set the topright corner of the Rect object so we can place the buttons in the window. Notice that the newGameRect and hintsRect have the same x coordinate (WINDOWWIDTH - 8), but different y coordinates (10 and 40, respectively). This puts the "Hints" button slightly below the "New Game" button.

    Note that the buttons are not yet drawn on the screen, we are just setting them up for now."""

    while True:
        # Keep looping for player and computer's turns.
        """This is where the main part of the game takes place. We have an infinite loop (the "while True:" loop) that handles player input, updating the state of the game world, and displaying the game world on the screen. The part before the infinite loop sets up variables for the start of a game. When the game is over, we return from this function.

        The turn variable keeps track of whose turn it is, and will always have either the string 'player' or 'computer' in it."""

        if turn == 'player':
            # Player's turn.
            move = None
            while move == None:
                # Keep looping until the player clicks on a valid space.

                # Determine if we should show a board with hints marked or not.
                if showHints:
                    boardToDraw = getBoardWithValidMoves(mainBoard, playerTile)
                    """The getBoardWithValidMoves() function modifies the board data structure we pass it to set '.' strings in every position where the player can make a move. Our code in drawBoard() will later read these '.' strings and draw little brown squares on all the spaces the player could possibly go."""
                else:
                    boardToDraw = mainBoard
                    """If hints mode is disabled (that is, showHints stores the False value), then we just use the regular board data structure without adding the '.' strings."""

                # Process all events.
                for event in pygame.event.get():
                    """Here we loop through all the events in the event queue. The pygame.event.get() function will return a list of pygame.event.Event objects that have been generated since the last time pygame.event.get() was called. An Event object is generated whenever the player presses a key, clicks the mouse, tries to shut down the program, move sthe mouse, and many other situations.

                    More info on events can be found here: http://inventwithpython.com/chapter18.html#EventsandHandlingtheKEYDOWNEvent
                    """
                    if event.type == QUIT:
                        terminate()
                        """The QUIT event is created when the user tries to shut down the program by clicking the X in the top right corner, or by killing the program from the task manager or some other means. Note that QUIT comes from pygame.locals.QUIT, but we can simply type QUIT because we used "from pygame.locals import *" instead of "import pygame.locals". The same applies for MOUSEMOTION, MOUSEBUTTONUP, KEYDOWN, and the keyboard constants such as K_ESCAPE and K_p since these values are also in pygame.locals."""
                    if event.type == MOUSEBUTTONUP:
                        # Handle mouse click events
                        mousex, mousey = event.pos
                        """When the MOUSEBUTTONUP is created, we check if the mouse click happened over one the "New Game" button, the "Hints" button, or one of the spaces on the board (otherwise we can ignore it.)"""
                        if newGameRect.collidepoint( (mousex, mousey) ):
                            # Start a new game
                            return True
                            """The collidepoint() method will return True if the (x, y) coordinates we pass it are inside of the newGameRect rectangle. If so, then we make this playGame() function return True, causing a new game to start."""
                        elif hintsRect.collidepoint( (mousex, mousey) ):
                            # Toggle hints mode
                            showHints = not showHints
                            """If the mouse click was inside the "Hints" text, then we set "showHints" to "not showHints". This is an easy way to toggle a boolean value. If showHints is True, it will be set to False. And if showHints was False, then it will be set to True."""

                        move = getSpaceClicked(mousex, mousey)
                        """The getSpaceClicked button will return a tuple of two integers representing the x and y coordinates on the board of the space that was clicked on. If not space was clicked on (for example, if a point off of the board was clicked) then getSpaceClicked() will return None."""
                        if move != None and not isValidMove(mainBoard, playerTile, move[0], move[1]):
                            move = None
                            """If a space was clicked on, but it was not a valid move for the player to make, then we set the move variable back to None and wait for the player to click on the board again.

                            The reason we check for move not being equal to None is that if we try to evaluate move[0] or move[1], Python will produce an error because None[0] and None[1] are not valid expressions. (The None value is not a list.) But if move != None evaluates to False first, then the other part of the expression isn't even evaluated at all since it doesn't matter if it is True or False, the "and" keyword makes the entire expression False since the first half is False. This is called short-circuit evaluation.

                            More info on short-circuit evaluaton can be found here: http://inventwithpython.com/chapter10.html#ShortCircuitEvaluation"""

                # Draw the game board.
                drawBoard(boardToDraw)
                drawInfo(boardToDraw, playerTile, computerTile, turn)

                # Draw the "New Game" and "Hints" buttons.
                MAINSURF.blit(newGameSurf, newGameRect)
                MAINSURF.blit(hintsSurf, hintsRect)

                """While we are waiting for the player to click on a space, we will draw the board and the game information to the MAINSURF surface, and then blit (that is, draw) the "New Game" and "Hints" buttons to MAINSURF as well."""

                MAINCLOCK.tick(FPS)
                pygame.display.update()
                """A call to pygame.display.update() causes any drawing functions done to the MAINSURF pygame.Surface object to be drawn to the screen. Unlike other pygame.Surface object, the object stored in MAINSURF was the one returned by the pygame.display.set_mode() call, which is why it is the Surface object that is drawn to the screen when pygame.display.update() is called.

                The call to MAINCLOCK.tick(FPS) will introduce a pause to the game so that the program doesn't run faster than 10 frames per second. (10 is the value we stored inside the FPS constant.) This is so that our program doesn't run too fast on very powerful computer."""

            # Make the move and end the turn.
            makeMove(mainBoard, playerTile, move[0], move[1])
            if getValidMoves(mainBoard, computerTile) == []:
                # No possible moves for the computer to make, so end the game.
                break
            else:
                turn = 'computer'

        else:
            # Computer's turn.

            """The computer's turn will be similar to the code for the player's turn. We will always use the regular board data structure, not the one with the hints added on to it (even if hints mode is enabled.) But we will still draw the board, game info, and "New Game" and "Hints" buttons on the screen."""

            # Draw the board.
            drawBoard(mainBoard)
            drawInfo(mainBoard, playerTile, computerTile, turn)

            # Draw the "New Game" and "Hints" buttons.
            MAINSURF.blit(newGameSurf, newGameRect)
            MAINSURF.blit(hintsSurf, hintsRect)

            # Pause the game for bit to give the illusion that the computer is thinking.
            pauseUntil = time.time() + random.randint(5, 15) * 0.1
            while time.time() < pauseUntil:
                pygame.display.update()
            """Normally the getComputerMove() function runs very quickly; it only takes a few milliseconds on modern computers. This can make the computer's turn seem to go unreasonably fast. To counter this, we will add a short pause of a random length (between 0.5 and 1.5 seconds). First, we take the current time by calling time.time(). (The exact value is a floating point number representing the number of seconds since January 1st, 1970 (also known as the UNIX epoch).) Then we add random.randint(5, 15) * 0.1 to this number and store it in pauseUntil.

            random.randint(5, 15) will return a random number between 5 and 15, and then we multiply this by 0.1 to produce a number randomly between 0.5 and 1.5.

            Then we enter a while loop which will keep looping until the current time (that is, the value returned by time.time()) becomes greater than the value stored in pauseUntil. While we loop, we keep updating the screen with calls to pygame.display.update().
            """

            # Make the move and end the turn.
            x, y = getComputerMove(mainBoard, computerTile)
            makeMove(mainBoard, computerTile, x, y)
            """All the complicated code for determining the best move for the computer to make happens inside the getComputerMove() function. But for right here, all we have to do is call the function and then make the move on the data board structure."""

            if getValidMoves(mainBoard, playerTile) == []:
                # No possible moves for the human player to make, so end the game.
                break
            else:
                turn = 'player'

    """At this point, we have broken out of the while loop above with a break statement. (The above while loop's condition is simply True, which means the condition will never evaluate to False so the only way to get out of it is with a break statement.) Now we want to get a final score and tell the player if they won, lost, or it was a draw."""

    # Display the final score.
    drawBoard(mainBoard)
    scores = getScoreOfBoard(mainBoard)

    # Determine the text of the message to display.
    if scores[playerTile] > scores[computerTile]:
        text = 'You beat the computer by %s points! Congratulations!' % \
               (scores[playerTile] - scores[computerTile])
    elif scores[playerTile] < scores[computerTile]:
        text = 'You lost. The computer beat you by %s points.' % \
               (scores[computerTile] - scores[playerTile])
    else:
        text = 'The game was a tie!'

    """The text variable will contain the string we display on the window to the player. Notice that we not only tell the player if they won or lost, but also by how many points."""

    textSurf = FONT.render(text, True, TEXTCOLOR, BGCOLOR)
    textRect = textSurf.get_rect()
    textRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))
    MAINSURF.blit(textSurf, textRect)

    # Display the "Play again?" text with Yes and No buttons.
    text2Surf = BIGFONT.render('Play again?', True, TEXTCOLOR, BGCOLOR)
    text2Rect = text2Surf.get_rect()
    text2Rect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) + 50)

    # Make "Yes" button.
    yesSurf = BIGFONT.render('Yes', True, TEXTCOLOR, BGCOLOR)
    yesRect = yesSurf.get_rect()
    yesRect.center = (int(WINDOWWIDTH / 2) - 60, int(WINDOWHEIGHT / 2) + 90)

    # Make "No" button.
    noSurf = BIGFONT.render('No', True, TEXTCOLOR, BGCOLOR)
    noRect = noSurf.get_rect()
    noRect.center = (int(WINDOWWIDTH / 2) + 60, int(WINDOWHEIGHT / 2) + 90)

    """All the code above is similar to how we created the pygame.Surface and pygame.Rect objects for the "New Game" and "Hints" buttons. First we call the render() method to create the Surface object, then we call the get_rect() method to create the Rect object, and then we modify the Rect object to set the position of the text. Remember that this just sets up the text to be displayed on the screen, but it won't show up on the screen until we blit the Surface objects to MAINSURF and call pygame.display.update().

    We will want Surface and Rect objects for four pieces of text: Telling the player if the won, asking if they want to play again, and yes and no buttons for the user to click on."""

    while True:
        # Process events until the user clicks on Yes or No.
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if yesRect.collidepoint( (mousex, mousey) ):
                    return True
                elif noRect.collidepoint( (mousex, mousey) ):
                    return False
                """This code is very similar to the code used to detect if the player clicked on the "New Game" and "Hints" buttons, except now we are checking the player clicked on the Yes or No buttons. We will return from this function with a True or False value depending on what the player clicked, which will move program execution back to the main() function (which is the only place in our program where playGame() is called from.)"""
        MAINSURF.blit(textSurf, textRect)
        MAINSURF.blit(text2Surf, text2Rect)
        MAINSURF.blit(yesSurf, yesRect)
        MAINSURF.blit(noSurf, noRect)
        pygame.display.update()
        MAINCLOCK.tick(FPS)
        """While waiting for the player to click on a button, each time we loop through the while loop we will redraw the text and buttons to MAINSURF by calling the blit() function and then calling pygame.display.update()."""


def drawBoard(board):
    # Draw background of board.

    """There are four steps to drawing the board:"""
    MAINSURF.fill(BGCOLOR)
    pygame.draw.rect(MAINSURF, BOARDBGCOLOR, (XMARGIN, YMARGIN, BOARDWIDTH * SPACESIZE, BOARDHEIGHT * SPACESIZE))
    """First, we fill the entire window (that is, the MAINSURF Surface object) with the background color to paint over everything that was there before. Then we draw the background of the board over this."""

    # Draw grid lines of the board.
    for x in range(BOARDWIDTH + 1):
        # Draw the horizontal lines.
        startx = (x * SPACESIZE) + XMARGIN
        starty = YMARGIN
        endx = (x * SPACESIZE) + XMARGIN
        endy = YMARGIN + (BOARDHEIGHT * SPACESIZE)
        pygame.draw.line(MAINSURF, GRIDLINECOLOR, (startx, starty), (endx, endy))
    for y in range(BOARDHEIGHT + 1):
        # Draw the vertical lines.
        startx = XMARGIN
        starty = (y * SPACESIZE) + YMARGIN
        endx = XMARGIN + (BOARDWIDTH * SPACESIZE)
        endy = (y * SPACESIZE) + YMARGIN
        pygame.draw.line(MAINSURF, GRIDLINECOLOR, (startx, starty), (endx, endy))
    """Second, the above code will draw the lines on the board that mark off the spaces. BOARDWIDTH contains the number of spaces on the board. We will need BOARDWIDTH + 1 vertical lines drawn on the board, for the same reason we need to 3 vertical lines for this example board that is 2 spaces wide:

    |---|---|---|
    |   |   |   |
    |   |   |   |
    |---|---|---|

    For each horizontal (and then vertical) line we draw, we need to calculate the x and y coordinates of the starting point and the ending point of the line. Finally, we call pygame.draw.line() to draw the line onto the MAINSURF Surface.
    """

    # Draw the black & white tiles or hint spots.
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            """Third, we want to loop through each of the spaces on the board and see if there is an 'X' or 'O' string in its corresponding space in the board data structure. If so, we want to draw a tile on that space on the screen."""
            centerx = XMARGIN + x * SPACESIZE + int(SPACESIZE / 2)
            centery = YMARGIN + y * SPACESIZE + int(SPACESIZE / 2)
            if board[x][y] == 'X' or board[x][y] == 'O':
                if board[x][y] == 'X':
                    tileColor = XPLAYERCOLOR
                else:
                    tileColor = OPLAYERCOLOR
                pygame.draw.circle(MAINSURF, tileColor, (centerx, centery), int(SPACESIZE / 2) - 4)
            if board[x][y] == '.':
                pygame.draw.rect(MAINSURF, HINTCOLOR, (centerx - 4, centery - 4, 8, 8))
            """Fourth and finally, if there is a '.' string in the board data structure for this space, we want to draw a small brown square on the MAINSURF surface to inform the player that this is a possible move they can make. The '.' mark is put into the board data structure that was passed to drawBoard() in the playGame() function."""


def getSpaceClicked(mousex, mousey):
    # Return a list with two integers [x, y] of the board space coordinates where
    # the mouse was clicked. Or returns None if the mouse click is not in any space.
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if mousex > x * SPACESIZE + XMARGIN and \
               mousex < (x + 1) * SPACESIZE + XMARGIN and \
               mousey > y * SPACESIZE + YMARGIN and \
               mousey < (y + 1) * SPACESIZE + YMARGIN:
                return [x, y]
            """We loop through every space on the board, and if the x and y coordinates stored in mousex and mousey are inside a space, we return the x and y coordinates of that space on the board. Note that mousex and mousey use pixel coordinates of the window (ranging from 0 to WINDOWWIDTH and 0 to WINDOWHEIGHT), whereas the coordinate system used for the return value is the board (ranging from 0 to BOARDWIDTH and 0 to BOARDHEIGHT)."""
    return None


def drawInfo(board, playerTile, computerTile, turn):
        # Draws the game info at the bottom of the screen (scores and whose turn it is)
        scores = getScoreOfBoard(board)
        scoreSurf = FONT.render("Player Score: %s    Computer Score: %s    %s's Turn" % (str(scores[playerTile]), str(scores[computerTile]), turn.title()), True, TEXTCOLOR)
        scoreRect = scoreSurf.get_rect()
        scoreRect.bottomleft = (10, WINDOWHEIGHT - 5)
        MAINSURF.blit(scoreSurf, scoreRect)


def resetBoard(board):
    # Blanks out the board it is passed, except for the original starting position.
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            board[x][y] = ' '

    # Starting pieces:
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'
    """Remember that the game starts with a board that is not blank, but rather has two white and two black tiles positioned at the center."""


def getNewBoard():
    # Creates a brand new, blank board data structure.
    board = []
    for i in range(BOARDWIDTH):
        board.append([' '] * BOARDHEIGHT)

    return board


def isValidMove(board, tile, xstart, ystart):
    """This function is the exact same as it was in the text-based version, reversi.py. A description of how this function works can be found in the "Invent Your Own Computer Games with Python" book which features that program. The section that explains this function can be found here: http://inventwithpython.com/chapter15.html#CheckingifaMoveisValid """

    # Returns False if the player's move on space xstart, ystart is invalid.
    # If it is a valid move, returns a list of spaces that would become the player's if they made a move here.
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False

    board[xstart][ystart] = tile # temporarily set the tile on the board.

    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection # first step in the direction
        y += ydirection # first step in the direction
        if isOnBoard(x, y) and board[x][y] == otherTile:
            # There is a piece belonging to the other player next to our piece.
            x += xdirection
            y += ydirection
            if not isOnBoard(x, y):
                continue
            while board[x][y] == otherTile:
                x += xdirection
                y += ydirection
                if not isOnBoard(x, y): # break out of while loop, then continue in for loop
                    break
            if not isOnBoard(x, y):
                continue
            if board[x][y] == tile:
                # There are pieces to flip over. Go in the reverse direction until we reach the original space, noting all the tiles along the way.
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])

    board[xstart][ystart] = ' ' # restore the empty space
    if len(tilesToFlip) == 0: # If no tiles were flipped, this is not a valid move.
        return False
    return tilesToFlip


"""The isOnBoard(), getBoardWithValidMoves(), getValidMoves() and getScoreOfBoard() functions are also described in "Invent with Python" in Chapter 15: http://inventwithpython.com/chapter15.html """


def isOnBoard(x, y):
    # Returns True if the coordinates are located on the board.
    return x >= 0 and x < BOARDWIDTH and y >= 0 and y < BOARDHEIGHT


def getBoardWithValidMoves(board, tile):
    # Returns a new board with . marking the valid moves the given player can make.
    dupeBoard = getBoardCopy(board)

    for x, y in getValidMoves(dupeBoard, tile):
        dupeBoard[x][y] = '.'
    return dupeBoard


def getValidMoves(board, tile):
    # Returns a list of [x,y] lists of valid moves for the given player on the given board.
    validMoves = []

    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves


def getScoreOfBoard(board):
    # Determine the score by counting the tiles. Returns a dictionary with keys 'X' and 'O'.
    xscore = 0
    oscore = 0
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X':xscore, 'O':oscore}


def enterPlayerTile():
    # Draws the text and handles the mouse click events for letting the player
    # choose which color they want to be.
    # Returns ['X', 'O'] if the player chooses to be White, ['O', 'X'] if Black.

    # Create the text.
    textSurf = FONT.render('Do you want to be X or O?', True, TEXTCOLOR, BGCOLOR)
    textRect = textSurf.get_rect()
    textRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))

    xSurf = BIGFONT.render('White', True, TEXTCOLOR, BGCOLOR)
    xRect = xSurf.get_rect()
    xRect.center = (int(WINDOWWIDTH / 2) - 60, int(WINDOWHEIGHT / 2) + 40)

    oSurf = BIGFONT.render('Black', True, TEXTCOLOR, BGCOLOR)
    oRect = oSurf.get_rect()
    oRect.center = (int(WINDOWWIDTH / 2) + 60, int(WINDOWHEIGHT / 2) + 40)

    """Like the code that creates Surface and Rect objects for text in playGame(), we create some objects to ask the player what which color they want to be and offer two buttons to select between black and white."""

    while True:
        # Keep looping until the player has clicked on a color.
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if xRect.collidepoint( (mousex, mousey) ):
                    return ['X', 'O']
                elif oRect.collidepoint( (mousex, mousey) ):
                    return ['O', 'X']

        # Draw the screen.
        MAINSURF.blit(textSurf, textRect)
        MAINSURF.blit(xSurf, xRect)
        MAINSURF.blit(oSurf, oRect)
        pygame.display.update()
        MAINCLOCK.tick(FPS)

        """This code is also similar to the event loop in playGame(), and works the same way."""

    return random.choice([['X', 'O'], ['O', 'X']])

"""The rest of these functions are also described in "Invent with Python" in chapter 15: http://inventwithpython.com/chapter15.html """

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def makeMove(board, tile, xstart, ystart):
    # Place the tile on the board at xstart, ystart, and flip any of the opponent's pieces.
    # Returns False if this is an invalid move, True if it is valid.
    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False

    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True


def getBoardCopy(board):
    # Make a duplicate of the board list and return the duplicate.
    dupeBoard = getNewBoard()

    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            dupeBoard[x][y] = board[x][y]

    return dupeBoard


def isOnCorner(x, y):
    # Returns True if the position is in one of the four corners.
    return (x == 0 and y == 0) or \
           (x == BOARDWIDTH and y == 0) or \
           (x == 0 and y == BOARDHEIGHT) or \
           (x == BOARDWIDTH and y == BOARDHEIGHT)


def getComputerMove(board, computerTile):
    # Given a board and the computer's tile, determine where to
    # move and return that move as a [x, y] list.
    possibleMoves = getValidMoves(board, computerTile)

    # randomize the order of the possible moves
    random.shuffle(possibleMoves)

    # always go for a corner if available.
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]

    # Go through all the possible moves and remember the best scoring move
    bestScore = -1
    for x, y in possibleMoves:
        dupeBoard = getBoardCopy(board)
        makeMove(dupeBoard, computerTile, x, y)
        score = getScoreOfBoard(dupeBoard)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove


def terminate():
    pygame.quit()
    sys.exit()
    """In order to terminate the program, we must call both pygame.quit() (to shut down the Pygame engine) and sys.exit() (to shut down the program.) Calling sys.exit() without calling pygame.quit() first probably won't harm anything, though it does give IDLE some problems if the user runs this program from it. It's just considered a graceful way to shut down the Pygame library."""


if __name__ == '__main__':
    main()
    """This if statement is actually the first line of code that is run in our program (aside from the import statements and the constant variable assignments. __name__ is a special variable that is created for all Python programs implicitly. The value stored in this variable is the string '__main__', but only when the script is run by itself. If this script is imported by another script's import statement, then the value of __name__ will be the name of the file (if this script still has the name tetromino.py, then the __name__ variable will contain 'tetromino').

    This is really handy if we ever want to use the functions that are in this program in another program. By having this if statement here, which then runs the main() function, we could have another program use "import tetromino" and make use of any of the functions we've already written. Or if you want to test individual functions by calling them from the interactive shell, you could call them without running the game program. This trick is really handy for code reuse."""