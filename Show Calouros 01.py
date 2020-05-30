import pygame.mixer
sounds = pygame.mixer
sounds.init()

def espera_tocar (canal):
    while canal.get_busy():
        pass

s = sounds.Sound('heartbeat.wav')
espera_tocar(s.play())
s2 = sounds.Sound('buzz.wav')
espera_tocar(s2.play())
s3 = sounds.Sound('ohno.wav')
espera_tocar(s3.play())
s4 = sounds.Sound('carhorn.wav')
espera_tocar(s4.play())

