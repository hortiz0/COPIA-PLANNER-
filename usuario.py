from evento import *
import os
import time
pessoas = []
dicionario = {}
usuario = []
global email
email = []
senha= []
from tkinter import *

class Usuario:
  def __init__(self, nome, email, senha, tele):
    self.__nome = nome
    self.__email = email
    self.__senha = senha
    self.__tele= tele
    self.evento= Evento()    

  def cadastro(self):
    os.system('clear')
    print('cadastro')
    arquivo = open('arquivo.txt', '+a')
    self.__nome = input('Digite o seu nome: ')
    arquivo.write(self.__nome)
    arquivo.write('\n')
    self.__email = input('Digite o seu email: ')
    arquivo.write(self.__email)
    arquivo.write('\n')
    self.__senha = input('Digite sua senha: ')
    arquivo.write(self.__senha)
    arquivo.write('\n')
    self.__tele= input('Digite seu telefone: ')
    print()
    print('cadastro concluido')
    time.sleep(3)
    arquivo.write(self.__tele)
    arquivo.write('\n')
    email.append(self.__email)
    pessoas.insert(0,(self.__nome,self.__email,self.__senha,self.__tele))
    arquivo.seek(0,0)
    arquivo.close

    #sql_dados= "INSERT INTO users(nome, email,senha,tele) VALUES ('" + self.nome + "', '" + self.__email + "', '" + self.__senha +'", "' + self.__tele + "')"

    #insert_data(conexao, sql_dados)
 
    
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
    print('nome do usuario:',self.__nome)
  def exibir(self):
    if len(novosUsuarios) == 0:
      print("escolha 1 ou 2")
    else:
      for a in novosUsuarios:
        print("Nome: {} \nEmail: {} \nSenha: {}Telefone: {} ".format (a.nome, a.email, a.senha, a.tele))

  def login(self):
    os.system('clear')
    print('LOGIN')
    em = input('Digite seu email: ')
    senha= input('digite sua senha: ')
    if em  in email:
     self.senha_login(em)
    else:
      print('não existe, faça seu cadastro')
      time.sleep(6)
      


  

  
    