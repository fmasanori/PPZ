# Ink Spill (Flood It Clone)
# http://inventwithpython.com/blog
# By Al Sweigart al@inventwithpython.com

"""
Welcome to the Code Comments for Ink Spill. Code Comments is a series of simple games with detailed comments in the source code, so you can see how the game works.

The text in between the triple-double-quotes are comments. The Python interpreter ignores any text in between them, so we can add any comments about the source code without affecting the program. In general for Code Comments, the comments will describe the lines of code above the comment. It helps to view this file either on the Code Comments site or with a text editor that does "syntax highlighting", so that the comments appear in a separate color and are easier to distinguish from the code.

This Code Comments assumes you know some basic Python programming. If you are a beginner and would like to learn computer programming, there is a free book online called "Invent Your Own Computer Games with Python" at http://inventwithpython.com

The Code Comments programs make references to sections of this book throughout the program. This Code Comments can also teach you how to use the Pygame library to make your own games with graphics, animation, and sound. You can download Pygame from http://pygame.org and view its documentation at http://pygame.org/docs/

HOW TO PLAY INK SPILL:
Click on the colored palettes at the bottom to change the color of the top left box. Any boxes connected to this box with the same color will also have their color changed. The goal of the game is to turn the entire board to a single color before running out of turns.
"""

import random
import time
import sys
import pygame
from pygame.locals import *
"""Here we import modules that our game needs. random has random number functions, time has the sleep() function, sys has the exit() function, and pygame contains all the pygame-related functions.

pygame.locals contains constants like MOUSEMOTION and MOUSEBUTTONUP and QUIT for the events. It's easier to type MOUSEBUTTONUP instead of pygame.locals.MOUSEBUTTONUP, so we use the "from pygame.locals import *" format to import these to the local namespace.
"""

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BOXSIZE = 20
PALETTEGAPSIZE = 10
PALETTESIZE = 45
MAXLIFE = 30
COLS = 17
ROWS = 17
"""These constant variables (the uppercase names means we shouldn't change the values stored in them) set some standard values for our game. You can play around with different values for them (though some values might cause bugs in the game.) By using constants instead of the values directly, it is easier to make changes since we only have to change them in one place.

For example, if we used 32 instead of MAXLIFE, then if we wanted to change our code later we'd have to change every place in the code we find 32. This is trickier than just changing the one line where MAXLIFE is originally set.

More information about constants is at http://inventwithpython.com/chapter9.html#ConstantVariables
"""

WHITE = (255, 255, 255)
DARKGRAY = (70, 70, 70)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
"""We also set up some constant values for different colors. Pygame uses tuples of three integers to represent color. The integers represent the amount of red, green, and blue in the color (this is commonly called a RGB). 0 means there is none of the primary color in the color, and 255 means there is the maximum amount. So (255, 0, 0) is red, since it has the maximum amount of red but no green or blue. But (255, 0, 255) adds the max amount of blue with the red, creating purple.

More information about colors is at http://inventwithpython.com/chapter17.html#ColorsinPygame
"""

COLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE)
BGCOLOR = DARKGRAY

