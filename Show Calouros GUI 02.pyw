from tkinter import *

def apertei_botão():
    print ('Apertei o botão!')

app = Tk()
app.title("Teste de botão")
app.geometry('300x100+200+100')

b = Button(app, text = "Aperte-me!", width = 10, command = apertei_botão)
b.pack(side = "top", padx = 10, pady = 10)

app.mainloop()        


