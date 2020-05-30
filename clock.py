import tkinter
from time import strftime
#by Luciano Ramalho

relógio = tkinter.Label()

relógio.pack()
relógio['font'] = 'Helvetica 120 bold'
relógio['text'] = strftime('%H:%M:%S')

def tictac():
    agora = strftime('%H:%M:%S')
    if agora != relógio['text']:
        relógio['text'] = agora
    relógio.after(100, tictac)

tictac()
relógio.mainloop()

