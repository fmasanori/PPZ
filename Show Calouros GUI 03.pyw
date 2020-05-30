from tkinter import *
app = Tk()
app.title("Show de calouros")
app.geometry('300x100+200+100')
import pygame.mixer
sounds = pygame.mixer
sounds.init()
certos = 0
errados = 0
def espera_tocar(canal):
    while canal.get_busy():
        pass
def musica_certa():
    global certos
    s = sounds.Sound("correct.wav")
    espera_tocar(s.play())
    certos = certos + 1 
def musica_errada():
    global errados
    s = sounds.Sound("wrong.wav")
    espera_tocar(s.play())
    errados = errados + 1
b1 = Button(app, text = "Certo!", width = 10, command = musica_certa)
b1.pack(side = "left", padx = 10, pady = 10)
b2 = Button(app, text = "Errado!", width = 10, command = musica_errada)
b2.pack (side = "right", padx = 10, pady = 10)
app.mainloop()        


