from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from funcoes import *
from functools import partial

pincel = 'white'

def cor(): #Função aplicada ao click do botão "Gerar"
    cor_fixa = str(paleta1['background'])
    cor_fixa = 'black'
    paleta1.config(background=cor_fixa)
    paleta1.config(activebackground='black')

    paleta2.config(background=cores_aleatorias())
    active2 = str(paleta2['background'])
    paleta2.config(activebackground=active2)

    paleta3.config(background=cores_aleatorias())
    active3 = str(paleta3['background'])
    paleta3.config(activebackground=active3)

    paleta4.config(background=cores_aleatorias())
    active4 = str(paleta4['background'])
    paleta4.config(activebackground=active4)

def selecao(a,b,c,d):
    global pincel
    a.config(bd=5, relief='ridge') #

    b.config(bd=2, relief='groove')
    c.config(bd=2, relief='groove')
    d.config(bd=2, relief='groove')
    pincel = str(a['background'])
    return a,b,c,d

def reset(): #Função aplicada ao click do botão "Reset"
    paleta1.config(bd=2, relief='groove', background='white', activebackground='white')
    paleta2.config(bd=2, relief='groove', background='white', activebackground='white')
    paleta3.config(bd=2, relief='groove', background='white', activebackground='white')
    paleta4.config(bd=2, relief='groove', background='white', activebackground='white')
    quadro1.config(pady=20, padx=60,background='white', activebackground='white')
    quadro2.config(pady=20, padx=60,background='white', activebackground='white')
    quadro3.config(pady=20, padx=60,background='white', activebackground='white')
    quadro4.config(pady=20, padx=60,background='white', activebackground='white')
    quadro5.config(pady=20, padx=60,background='white', activebackground='white')
    quadro6.config(pady=20, padx=60,background='white', activebackground='white')
    quadro7.config(pady=20, padx=60,background='white', activebackground='white')
    quadro8.config(pady=20, padx=60,background='white', activebackground='white')
    quadro9.config(pady=20, padx=60,background='white', activebackground='white')
    quadro10.config(pady=20, padx=60,background='white', activebackground='white')
    quadro11.config(pady=20, padx=60,background='white', activebackground='white')
    quadro12.config(pady=20, padx=60,background='white', activebackground='white')
    quadro13.config(pady=20, padx=60,background='white', activebackground='white')
    quadro14.config(pady=20, padx=60,background='white', activebackground='white')
    quadro15.config(pady=20, padx=60,background='white', activebackground='white')
    quadro16.config(pady=20, padx=60,background='white', activebackground='white')
    quadro17.config(pady=20, padx=60,background='white', activebackground='white')
    quadro18.config(pady=20, padx=60,background='white', activebackground='white')
    quadro19.config(pady=20, padx=60,background='white', activebackground='white')
    quadro20.config(pady=20, padx=60,background='white', activebackground='white')
    quadro21.config(pady=20, padx=60,background='white', activebackground='white')
    quadro22.config(pady=20, padx=60,background='white', activebackground='white')
    quadro23.config(pady=20, padx=60,background='white', activebackground='white')
    quadro24.config(pady=20, padx=60,background='white', activebackground='white')
    quadro25.config(pady=20, padx=60,background='white', activebackground='white')
    edtamanho.delete(first=0,last= 3)
    edtamanho2.delete(first=0,last= 3)    

def definir():
    largura = int(edtamanho2.get())
    altura = int(edtamanho.get())

    if (altura in range (10,56) and largura in range(20,121)):
        quadro1.config(padx=largura, pady=altura)
        quadro2.config(padx=largura, pady=altura)
        quadro3.config(padx=largura, pady=altura)
        quadro4.config(padx=largura, pady=altura)
        quadro5.config(padx=largura, pady=altura)
        quadro6.config(padx=largura, pady=altura)
        quadro7.config(padx=largura, pady=altura)
        quadro8.config(padx=largura, pady=altura)
        quadro9.config(padx=largura, pady=altura)
        quadro10.config(padx=largura, pady=altura)
        quadro11.config(padx=largura, pady=altura)
        quadro12.config(padx=largura, pady=altura)
        quadro13.config(padx=largura, pady=altura)
        quadro14.config(padx=largura, pady=altura)
        quadro15.config(padx=largura, pady=altura)
        quadro16.config(padx=largura, pady=altura)
        quadro17.config(padx=largura, pady=altura)
        quadro18.config(padx=largura, pady=altura)
        quadro19.config(padx=largura, pady=altura)
        quadro20.config(padx=largura, pady=altura)
        quadro21.config(padx=largura, pady=altura)
        quadro22.config(padx=largura, pady=altura)
        quadro23.config(padx=largura, pady=altura)
        quadro24.config(padx=largura, pady=altura)
        quadro25.config(padx=largura, pady=altura)
    else:
        alerta()

