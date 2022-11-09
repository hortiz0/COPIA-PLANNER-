# class Evento

from tkinter import * 

cor1='orange'

class Evento:
  def __init__(self):
    self.__nomeEvento = ''
    self.__localEvento = ''
    self.__horarioEvento = ''
    self.__dataEvento = ''
    self.__dialivre = ''
    self.eventos = []
    self.eventoes = []

  def definirEvento(self):
    janela_evento = Tk()
    janela_evento.title("BEM VINDO AO DEFINIR EVENTO")
    janela_evento.configure(background=cor1)
    janela_evento.geometry("700x500+200+200")
    quest = Label(janela_evento, text="EVENTO", background=cor1)
    quest.place(x=120, y=20)
    quest1 = Label(janela_evento, text= "Nome: ", background= cor1)
    quest1.place(x=50, y=50)
    entrada1= Entry(janela_evento)
    entrada1.place(x=130, y=50)
    quest2 = Label(janela_evento, text= "Local: ", background= cor1)
    quest2.place(x=50, y=80)
    entrada2= Entry(janela_evento)
    entrada2.place(x=130, y=80)
    quest3 = Label(janela_evento, text= "Horário: ", background= cor1)
    quest3.place(x=50, y=110)
    entrada3= Entry(janela_evento)
    entrada3.place(x=130, y=110)
    quest4 = Label(janela_evento, text= "Data: ", background= cor1)
    quest4.place(x=50, y=140)
    entrada4= Entry(janela_evento)
    entrada4.place(x=130, y=140)
    quest5 = Label(janela_evento, text= "Dias livres: ", background= cor1)
    quest5.place(x=50, y=170)
    entrada5= Entry(janela_evento)
    entrada5.place(x=130, y=170)
    
    def bt_click():
       self.__nomeEvento = entrada1.get()
       self.__localEvento = entrada2.get()
       self.__horarioEvento = entrada3.get()
       self.__dataEvento = entrada4.get()
       self.__dialivre = entrada5.get()
       self.eventos.extend((self.__nomeEvento,self.__localEvento,self.__horarioEvento, self.__dataEvento, self.__dialivre))
       self.eventoes.append(self.eventos)
       janela_evento.destroy()
    
    botao_evento = Button(janela_evento, text = 'enviar', command=bt_click)
    botao_evento.place(x = 50, y = 220)


    janela_evento.mainloop()
       
  def exibirT(self):
    
    janela_exibir= Tk()
    janela_exibir.title("JANELA EXIBIR TAREFAS")
    janela_exibir.configure(background=cor1)
    janela_exibir.geometry("700x500+200+200")
    quest = Label(janela_exibir, text="TAREFAS", background=cor1)
    quest.place(x=120, y=20)
    x = 0
    eixo_y = 80
    for e in self.eventoes:   
      quest1 = Label(janela_exibir, text= ('NOME: ', self.eventos[x]), background= cor1)
      quest1.place(x=50, y=eixo_y)
      quest2 = Label(janela_exibir, text= ('LOCAL: ', self.eventos[x+1]), background= cor1)
      quest2.place(x=50, y=eixo_y+20)
      quest3 = Label(janela_exibir, text= ('HORÁRIO: ', self.eventos[x+2]), background= cor1)
      quest3.place(x=50, y=eixo_y+40)
      quest4 = Label(janela_exibir, text= ('DATA: ', self.eventos[x+3]), background= cor1)
      quest4.place(x=50, y=eixo_y+60)
      quest5 = Label(janela_exibir, text= ('DIA LIVRE: ', self.eventos[x+4]), background= cor1)
      quest5.place(x=50, y=eixo_y+80)
      eixo_y+=110
      x +=4
      
    def bt_click(): 
      janela_exibir.destroy()
      
    botao = Button(janela_exibir, text = 'voltar', command=bt_click)
    botao.place(x = 50, y = eixo_y+30)

    janela_exibir.mainloop()

#Fim class