def main():
    global MAINCLOCK, MAINSURF
    """The main() function is where our program begins. (See the last two lines of code to see why.) Because we define MAINCLOCK and MAINSURF inside this function, these are local variables to the main() function and the names MAINCLOCK and MAINSURF won't exist outside of this function. By using a global statement, we can tell Python that we want these variables to be global variables.

    More information about global and local variables is at http://inventwithpython.com/chapter6.html#VariableScope
    """

    pygame.init()
    MAINCLOCK = pygame.time.Clock()
    MAINSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    """pygame.init() needs to be called before any of the other Pygame functions.

    pygame.time.Clock() returns a pygame.Clock object. We will use this object's tick() method to ensure that the program runs at no faster than 30 frames per second (or whatever integer value we have in the FPS constant.)

    pygame.display.set_mode() creates the window on the screen and returns a pygame.Surface object. Any drawing done on this Surface object with the pygame.draw.* functions will be displayed on the screen when we call pygame.display.update().

    More information about pygame.display.set_mode() is at http://inventwithpython.com/chapter17.html#ThepygamedisplaysetmodeandpygamedisplaysetcaptionFunctions"""

    pygame.display.set_caption('Ink Spill')
    mousex = 0
    mousey = 0
    mainBoard = generateRandomBoard(COLS, ROWS, 100)
    life = MAXLIFE
    lastPaletteClicked = None
    """Here are some basic start-of-the-game settings we want to make. First we set the text of the window's caption. mousex and mousey will store the latest coordinates of the mouse cursor.

    mainBoard will contain the board data structure of what each box's color is. It is a list of list of integers, so mainBoard[0][0] contains an integer for the color of the topmost leftmost box. If this integer is, say, 2, then the color corresponds to COLORS[2] (which we have set up to be BLUE.) mainBoard[1][0] is the box to the right of mainBoard[0][0] and mainBoard[0][1] is the box below mainBoard[0][0].

    generateRandomBoard() will return a board with randomly colored boxes, which is how the game starts off. We pass 100 for the third parameter to make the board slightly easier to solve then a completely random board. (See the generateRandomBoard() function for how we do this exactly.)

    life stores how many turns left the player has. lastPaletteClicked stores the last move the player made, so they don't accidentally waste a turn by clicking the same palette twice in a row."""

    # Main game loop:
    while True:
        paletteClicked = None
        """This is the main game loop, which constantly loops while the program is playing. In this loop, we display the board on the screen and also handle any input events from the player. paletteClicked will store an integer of the last palette that was clicked on (0 for the color stored in COLORS[0], 1 for the color stored in COLORS[1], etc.) We reset the value to None each time the game loop loops."""

        # Draw the screen.
        MAINSURF.fill(BGCOLOR)
        drawBoard(mainBoard)
        drawLifeMeter(life)
        drawPalettes()
        """We have three functions that draw the various things to the screen. drawBoard() draws the boxes, drawLifeMeter() draws the red boxes on the left side that show how many turns left the player has, and drawPalettes() draws the palette buttons at the bottom. Note that nothing will actually appear on the screen until pygame.display.update() is called.

        The MAINSURF.fill() call simply paints the entire screen with the background color, to erase any previous drawings made."""

        # Handle any events.
        for event in pygame.event.get():
            """The pygame.event.get() function returns a list of pygame.Event objects of events that have happened since the last call to pygame.event.get(). This loop uses the same code to handle each event in this list."""
            if event.type == QUIT:
                """The QUIT event is created when the user tries to shut down the program by clicking the X in the top right corner, or by killing the program from the task manager or some other means."""
                pygame.quit()
                sys.exit()
                """In order to terminate the program, we must call both pygame.quit() (to shut down the Pygame engine) and sys.exit() (to shut down the program.)"""

            if event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                """A MOUSEMOTION event is created whenever the user moves the mouse over the window. The Event object created has a pos attribute that is a tuple of the two xy integer coordinates for where the mouse is located. We will save these values off to mousex and mousey."""
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                paletteClicked = getClickedPalette(mousex, mousey)
                """When the MOUSEBUTTONUP is created, we check if the mouse is currently over one of the color palettes (otherwise we can ignore it.) The bulk of this is implemented inside our getClickedPalette() function. This function returns None if the mouse wasn't over a palette, or it returns an integer of the palette number."""

        if paletteClicked != None and paletteClicked != lastPaletteClicked:
            lastPaletteClicked = paletteClicked
            """If the mouse was clicked over a palette in this iteration of the game loop, then paletteClicked will not be None. To keep the player from accidentally wasting a turn by clicking the same palette twice, we also make sure that the paletteClicked does not equal lastPaletteClicked. lastPaletteClicked originally has a value of None (meaning no palette was clicked) but we store the currently clicked palette number here for future reference."""
            floodAnimation(mainBoard, paletteClicked)
            """floodAnimation() causes the fade effect that happens after the player clicks a palette."""
            life -= 1
            """We decrease the value in life by one, meaning the player has used up a turn."""

            resetGame = False
            if hasWon(mainBoard):
                for i in range(4):
                    flashBorderAnimation(WHITE, mainBoard)
                resetGame = True
                """If the hasWon() function returns True, then the entire board is one color and the player has won. We flash the board white four times, and then set resetGame to True so that the code later on will know to start a new game."""
            elif life == 0:
                """If life is at 0, then the player has run out of turns. Note that this code needs to come AFTER the hasWon() check, otherwise if the player used their last turn to make a winning move, the code would notice that life is at zero before it noticed that the player won the game."""
                drawLifeMeter(0)
                pygame.display.update()
                time.sleep(0.4)
                """We draw the empty life meter to the screen so the player can see that it is now empty."""
                for i in range(4):
                    flashBorderAnimation(BLACK, mainBoard)
                resetGame = True

            if resetGame:
                """A new game can start if the player wins or loses the last game. Either way, resetGame is set to True, so we know that we should reset the values in mainBoard, life, and lastPalette so that on the next iteration through the loop a new game begins. We add the sleep() call to have a slight pause before the next game starts."""
                time.sleep(2)
                mainBoard = generateRandomBoard(COLS, ROWS, 100)
                life = MAXLIFE
                lastPaletteClicked = None

        pygame.display.update()
        MAINCLOCK.tick(FPS)
        """A call to pygame.display.update() causes any drawing functions done to the MAINSURF pygame.Surface object to be drawn to the screen. Unlike other pygame.Surface object, the object stored in MAINSURF was the one returned by the pygame.display.set_mode() call, which is why it is the Surface object that is drawn to the screen when pygame.display.update() is called.

        The call to MAINCLOCK.tick(FPS) will introduce a pause to the game so that the program doesn't run faster than 30 frames per second. (30 is the value we stored inside the FPS constant.) This is so that our program doesn't run too fast on very powerful computer."""

