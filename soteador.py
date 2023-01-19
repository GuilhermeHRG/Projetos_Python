import random
from tkinter import*
from tkinter import Entry
from typing import List


def sortear():

    n = random.randint(int(ent_lmt1.get()), int(ent_lmt2.get()))

    texto_numero["text"] = f"NÚMERO SORTEADO: \n{n}"




janela = Tk()
#LAYOUT
janela.geometry("250x250")
janela.title("SORTEADOR")
texto_inicial = Label(janela, text="SORTEADOR ONLINE")
texto_inicial.grid(column=0, row=0, padx=10, pady=10)

#ENTRADA DE DADOS
ent_lmt1 = Entry(janela, bd=2, font=('Calibri', 15), justify=CENTER)
ent_lmt1.grid(column=0, row=1, padx=10, pady=10)



ent_lmt2 = Entry(janela, bd=2, font=('Calibri', 15), justify=CENTER)
ent_lmt2.grid(column=0, row=2, padx=10, pady=10)




Botao = Button(janela, text="SORTEAR", command=sortear)
Botao.grid(column=0, row=3, padx=10, pady=10)

texto_numero = Label(janela, text="")
texto_numero.grid(column=0, row=4, padx=10, pady=10)
janela.mainloop()
