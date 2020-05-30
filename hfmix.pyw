from tkinter import *
from sound_panel import *
import pygame.mixer
import os
app = Tk()
app.title('Head First Mix')
mixer = pygame.mixer
mixer.init()
dirList = os.listdir(".")
for fname in dirList:
   if fname.endswith('.wav') and fname[0] in '345':
   #if fname.endswith('.aif'):
   #if fname.startswith('flick3r__'):
        SoundPanel(app, mixer, fname).pack()
def termina():
    mixer.stop()
    app.destroy()
app.protocol('WM_DELETE_WINDOW', termina)
app.mainloop()
