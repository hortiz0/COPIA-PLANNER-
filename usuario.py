from evento import *
import os
import time
import sqlite3
from tkinter.messagebox import*
global email
email = []
senha = []

from tkinter import *


global novosUsuarios
novosUsuarios = []

cor1 = "#993399"
evento = Evento()

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
          self.__email = entrada2.get()
          self.__senha = entrada3.get()
          self.__tele = entrada4.get()
          email.append(self.__email)
          senha.append(self.__senha)
          novosUsuarios.extend((self.__nome, self.__email, self.__tele))
          self.banco_de_dados(self.__nome, self.__email, self.__senha, self.__tele)
          janela_cadastro.destroy()

          
        botao = Button(janela_cadastro, text = 'enviar', command=bt_click)
        botao.place(x = 70, y = 180)

        janela_cadastro.mainloop()

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
              email_login = entrada1.get()
              janela_login.destroy()
              self.escolha(email_login)
            else:
              print(showerror("error", "senha errada")) 
          else:
            print(showerror("error", "você não possui cadastro")) 
            
          def bt_click2():
            janela_login.destroy()  
          
          botao_voltar = Button(janela_login, text= 'voltar ao inicio', command = bt_click2)
          botao_voltar.place(x=70, y=180)
            
        botao_login = Button(janela_login, text = 'enviar', command=bt_click)
        botao_login.place(x = 70, y = 110)
        

        
        janela_login.mainloop()

    def escolha(self, email_login):
      janela_menu=Tk()
      janela_menu.title("MENU")
      janela_menu.configure(background=cor1)
      janela_menu.geometry("700x500+200+200")
      quest = Label(janela_menu, text="MENU DE OPÇÕES", background=cor1)
      quest.place(x = 100, y = 20)
      escolha1 = Label(janela_menu, background=cor1, text = '1 - DEFINIR EVENTO')
      escolha1.place(x = 50, y = 50 )
      escolha2 = Label(janela_menu, background=cor1, text = '2 - MOSTRAR EVENTOS CADASTRADOS')
      escolha2.place(x = 50, y = 70 )
      escolha3 = Label(janela_menu, background=cor1, text = '3 - MOSTRAR CALENDÁRIO')
      escolha3.place(x = 50, y = 90 )
      escolha4 = Label(janela_menu, background=cor1, text = '4 - DADOS DO USUÁRIO')
      escolha4.place(x = 50, y = 110 )
      entrada = Entry(janela_menu)
      entrada.place(x=50, y= 140)
      
      def bt_click():
        if int(entrada.get()) == 1:
            janela_menu.destroy()
            evento.definirEvento()
            self.escolha(email_login)
          
        elif int(entrada.get()) == 2:
            janela_menu.destroy()
            evento.exibirT()
            self.escolha(email_login)
          
        elif int(entrada.get()) == 3:
            janela_menu.destroy()
            print('oi')
            self.escolha(email_login)
          
        elif int(entrada.get()) == 4:
            janela_menu.destroy()
            self.dadosUsuario(email_login)
            self.escolha(email_login)
            
          
      botao = Button(janela_menu, text='enviar', command = bt_click)
      botao.place(x=50, y=170)
      janela_menu.mainloop()

    def dadosUsuario(self, email_login):
       indice = novosUsuarios.index(email_login)
       print('nome:', novosUsuarios[indice-1])
       print('email:', novosUsuarios[indice])
       print('telefone:', novosUsuarios[indice+2])
       input('enter para voltar ao menu')
       os.system('clear')
     
    def banco(self):
      global conexao, c
      conexao = sqlite3.connect('Planner.db')
      c= conexao.cursor()
      c.execute("""
      CREATE TABLE IF NOT EXISTS  Usuario (
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            senha TEXT NOT NULL,
            telefone TEXT NOT NULL
      );
      """)
  
        
    def banco_de_dados(self, nome, email, senha, tele):
      self.banco()
  
      c.execute("""INSERT INTO Usuario (nome,email,senha,telefone) 
                    VALUES (?, ? , ?, ?)"""
                , (nome, email, senha, tele))
      
      conexao.commit()
      
      c.close()
      conexao.close()

    def ler(self):
      self.banco()
      c.execute("""
      SELECT * FROM Usuario;
      """)

      for linha in c.fetchall():
        print(linha)

      c.close()
      conexao.close()

      input('enter para voltar')


    def excluir(self):
      self.banco()

      email_banco = input('email do usuário: ')
      c.execute("""
      DELETE FROM Usuario
      WHERE email = ?
      """,(email_banco,))

      conexao.commit()
      conexao.close()

      input('enter para voltar')


      

        
      
      