def hasWon(board):
    """To determine if the player won, we look at the board data structure and see if every box represented by it is the same color. To do this, we grab the color of the box in the topleft corner (which is stored in board[0][0]) and loop through all the other items in board to see if they are the same. The first time we find a different color box, we return False. If we make it through the loops without finding a differently colored box, we return True."""
    color = board[0][0]
    for x in range(COLS):
        for y in range(ROWS):
            if board[x][y] != color:
                return False
    return True

def flashBorderAnimation(color, board, animationSpeed=30):
    """To achive the "flashing border" effect of a certain color, we are going to draw the board as it is, then on top of that draw a solidly colored surface (of increasing transparency), and then just the board on top of that. The effect will be that it appears that everything except the board flashes."""

    origSurf = MAINSURF.copy()
    """First we save off what the board currently looks like to a variable called origSurf. This will be what the MAINSURF surface originally looked like. All pygame.Surface objects (including the one stored in MAINSURF) have a copy() method that returns another pygame.Surface object that is a copy of itself."""
    flashSurf = pygame.Surface(MAINSURF.get_size())
    """Next we create a new pygame.Surface object by calling the pygame.Surface() constructor function. This constructor requires a tuple with two integer values for the width and height of the surface. Since we want the surface to have the same width and height as the MAINSURF surface, we call the get_size() method which returns just such a tuple."""
    flashSurf = flashSurf.convert_alpha()
    """Anytime we want to drawn "transparent pixels" to a pygame.Surface object, we need to first call the convert_alpha() method on that surface."""
    for start, end, step in ((0, 256, 1), (255, 0, -1)):
        """This for loop will only have two iterations. On the first iteration, start and end and step will have the values 0, 255, and 1 respectively. Then they will have the values 255, 0, and -1 on the second iteration.

        The start, end, and step variables will be used in the inner for loop, so that the for loop first loops from 0 up to (but not including) 256 (increasing at each step by 1) and then from 255 down to (but not including) 0 (decreasing at each step by -1). This value will be used for the transparency of the "flash" surface."""
        for transparency in range(start, end, animationSpeed * step):
            MAINSURF.blit(origSurf, (0, 0))
            """First we want to redraw the MAINSURF surface with the image it originally was."""
            r, g, b = color
            flashSurf.fill((r, g, b, transparency))
            MAINSURF.blit(flashSurf, (0, 0))
            """Second, we want to draw a solid (but somewhat transparent) color over the old image. We use Python's multiple assignment trick to assign the three integers in the color tuple to the variables r, g, and b. We can then use these three variables and the transparency variable to create a Pygame color data structure that has transparency. (Pygame's transparent colors have a fourth value in addition to red, green, and blue. The fourth value (called the alpha value) specifies how opaque the color is. 0 is completely transparent and 255 is completely opaque."""
            drawBoard(board)
            """Third, we draw just the board on top of the transparent layer so that it is not affected by the transparent color."""
            pygame.display.update()
            MAINCLOCK.tick(FPS)
            """We need to call pygame.display.update() in order to display the MAINSURF surface on the screen."""
    MAINSURF.blit(origSurf, (0, 0))
    """After doing the flash animation, we redraw the original surface back to MAINSURF."""