def pintar(quadro):
    quadro.config(background=pincel, activebackground=pincel)
    return quadro

#Janela definida
janela = Tk()
janela.title('Paleta de Cores')
janela.geometry('700x600+600+200')

#Estilização
icone_gerar = tk.PhotoImage(file='./assets/gerar.png')
icone_resetar= tk.PhotoImage(file='./assets/reset.png')
icone_definir= tk.PhotoImage(file='./assets/definir.png')
icone_sair= tk.PhotoImage(file='./assets/sair.png')

#1.1 - Contâiner para botão e caixa de texto
painel1_1 = tk.Frame(janela, padx=10, pady=10)

lbtamanho = tk.Label(painel1_1, 
                      text='Altura', 
                      pady=10,
                      padx=10
                      )

edtamanho = tk.Entry(painel1_1, 
                      background='white'
                      )

lbtamanho2 = tk.Label(painel1_1, 
                      text='Largura', 
                      pady=10,
                      padx=10
                      )

edtamanho2 = tk.Entry(painel1_1, 
                      background='white'
                      )

btdefinir = tk.Button(painel1_1, 
                     text='Definir',
                     compound=tk.LEFT,
                     image= icone_definir, 
                     pady=3,
                     padx=10,
                     command=lambda: definir()
                     )

#2 - Contâiner para a paleta
painel2 = tk.Frame(janela, pady=20, padx=20)

paleta1 = tk.Button(painel2,pady=20, padx=50, background='white', activebackground='white', bd=2, relief='groove', command= lambda: selecao(paleta1, paleta3, paleta2, paleta4))
paleta2 = tk.Button(painel2,pady=20, padx=50, background='white', activebackground='white', bd=2, relief='groove', command= lambda: selecao(paleta2, paleta1, paleta3, paleta4))
paleta3 = tk.Button(painel2,pady=20, padx=50, background='white', activebackground='white', bd=2, relief='groove', command= lambda: selecao(paleta3, paleta1, paleta2, paleta4))
paleta4 = tk.Button(painel2,pady=20, padx=50, background='white', activebackground='white', bd=2, relief='groove', command= lambda: selecao(paleta4, paleta3, paleta2, paleta1))

#1 - Contâiner para os botões
painel1 = tk.Frame(janela, padx=10, pady=10)

btgerar = tk.Button(painel1, 
                   text="Gerar", 
                   pady=3,
                   padx=13, 
                   compound=tk.LEFT,
                   command=partial(cor),
                   image=icone_gerar
                   )

btresetar= tk.Button(painel1, 
                    text='Resetar',
                    pady=3,
                    padx=10,
                    compound=tk.LEFT,
                    command=partial(reset),
                    image= icone_resetar
                    )   

#3 - Contâiner para os quadros
painel3 = tk.Frame(janela)
quadro1 = tk.Button(painel3, pady=20, padx=60,background='white', activebackground='white', command=lambda: pintar(quadro1))
quadro2 = tk.Button(painel3, pady=20, padx=60,background='white', activebackground='white', command=lambda: pintar(quadro2))
quadro3 = tk.Button(painel3, pady=20, padx=60,background='white', activebackground='white', command=lambda: pintar(quadro3))
quadro4 = tk.Button(painel3, pady=20, padx=60,background='white', activebackground='white', command=lambda: pintar(quadro4))
quadro5 = tk.Button(painel3, pady=20, padx=60,background='white', activebackground='white', command=lambda: pintar(quadro5))

painel3_1 = tk.Frame(janela)
quadro6 = tk.Button(painel3_1, pady=20, padx=60,background='white', activebackground='white', command=lambda: pintar(quadro6))
quadro7 = tk.Button(painel3_1, pady=20, padx=60,background='white', activebackground='white', command=lambda: pintar(quadro7))
quadro8 = tk.Button(painel3_1, pady=20, padx=60,background='white', activebackground='white', command=lambda: pintar(quadro8))
quadro9 = tk.Button(painel3_1, pady=20, padx=60,background='white', activebackground='white', command=lambda: pintar(quadro9))
quadro10 = tk.Button(painel3_1, pady=20, padx=60,background='white', activebackground='white', command=lambda: pintar(quadro10))

