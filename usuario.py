#Classe usuário
from evento import *
import os

class Usuario:
  def __init__(self, nome, email, senha, tele):
    self.__nome = nome
    self.__email = email
    self.__senha = senha
    self.__tele= tele
    self.evento= Evento()
    self.us = []

  def cadastro(self):
    self.__nome = input('Digite o seu nome: ')
    self.__email = input('Digite o seu email: ')
    self.__senha = input('Digite sua senha: ')
    self.__tele= input('Digite seu telefone: ')
    self.us.extend((self.__nome,self.__email,self.__senha,self.__tele))
    
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
      print("i")
    else:
      for a in novosUsuarios:
        print("Nome: {} \nEmail: {} \nSenha: {}Telefone: {} ".format (a.nome, a.email, a.senha, a.tele))

  def login(self):
    os.system('clear')
    print('LOGIN')
    em = input('Digite seu email: ')
    sen = input('digite sua senha: ')
    if em in email:
     self.senha_login(login)
    else:
      print('email incorreto')
      self.fazer_login()


