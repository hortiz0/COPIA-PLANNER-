# class Evento
eventos = []
eventoes = []
from tkinter import * 

cor1='orange'

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
    quest1.place(x=50, y=40)
    entrada1= Entry(janela_evento)
    entrada1.place(x=120, y=60)
    quest2 = Label(janela_evento, text= "Digite o local do seu evento: ", background= cor1)
    quest2.place(x=50, y=80)
    entrada2= Entry(janela_evento)
    entrada2.place(x=120, y=100)
    quest3 = Label(janela_evento, text= "Digite o horário do seu evento: ", background= cor1)
    quest3.place(x=50, y=120)
    entrada3= Entry(janela_evento)
    entrada3.place(x=120, y=140)
    quest4 = Label(janela_evento, text= "Digite a data do seu evento: ", background= cor1)
    quest4.place(x=50, y=180)
    entrada4= Entry(janela_evento)
    entrada4.place(x=120, y=200)
    quest5 = Label(janela_evento, text= "Digite o mês do seu evento: ", background= cor1)
    quest5.place(x=50, y=220)
    entrada5= Entry(janela_evento)
    entrada5.place(x=120, y=240)
    quest6 = Label(janela_evento, text= "Digite o ano do seu evento: ", background= cor1)
    quest6.place(x=50, y=280)
    entrada6= Entry(janela_evento)
    entrada6.place(x=120, y=300)
    quest7 = Label(janela_evento, text= "Digite os dias livres: ", background= cor1)
    quest7.place(x=50, y=320)
    entrada7= Entry(janela_evento)
    entrada7.place(x=120, y=340)
    
    def bt_click():
       self.__nomeEvento = entrada1.get()
       self.__localEvento = entrada1.get()
       self.__horarioEvento = entrada1.get()
       self.__dataEvento = entrada1.get()
       self.__mesEvento = entrada1.get()
       self.__anoEvento = entrada1.get()
       self.__dialivre = entrada1.get()
       eventos.extend((self.__nomeEvento, self.__localEvento, self.__horarioEvento, self.__dataEvento, self.__mesEvento, self.__anoEvento, self.__dialivre))
       eventoes.append(eventos)
    
    def bt_click1():
      janela_evento.destroy()
    

    botao_voltar = Button(janela_evento, text= 'voltar ao inicio', command = bt_click1)
    botao_voltar.place(x=50, y=410)
    botao_evento = Button(janela_evento, text = 'enviar', command=bt_click)
    botao_evento.place(x = 50, y = 380)

  

    janela_evento.mainloop()
       
  def exibirT(self):
    for e in eventoes:
      
      janela_exibirT= Tk()
      janela_exibirT.title("BEM VINDO AO EXIBIR EVENTOS")
      janela_exibirT.configure(background=cor1)
      janela_exibirT.geometry("700x500+200+200")
      quest = Label(janela_exibirT, text="EVENTOS CADASTRADOS", background=cor1)
      quest.place(x=120, y=20)
      quest1 = Label(janela_exibirT, text= "Nome: ", background= cor1,(eventos[x])
                   
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