#Alunos: Adriana Maciel Quintana Hortiz, Alexandre Adryan Fernandes Rodrigues, Beatriz Júlia Cavalcantes dos Santos e William de Mendonça Ribeiro
#2° ano técnico em informática vespertino


#Bibliotecas
from evento import*
from usuario import*
import os
from datetime import date
import calendar

#Globais
novosUsuarios = []

global alguem

global eventos
Eventos = []

quest = -1


usuCamila=Usuario('Camila','camila','camila','1')
usuCamila.exibirNome()
usuCamila.evento.definirEvento()
usuCamila.evento.exibirT()
       
#Funções
def iniciar():
  global novosUsuarios
  print('\033[1;49;31m BEM VINDO AO SEU PLANNER \033[m')
  
  quest = int(input("\n1 - CADASTRO \n2 - DEFINIR EVENTO \n3 - EXIBIR AGENDAMENTO DO EVENTO \n4 - EXIBIR CALENDARIO \n5 - INFORMAÇÕES DE USUÁRIO \n--> "))
  if quest == 1:
    print('\033[1;49;36m \n-INICIANDO SEU CADASTRO- \033[m')
    alguem = Usuario()
    alguem.cadastro()
    novosUsuarios.append(alguem)
    os.system("clear")
    iniciar()
  elif quest == 2:
    definirEvento()
    os.system("clear")
    iniciar()
  elif quest == 3:
    exibirEvento()
  elif quest == 4:
    exibirCalendar()
    iniciar()
  elif quest == 5:
    os.system("clear")
    if len(novosUsuarios) == 0:
      print("i")
    else:
     for a in novosUsuarios:
       print("Nome: {} \nEmail: {}\nTelefone: {}\n".format(a.getNome(), a.getEmail(),a.getTele()))
       
    retornar()
  elif quest < 1:
   raise Exception("Não aceitamos número abaixo de zero")
  
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
alguem = Usuario()
evento = Evento()

#fim da class  

#Start
iniciar()