def getBoardCopy(board):
    """Our floodAnimation() function will require a duplicate copy of the board data structure. We cannot simply have an assignment statement like dupe = board since this will copy a reference to the board data structure instead of copying the board data itself.

    Remember that the board data structure is really just a list of list of integers. More information about lists of lists is at http://inventwithpython.com/chapter13.html#CreatingaNewGameBoard

    More information about list references is at http://inventwithpython.com/chapter10.html#ListReferences """
    dupe = []
    """The dupe variable will store our duplicate copy of the game board data structure."""
    for x in range(COLS):
        column = []
        """The column variable will be the copy of the list within the list in the board data structure."""
        for y in range(ROWS):
            column.append(board[x][y])
        dupe.append(column)
        """After we have gone through the entire column, add the column to the dupe list."""
    return dupe

def floodAnimation(board, paletteClicked, animationSpeed=25):
    origBoard = getBoardCopy(board)
    """First we want to save the game board data structure as it originally was before we made the move. This is because our animation will draw the original surface with the surface of how the board looks after making the move on top of it, with some transparency. The end effect is that we gradually fade into how the board looks after the new move."""

    flood(board, board[0][0], paletteClicked, 0, 0)
    """flood() is the function that changes the game board data structure in accordance with the rules of the game. See the flood() function itself for a more detailed description."""

    for transparency in range(0, 255, animationSpeed):
        drawBoard(origBoard)
        drawBoard(board, transparency)
        """After calling flood(), the board variable stores what the board looks like after the move. The origBoard variables stores a board data structure of the state the board was in before we made the move. By calling drawBoard() with origBoard first, we draw the original board to the MAINSURF surface, and then we call drawBoard() passing board and transparency to draw how the board looks after the move was made. On each iteration of the loop, the value in transparency increases by the integer in animationSpeed. This makes the new move board slowly fade in over the old board.

        The larger the value in animationSpeed, the quicker the new move board becomes completely opaque."""
        pygame.display.update()
        MAINCLOCK.tick(FPS)

def generateRandomBoard(width, height, easy=0):
    """Notice that the first part of the code in generateRandomBoard() is very similar to getBoardCopy(). This is because both functions create a game board data structure. However, in generateRandomBoard(), we assign a random color to each box, instead of copying the color from some other game board data structure."""
    board = []
    for x in range(width):
        column = []
        for y in range(height):
            column.append(random.randint(0, len(COLORS) - 1))
        board.append(column)

    # Make the board easier by setting some boxes to be the same color as their neighbor.
    """We can make this game a little bit easier by adding larger areas of similar colors. We can do this by randomly selecting a box (except for one on the edge of the board) and changing two of its neighbors to be the same color. If we keep doing this enough, then there will be patches of same-colored boxes on the board, which can give the player a stradegy to work with in trying to solve the game.

    The more we do this, the easier the game becomes in general. The "easy" parameter will tell this function how often to do this to the board."""
    for i in range(easy):
        x = random.randint(1, width-2)
        y = random.randint(1, height-2)
        """By selecting only boxes that are not on the border (that is, having a x or y value that is either 0 or the width or height minus 1) we never have to worry about trying to color a nonexistant neighbor (such as board[-1][0]) which would cause our program to crash."""
        direction = random.randint(0, 3)

        if direction == 0:
            board[x-1][y] == board[x][y]
            board[x][y-1] == board[x][y]
            """Remember, with the coordinate system we use decreases going left and up, and increases going right and down. The above two lines of code will change the neighbor to the left and above the box at board[x][y]."""
        elif direction == 1:
            board[x+1][y] == board[x][y]
            board[x][y+1] == board[x][y]
        elif direction == 2:
            board[x][y-1] == board[x][y]
            board[x+1][y] == board[x][y]
        else:
            board[x][y+1] == board[x][y]
            board[x-1][y] == board[x][y]

    return board