painel3_2 = tk.Frame(janela)
quadro11 = tk.Button(painel3_2, pady=20, padx=60,background='white', activebackground='white', command=lambda: pintar(quadro11))
quadro12 = tk.Button(painel3_2, pady=20, padx=60,background='white', activebackground='white', command=lambda: pintar(quadro12))
quadro13 = tk.Button(painel3_2, pady=20, padx=60,background='white', activebackground='white', command=lambda: pintar(quadro13))
quadro14 = tk.Button(painel3_2, pady=20, padx=60,background='white', activebackground='white', command=lambda: pintar(quadro14))
quadro15 = tk.Button(painel3_2, pady=20, padx=60,background='white', activebackground='white', command=lambda: pintar(quadro15)) 

painel3_3 = tk.Frame(janela)
quadro16 = tk.Button(painel3_3, pady=20, padx=60,background='white', activebackground='white', command=lambda: pintar(quadro16))
quadro17 = tk.Button(painel3_3, pady=20, padx=60,background='white', activebackground='white', command=lambda: pintar(quadro17))
quadro18 = tk.Button(painel3_3, pady=20, padx=60,background='white', activebackground='white', command=lambda: pintar(quadro18))
quadro19 = tk.Button(painel3_3, pady=20, padx=60,background='white', activebackground='white', command=lambda: pintar(quadro19))
quadro20 = tk.Button(painel3_3, pady=20, padx=60,background='white', activebackground='white', command=lambda: pintar(quadro20))

painel3_4 = tk.Frame(janela)
quadro21 = tk.Button(painel3_4, pady=20, padx=60,background='white', activebackground='white', command=lambda: pintar(quadro21))
quadro22 = tk.Button(painel3_4, pady=20, padx=60,background='white', activebackground='white', command=lambda: pintar(quadro22))
quadro23 = tk.Button(painel3_4, pady=20, padx=60,background='white', activebackground='white', command=lambda: pintar(quadro23))
quadro24 = tk.Button(painel3_4, pady=20, padx=60,background='white', activebackground='white', command=lambda: pintar(quadro24))
quadro25 = tk.Button(painel3_4, pady=20, padx=60,background='white', activebackground='white', command=lambda: pintar(quadro25))

#4 - Contâiner para o botão "Sair"
painel4 = tk.Frame(janela, pady=20, padx=20)

btsair = tk.Button(painel4, 
                  text='Sair', 
                  pady=3,
                  padx=10,
                  compound=tk.LEFT,
                  image= icone_sair, 
                  command=janela.destroy
                  )

#Packs
painel1.pack(side=TOP)
btgerar.pack(side=LEFT)
btresetar.pack(side=RIGHT)

painel1_1.pack(side=TOP)
lbtamanho.pack(side=LEFT)
edtamanho.pack(side=LEFT)
btdefinir.pack(side=RIGHT)

painel1_1.pack(side=TOP)
lbtamanho2.pack(side=LEFT)
edtamanho2.pack(side=LEFT)

painel2.pack(side=TOP)
paleta1.pack(side=LEFT)
paleta2.pack(side=LEFT)
paleta3.pack(side=LEFT)
paleta4.pack(side=LEFT)

painel3.pack(side=TOP)
quadro1.pack(side=LEFT)
quadro2.pack(side=LEFT)
quadro3.pack(side=LEFT)
quadro4.pack(side=LEFT)
quadro5.pack(side=LEFT)

painel3_1.pack()
quadro6.pack(side=LEFT)
quadro7.pack(side=LEFT)
quadro8.pack(side=LEFT)
quadro9.pack(side=LEFT)
quadro10.pack(side=LEFT)

painel3_2.pack()
quadro11.pack(side=LEFT)
quadro12.pack(side=LEFT)
quadro13.pack(side=LEFT)
quadro14.pack(side=LEFT)
quadro15.pack(side=LEFT)

painel3_3.pack()
quadro16.pack(side=LEFT)
quadro17.pack(side=LEFT)
quadro18.pack(side=LEFT)
quadro19.pack(side=LEFT)
quadro20.pack(side=LEFT)

painel3_4.pack()
quadro21.pack(side=LEFT)
quadro22.pack(side=LEFT)
quadro23.pack(side=LEFT)
quadro24.pack(side=LEFT)
quadro25.pack(side=LEFT)

painel4.pack()
btsair.pack()

janela.mainloop()