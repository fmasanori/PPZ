from tkinter import *
app = Tk()
app.title("Show de calouros")
app.geometry('300x100+200+100')

b1 = Button(app, text = "Certo!", width = 10)
b1.pack(side = "left", padx = 10, pady = 10)

b2 = Button(app, text = "Errado!", width = 10)
b2.pack (side = "right", padx = 10, pady = 10)

app.mainloop()        


