from tkinter import * 
def salvar_dados():
    try:
        f = open('encomenda.txt', 'a')    
        f.write('Destino: ') 
        f.write(f'{destino.get()}\n') 
        f.write('Descrição: ') 
        f.write(f'{descrição.get()}\n')
        f.write('Endereço: ') 
        f.write(f'{endereço.get('1.0', END)}\n')
        destino.set('São José dos Campos') 
        descrição.delete(0, END) 
        endereço.delete("1.0", END)
        f.close()
    except Exception as exceção:
        messagebox.showerror('Erro!',
        'Não foi possível gravar a encomenda\n%s' %exceção)
    
def ler_destinos(arquivo): 
    destinos = [] 
    f = open(arquivo) 
    for linha in f: destinos.append(linha.rstrip()) 
    return destinos

app = Tk() 
app.title('Head-Ex Logística e Transportes') 
Label(app, text = "Destino:").pack() 
destino = StringVar() 
destino.set('São José dos Campos') 

opções = ler_destinos("cidades.txt") 
OptionMenu(app, destino, *opções).pack()

Label(app, text = "Descrição:").pack() 
descrição = Entry(app) 
descrição.pack() 
Label(app, text = "Endereço:").pack() 
endereço = Text(app) 
endereço.pack() 
Button(app, text = "Salvar", command = salvar_dados).pack() 
app.mainloop() 

