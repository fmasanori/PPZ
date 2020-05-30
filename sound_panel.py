from tkinter import *
import pygame.mixer
class SoundPanel(Frame):
    def muda(self):
        if self.tocando.get():
            self.track.play(loops = -1)
        else:
            self.track.stop()
    def muda_volume(self, v):
        self.track.set_volume(self.volume.get())
    def __init__(self, app, mixer, sound_file):
        Frame.__init__(self, app)
        self.track = mixer.Sound(sound_file)
        self.tocando = IntVar()
        tocar = Checkbutton(self, variable = self.tocando,
                            command = self.muda,
                            text = sound_file)
        tocar.pack(side = LEFT)
        self.volume = DoubleVar()
        self.volume.set(self.track.get_volume())
        escala = Scale(self, variable = self.volume,
            from_ = 0.0, to = 1.0, resolution = 0.1,
            command = self.muda_volume,
            label = 'Volume', orient = HORIZONTAL)
        escala.pack(side = RIGHT)

