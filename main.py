from usuario import *
import os
from tkinter import *
import calendar
import sqlite3

definirEvento = []

# Globais

global alguem

global eventos
Eventos = []
alguem = Usuario()

from usuario import novosUsuarios
# Funções

def bd():
  print('\n1 - ver banco de dados\n2 - excluir dados\n3 - voltar')
  a=int(input("-> "))
  if a==1:
    alguem.ler()
    os.system('clear')
    bd()
  elif a==2:
    alguem.excluir()
    os.system('clear')
    bd()
  elif a==3:
    iniciar()
  else:
    print('digite 1 ou 2')

def iniciar():
    cor1 = "#993399"
    principal = Tk()
    principal.title("BEM VINDO AO SEU PLANNER")
    principal.configure(background=cor1)
    principal.geometry("700x500+200+200")
    quest = Label(principal, text="PLANNER", background=cor1)
    quest.place(x=100, y=20)
    quest1 = Label(principal, text="1 - LOGIN ", background=cor1)
    quest1.place(x=70, y=40)
    quest2 = Label(principal, text="2 - CADASTRO ", background=cor1)
    quest2.place(x=70, y=60)
    quest3 = Label(principal, text="3 - BANCO DE DADOS ", background=cor1)
    quest3.place(x=70, y=80)
    entrada = Entry(principal)
    entrada.place(x=70, y=110)

    def btclick():
        if int(entrada.get()) == 1:
            principal.destroy()
            alguem.login()
            iniciar()
        elif int(entrada.get()) == 2:
            principal.destroy()
            alguem.cadastro()
            iniciar()
        elif int(entrada.get()) == 3:
          bd()

    botao = Button(principal, text='enviar', command=btclick)
    botao.place(x=70, y=140)
    principal.mainloop()
  
# Start
iniciar()
