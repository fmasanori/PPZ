import pygame.mixer
sounds = pygame.mixer
sounds.init()
def espera_tocar(canal):
    while canal.get_busy():
        pass
certos = 0
errados = 0
opção = int(input ("Aperte 1)Certo 2)Errado e 0)Finalizar "))
while opção != 0:
    if opção == 1:
        s = sounds.Sound("correct.wav")
        espera_tocar(s.play())
        certos = certos + 1
    if opção == 2:    
        s2 = sounds.Sound("wrong.wav")
        espera_tocar(s2.play())
        errados = errados + 1
    opção = int(input ("Aperte 1)Certo 2)Errado e 0)Finalizar "))

print ("Certos:", certos, "Errados:", errados)

