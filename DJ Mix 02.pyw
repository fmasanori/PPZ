from tkinter import *
import pygame.mixer
app = Tk()
app.title('DJ Mix')
app.geometry('250x100+200+100')
som = '50459_M_RED_Nephlimizer.wav'
mixer = pygame.mixer
mixer.init()
def start():
    track.play(loops = -1)
def stop():
    track.stop()
def termina():
    track.stop()
    app.destroy()
track = mixer.Sound(som)
start_botão = Button(app, command = start, text = 'Start')
start_botão.pack(side = LEFT)
stop_botão = Button(app, command = stop, text = 'Stop')
stop_botão.pack(side = RIGHT)
app.protocol('WM_DELETE_WINDOW', termina)
app.mainloop()