def drawBoard(board, transparency=255):
    """The drawBoard() function draws the game board data structure it is passed to the MAINSURF surface. Optionally, the caller of this function can specify a transparency level (0 for completely transparent, 255 for completely opaque.)"""
    tempSurf = pygame.Surface(MAINSURF.get_size())
    """First we create a temporary pygame.Surface object that is the same size as the MAINSURF surface."""
    tempSurf = tempSurf.convert_alpha()
    """We will draw the game board to this temporary surface, possibly with a certain amount of transparency. Any surface that will contain transparent pixels will have to have its convert_alpha() method called first."""
    tempSurf.fill((0, 0, 0, 0))
    """Surface objects always have an opaque black color drawn on them when the object is first created. We don't want this, since the opaque black will block anything drawn under it. Instead we will draw a completely transparent black color to the surface to replace the opaque black. Note that the RGB values we use for this color don't matter, since completely transparent black looks the same as any completely transparent color. (Think of it like this: an invisible black tiger looks the same as an invisible white tiger: invisible.)"""

    for x in range(COLS):
        for y in range(ROWS):
            """We use nested for loops so that we draw each box in the board data structure."""
            left, top = leftTopOfBox(x, y)
            """We need to translate the position of the box on the board into a pixel position on the screen. This calculation will be done in leftTopOfBox(), which will return two integer values that we store in left and top variables using the multiple assignment trick."""
            r, g, b = COLORS[board[x][y]]
            pygame.draw.rect(tempSurf, (r, g, b, transparency), (left, top, BOXSIZE, BOXSIZE))
            """The pygame.draw.rect() function will draw a rectangle on our tempSurf Surface object, with a color that has the same RGB values as the box's color but a transparency value specified by the transparency parameter, and at the location we got from leftTopOfBox(). The two uses of BOXSIZE represent the width and height of the rectangle to draw, respectively."""
    MAINSURF.blit(tempSurf, (0, 0))
    """After we are done drawing the board to the temporary surface, we want to draw the contents of the temporary surface onto MAINSURF. (Remember, MAINSURF will have other things drawn on it besides the game board, such as the life meter and the clickable color palettes at the bottom.) The blit() method of a pygame.Surface object can drawn the contents of the another surface onto itself. The (0, 0) tells the blit() method to place the topleft corner of the tempSurf surface on MAINSURF at MAINSURF's (0, 0) coordinates. (You can blit surfaces onto other surfaces anywhere on that surface. In this case, we just want to completely overlap the surface so we choose (0, 0).)"""

def drawPalettes():
    """This function draws the clickable palettes onto MAINSURF. The PALETTESIZE constant determines how big the palettes will be, and the PALETTEGAPSIZE constant will indicate how many pixels of space should go in between each palette."""
    numColors = len(COLORS)
    xmargin = int((WINDOWWIDTH - ((PALETTESIZE * numColors) + (PALETTEGAPSIZE * (numColors - 1)))) / 2)
    for i in range(numColors):
        left = xmargin + (i * PALETTESIZE) + (i * PALETTEGAPSIZE)
        top = WINDOWHEIGHT - PALETTESIZE - 10
        """We want the bottom of the palettes to be 10 pixels up from the bottom of the window, hence the "- 10"."""
        pygame.draw.rect(MAINSURF, COLORS[i], (left, top, PALETTESIZE, PALETTESIZE))
        pygame.draw.rect(MAINSURF, BGCOLOR,   (left + 2, top + 2, PALETTESIZE - 4, PALETTESIZE - 4), 2)

def drawLifeMeter(currentLife):
    lifeBoxSize = int((WINDOWHEIGHT - 40) / MAXLIFE)
    """First we need to determine the size of each box. We want the size of the life meter to be WINDOWHEIGHT - 40 no matter how many life boxes there are. So we take that number and divide by the number of life boxes to get the size (in pixels) of each life box. (There may be some slight differences in the total size due to rounding down.)"""

    # Draw background of life box.
    pygame.draw.rect(MAINSURF, BGCOLOR, (20, 20, 20, 20 + (MAXLIFE * lifeBoxSize)))
    """First we draw a background rectangle to overwrite any previous life meter drawn on MAINSURF."""

    for i in range(MAXLIFE):
        if currentLife >= (MAXLIFE - i):
            pygame.draw.rect(MAINSURF, RED, (20, 20 + (i * lifeBoxSize), 20, lifeBoxSize))
            """Then we draw a red filled box for each turn the player has left."""
        pygame.draw.rect(MAINSURF, WHITE, (20, 20 + (i * lifeBoxSize), 20, lifeBoxSize), 1)
        """For every possible life box (whether it should be full or not) draw a white boundary box for it. The last parameter means that this box should not be filled in with the WHITE color, but instead just have a border with a width of 1 pixel."""

