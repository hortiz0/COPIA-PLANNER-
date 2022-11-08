from evento import *
import os
import time

pessoas = []
usuario = []
global email
email = []
senha = []
from tkinter import *

global novosUsuarios
novosUsuarios = []


cor1 = "#993399"

class Usuario:
    def __init__(self):
        self.__nome = ''
        self.__email = ''
        self.__senha = ''
        self.__tele = ''
        self.evento = Evento()

    def cadastro(self):
        janela_cadastro = Tk()
        janela_cadastro.title("BEM VINDO AO CADASTRO")
        janela_cadastro.configure(background=cor1)
        janela_cadastro.geometry("700x500+200+200")
        quest = Label(janela_cadastro, text="CADASTRO", background=cor1)
        quest.place(x=150, y=20)
        quest1 = Label(janela_cadastro, text="Nome: ", background=cor1)
        quest1.place(x=70, y=50)
        entrada1 = Entry(janela_cadastro)
        entrada1.place(x=130, y=50)
        quest2 = Label(janela_cadastro, text="Email: ", background=cor1)
        quest2.place(x=70, y=80)
        entrada2 = Entry(janela_cadastro)
        entrada2.place(x=130, y=80)
        quest3 = Label(janela_cadastro, text="Senha: ", background=cor1)
        quest3.place(x = 70, y=110)
        entrada3 = Entry(janela_cadastro)
        entrada3.place(x=130, y=110)
        quest4 = Label(janela_cadastro, text="Telefone: ", background=cor1)
        quest4.place(x=70, y=140)
        entrada4 = Entry(janela_cadastro)
        entrada4.place(x=130, y=140)

        def bt_click():
          self.__nome = entrada1.get()
          self.__email = entrada1.get()
          self.__senha = entrada1.get()
          self.__tele = entrada1.get()
          email.append(self.__email)
          senha.append(self.__senha)
          janela_cadastro.destroy()

          
        botao = Button(janela_cadastro, text = 'enviar', command=bt_click)
        botao.place(x = 70, y = 180)

        
        janela_cadastro.mainloop()
      
    def getCadastro(self):
        return self.__nome
        return self.__email
        return self.__senha
        return self.__tele

    def getNome(self):
        return self.__nome

    def getEmail(self):
        return self.__email

    def getTele(self):
        return self.__tele

    def exibirNome(self):
        print('nome do usuario: ', self.__nome)

    def exibir(self):
        if len(novosUsuarios) == 0:
            print("escolha 1 ou 2")
        else:
            for a in novosUsuarios:
                print("Nome: {} \nEmail: {} \nSenha: {}Telefone: {} ".format(a.nome, a.email, a.senha, a.tele))

    def login(self):
        janela_login = Tk()
        janela_login.title("BEM VINDO AO LOGIN")
        janela_login.configure(background=cor1)
        janela_login.geometry("700x500+200+200")
        quest = Label(janela_login, text="LOGIN", background=cor1)
        quest.place(x=120, y=20)
        quest1 = Label(janela_login, text="Email: ", background=cor1)
        quest1.place(x=70, y=50)
        entrada1 = Entry(janela_login)
        entrada1.place(x=120, y=50)
        quest2 = Label(janela_login, text="Senha: ", background=cor1)
        quest2.place(x=70, y=80)
        entrada2 = Entry(janela_login)
        entrada2.place(x=120, y=80)

        def bt_click():
          if entrada1.get() in email:
            indice = email.index(entrada1.get())
            if entrada2.get() in senha[indice]:
              janela_login.destroy()
            else:
              quest3 = Label(janela_login, text="senha errada", background=cor1)
              quest3.place(x=70, y=150)
          else:
            quest4 = Label(janela_login, text="email não existe", background=cor1)
            quest4.place(x=70, y=150)
            
          def  bt_click2():
            janela_login.destroy()  
          
          botao_voltar = Button(janela_login, text= 'voltar ao inicio', command = bt_click2)
          botao_voltar.place(x=70, y=180)
            
        botao_login = Button(janela_login, text = 'enviar', command=bt_click)
        botao_login.place(x = 70, y = 110)
        


        
        janela_login.mainloop()
      
      
      






