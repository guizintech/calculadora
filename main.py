from tkinter import *

def clicar(valor):
    atual = entrada.get()
    entrada.delete(0, END)
    entrada.insert(0, str(atual) + str(valor))

def limpar():
    entrada.delete(0, END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, END)
        entrada.insert(0, "Erro")

janela = Tk()
janela.title("Calculadora")
janela.geometry("300x400")

entrada = Entry(janela, width=20, font=("Arial", 24), borderwidth=5, justify="right")
entrada.grid(row=0, column=0, columnspan=4)

botoes = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3)
]

for (texto, linha, coluna) in botoes:
    if texto == "C":
        Button(janela, text=texto, width=5, height=2,
               command=limpar).grid(row=linha, column=coluna)

    elif texto == "=":
        Button(janela, text=texto, width=5, height=2,
               command=calcular).grid(row=linha, column=coluna)

    else:
        Button(janela, text=texto, width=5, height=2,
               command=lambda t=texto: clicar(t)).grid(row=linha, column=coluna)

janela.mainloop()