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
    janela_evento = Tk()
    janela_evento.title("BEM VINDO AO DEFINIR EVENTO")
    janela_evento.configure(background=cor1)
    janela_evento.geometry("700x500+200+200")
    quest = Label(janela_evento, text="EVENTO", background=cor1)
    quest.place(x=120, y=20)
    quest1 = Label(janela_evento, text= "Digite o nome do seu evento: ", background= cor1)
    entrada1= Entry(janela_evento)
    entrada1.place(x=120, y=50)
    quest2 = Label(janela_evento, text= "Digite o local do seu evento: ", background= cor1)
    entrada2= Entry(janela_evento)
    entrada2.place(x=120, y=50)
    quest3 = Label(janela_evento, text= "Digite o horário do seu evento: ", background= cor1)
    entrada3= Entry(janela_evento)
    entrada3.place(x=120, y=50)
    quest4 = Label(janela_evento, text= "Digite a data do seu evento: ", background= cor1)
    entrada4= Entry(janela_evento)
    entrada4.place(x=120, y=50)
    quest5 = Label(janela_evento, text= "Digite o mês do seu evento: ", background= cor1)
    entrada5= Entry(janela_evento)
    entrada5.place(x=120, y=50)
    quest6 = Label(janela_evento, text= "Digite o ano do seu evento: ", background= cor1)
    entrada6= Entry(janela_evento)
    entrada6.place(x=120, y=50)
    quest7 = Label(janela_evento, text= "Digite os dias livres: ", background= cor1)
    entrada7= Entry(janela_evento)
    entrada7.place(x=120, y=50)
    
    def bt_click():
      botao_voltar = Button(janela_evento, text= 'voltar ao inicio', command = bt_click)
      botao_voltar.place(x=70, y=180)
      botao_evento = Button(janela_login, text = 'enviar', command=bt_click)
      botao_evento.place(x = 70, y = 110)
      janela_login.mainloop()
  
               
    
    

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