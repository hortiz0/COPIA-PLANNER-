# class Evento
eventos = []
eventoes = []
from tkinter import * 

class Evento:
  def _init__(self):
    self.__nomeEvento = ''
    self.__localEvento= ''
    self.__horarioEvento = ''
    self.__dataEvento = ''
    self.__mesEvento= ''
    self.__anoEvento= ''
    self.__dialivre= ''
    


  def definirEvento(self):
    print('\033[1;49;36m -AGENDANDO EVENTO- \033[m')
    self.__nomeEvento = input("Defina o nome do evento: ")
    self.__localEvento = input("Insira o local do evento: ")
    self.__horarioEvento = input("Insira o horário do evento: ")
    self.__dataEvento = input("Digite a data do evento: ")
    self.__mesEvento = input("Digite o mês do evento: ")
    self.__anoEvento = input("Digite o ano do evento: ")
    self.__dialivre= input("Digite os dias livres: ")
    eventos.extend((self.__nomeEvento, self.__localEvento, self.__horarioEvento, self.__dataEvento, self.__mesEvento, self.__anoEvento, self.__dialivre))
    eventoes.append(eventos)
    
  def exibirT(self):
    x = 0
    print('\nDADOS DO EVENTO')
    for e in eventoes:
      print('nome:', eventos[x])
      print('local:', eventos[x+1])
      print('horario:', eventos[x+2])
      print('data:', eventos[x+3])
      print('mes:', eventos[x+4])
      print('ano:', eventos[x+5])
      print('dia livre:', eventos[x+6])
      print('\n')
      x += 7


#Fim class