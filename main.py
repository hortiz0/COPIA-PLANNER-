#Alunos: Adriana Maciel Quintana Hortiz, Alexandre Adryan Fernandes Rodrigues, Beatriz Júlia Cavalcantes dos Santos e William de Mendonça Ribeiro
#2° ano técnico em informática vespertino


#Bibliotecas
from tkinter import *
from interface import *

#principal.mainloop()

from evento import*
from usuario import*
import os
from tkinter import * 
from datetime import date
import calendar

#Globais
novosUsuarios = []

global alguem

global eventos
Eventos = []

#Funções
def iniciar():
  global novosUsuarios
  print('\033[1;49;31m BEM VINDO AO SEU PLANNER \033[m')
  
  quest = int(input("\n1 - LOGIN \n2 - CADASTRO \n3 - DEFINIR EVENTO \n4 - EXIBIR AGENDAMENTO DO EVENTO \n5 - EXIBIR CALENDARIO \n6 - INFORMAÇÕES DE USUÁRIO \n--> "))
  if quest == 1:
    alguem = Usuario('','','','')
    alguem.login()
    novosUsuarios.append(alguem)
    os.system("clear")
    iniciar()
  if quest == 2:
    print('\033[1;49;36m \n-INICIANDO SEU CADASTRO- \033[m')
    alguem = Usuario('','','','')
    alguem.cadastro()
    novosUsuarios.append(alguem)
    os.system("clear")
    iniciar()
  elif quest == 3:
    definirEvento()
    os.system("clear")
    iniciar()
  elif quest == 4:
    exibirEvento()
  elif quest == 5:
    exibirCalendar()
    iniciar()
  elif quest == 6:
    os.system("clear")
    if len(novosUsuarios) == 0:
      print("i")
    else:
     for a in novosUsuarios:
       print("Nome: {} \nEmail: {}\nTelefone: {}\n".format(a.getNome(), a.getEmail(),a.getTele()))
       
    retornar()
  elif quest < 1:
   raise Exception("Não aceitamos número abaixo de zero")
  elif quest>6:
    raise Exception("Não aceitamos números maiores que 6")
  
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