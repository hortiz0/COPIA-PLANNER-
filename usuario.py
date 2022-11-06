from evento import *
import os
pessoas = []
dicionario = {}

class Usuario:
  def __init__(self, nome, email, senha, tele):
    self.__nome = nome
    self.__email = email
    self.__senha = senha
    self.__tele= tele
    self.evento= Evento()

  def cadastro(self):
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
    arquivo.write(self.__tele)
    arquivo.write('\n')
    pessoas.insert(0,(self.__nome,self.__email,self.__senha,self.__tele))
    arquivo.seek(0,0)
    arquivo.close
    
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
    if em and sen in email:
    self.senha_login(em)
    
    else:
      print('email inexistente')
      input('enter pra tentar novamente')
      self.login()
  def senha_login
  
