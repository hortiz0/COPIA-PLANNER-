#Alunos: Adriana Maciel Quintana Hortiz, Alexandre Adryan Fernandes Rodrigues, Beatriz Júlia Cavalcantes dos Santos e William de Mendonça Ribeiro
#2° ano técnico em informática vespertino


#Bibliotecas
from tkinter import *
#principal.mainloop()

from evento import*
from usuario import*
import os
from tkinter import * 
from datetime import date
import calendar
global novosUsuarios
definirEvento=[]

#Globais
novosUsuarios = []

global alguem

global eventos
Eventos = []


#Funções
def iniciar():
  cor1 = "#993399"
  principal = Tk()
  principal.title("BEM VINDO AO SEU PLANNER")
  principal.configure( background = cor1)
  principal.geometry("700x500+200+200")
  quest = Label(principal, text = "PLANNER", background = cor1)
  quest.place(x = 100, y = 20)
  quest1 = Label(principal, text = "1 - LOGIN ", background = cor1)
  quest1.place(x = 70, y = 40)
  quest2 = Label(principal, text = "2 - CADASTRO ", background = cor1)
  quest2.place(x = 70, y = 60)
  quest3 = Label(principal, text = "3 - DEFINIR EVENTO ", background = cor1)
  quest3.place(x = 70, y = 80)
  quest4 = Label(principal, text = "4 - EXIBIR AGENDAMENTO DO EVENTO ", background = cor1)
  quest4.place(x = 70, y = 100)
  quest5 = Label(principal, text = "5 - EXIBIR CALENDARIO ", background = cor1)
  quest5.place(x = 70, y = 120)
  quest6 = Label(principal, text = "6 - INFORMAÇÕES DO USUARIO ", background = cor1)
  quest6.place(x = 70, y = 140)
  entrada = Entry(principal)
  entrada.place( x = 70, y = 170)
  def btclick():
    if int(entrada.get()) == 1:
      alguem = Usuario('','','','')
      alguem.login()
      novosUsuarios.append(alguem)
      os.system("clear")
      iniciar()
    elif int(entrada.get()) == 2:
      print('\033[1;49;36m \n-INICIANDO SEU CADASTRO- \033[m')
      alguem = Usuario('','','','')
      alguem.cadastro()
      novosUsuarios.append(alguem)
      os.system("clear")
      iniciar()
    elif int(entrada.get()) == 3:
      definirEvento()
      os.system("clear")
      iniciar()
    elif int(entrada.get()) == 4:
      exibirEvento()
    elif int(entrada.get()) == 5:
      exibirCalendar()
      iniciar()
    elif int(entrada.get()) == 6:
      os.system("clear")
      if len(novosUsuarios) == 0:
        print("não tem usuario")
        retornar()
    else:
      print('digite um numero de 1 a 6')
  

  botao = Button(principal, text = 'enviar', command = btclick )
  botao.place (x= 70, y=200)

  
def definirEvento():
  os.system("clear")
  evento.definirEvento()
  retornar()

def exibirEvento():
  evento.exibirT()
  retornar()
  
def exibirCalendar():
  print('Calendario')
  print(calendar.calendar(2022))
  retornar()

#Retornar ao inciar
def retornar():
  op = int(input("DIGITE 0 SE DESEJA VOLTAR PARA O MENU: "))
  try:
    op != 0
  except:
    print(" Número não identificado")
  finally:
    print("APENAS O NÚMERO 0 PARA VOLTAR AO MENU")
    
  if op == 0:
    os.system("clear")
    iniciar()
#Objeto
alguem = Usuario('', '', '', '')
evento = Evento()

#fim da class  

#Start
iniciar()