def getClickedPalette(x, y):
    numColors = len(COLORS)
    xmargin = int((WINDOWWIDTH - ((PALETTESIZE * numColors) + (PALETTEGAPSIZE * (numColors - 1)))) / 2)
    """The xmargin will tell us how many pixels are on the left side of the leftmost palette box. We have to calculate this because this value will be different for different values of PALETTESIZE, PALETTEGAPSIZE, numColors, and WINDOWWIDTH."""
    top = WINDOWHEIGHT - PALETTESIZE - 10
    for i in range(numColors):
        # Determine if the xy coordinates of the mouse click is inside any of the palettes.
        left = xmargin + (i * PALETTESIZE) + (i * PALETTEGAPSIZE)
        """The x coordinate of the left side of the palette box can be calculated from the xmargin and which number palette this is. (The palette for index 0 in COLORS is the leftmost, the palette for index 1 is on the right of that, etc.) The calculation for top does not have to be inside this for loop because the y coordinate for the top side of the palettes are the same for every palette."""
        r = pygame.Rect(left, top, PALETTESIZE, PALETTESIZE)
        """Here we create a pygame.Rect object by calling the pygame.Rect() constructor function. This Rect object will represent the area of the palette's box. (We pass PALETTESIZE for both the width and the height.)"""
        if r.collidepoint(x, y):
            return i
            """The collidepoint() method for pygame.Rect objects is a handy function to do collision detection. It will return True if the xy coordinates we pass it are within the Rect's rectangle. In that case, we should return this palette's number."""
    return None
    """If the mouse click's xy coordinates were not within any palette, then this function will return the None value."""

def flood(board, oldColorNum, newColorNum, x, y):
    """The way our game will know that the boxes are connected to the topleftmost box on the board by the same color is with this flood() function. flood() is a recursive function, meaning that it is a function that calls itself.

    The flood() function is actually quite simple: if the box it is given (by the x and y parameters) has a color that is the same as oldColorNum, then it changes that box's color to newColorNum. Furthermore, it then calls the flood() function on each of the neighboring boxes.

    So, like a zombie plague, these calls to flood() will result in more calls to flood(). And the function calls only stop when they hit the border of the board or a box that has a different color than the one specified by oldColorNum.

    More information about flood fill algorithms is at http://en.wikipedia.org/wiki/Flood_fill
    More information about recursive function calls is at http://en.wikipedia.org/wiki/Recursion_(computer_science) """
    if oldColorNum == newColorNum or board[x][y] != oldColorNum:
        return

    board[x][y] = newColorNum # change the color of the current box

    # Make the recursive call for any neighboring boxes:
    if x > 0:
        flood(board, oldColorNum, newColorNum, x - 1, y)
    if x < COLS - 1:
        flood(board, oldColorNum, newColorNum, x + 1, y)
    if y > 0:
        flood(board, oldColorNum, newColorNum, x, y - 1)
    if y < ROWS - 1:
        flood(board, oldColorNum, newColorNum, x, y + 1)

def leftTopOfBox(boxx, boxy):
    """This function determines the xy coordinates of the top left corner of a specific box in the board data structure. If boxx is 4 and boxy is 2, this would correspond to the box at board[4][2]. The x and y coordinates of the left side and top side (respectively) of the box in pixels is returned by this function."""
    # Determine size of the margins for each side.
    xmargin = int((WINDOWWIDTH - (COLS * BOXSIZE)) / 2)
    ymargin = int((WINDOWHEIGHT - (ROWS * BOXSIZE)) / 2)
    return (boxx * BOXSIZE + xmargin, boxy * BOXSIZE + ymargin)

if __name__ == '__main__':
    main()
    """This if statement is actually the first line of code that is run in our program 9aside from the import statements and the constant variable assignments. __name__ is a special variable that is created for all Python programs implicitly. The value stored in this variable is the string '__main__', but only when the script is run by itself. If this script is imported by another script's import statement, then the value of __name__ will be the name of the file (if this script still has the name inkspill.py, then the __name__ variable will contain 'inkspill').

    This is really handy if we ever want to use the functions that are in this program in another program. By having this if statement here, which then runs the main() function, we could have another program use "import inkspill" and make use of any of the functions we've already written. Or if you want to test individual functions by calling them from the interactive shell, you could call them without running the game program. This trick is really handy for code reuse."""