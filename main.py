from usuario import *
import os
from tkinter import *
import calendar

definirEvento = []

# Globais

global alguem

global eventos
Eventos = []

evento = Evento()


# Funções

def iniciar():
    alguem = Usuario()
    cor1 = "#993399"
    principal = Tk()
    principal.title("BEM VINDO AO SEU PLANNER")
    principal.configure(background=cor1)
    principal.geometry("700x500+200+200")
    quest = Label(principal, text="PLANNER", background=cor1)
    quest.place(x=100, y=20)
    quest1 = Label(principal, text="1 - LOGIN ", background=cor1)
    quest1.place(x=70, y=40)
    quest2 = Label(principal, text="2 - CADASTRO ", background=cor1)
    quest2.place(x=70, y=60)
    quest3 = Label(principal, text="3 - DEFINIR EVENTO ", background=cor1)
    quest3.place(x=70, y=80)
    quest4 = Label(principal, text="4 - EXIBIR AGENDAMENTO DO EVENTO ", background=cor1)
    quest4.place(x=70, y=100)
    quest5 = Label(principal, text="5 - EXIBIR CALENDARIO ", background=cor1)
    quest5.place(x=70, y=120)
    quest6 = Label(principal, text="6 - INFORMAÇÕES DO USUARIO ", background=cor1)
    quest6.place(x=70, y=140)
    entrada = Entry(principal)
    entrada.place(x=70, y=170)

    def btclick():
        if int(entrada.get()) == 1:
            principal.destroy()
            os.system('clear')
            alguem.login()
            novosUsuarios.append(alguem)
            iniciar()
        elif int(entrada.get()) == 2:
            principal.destroy()
            print('\033[1;49;36m \n-INICIANDO SEU CADASTRO- \033[m')
            os.system('clear')
            alguem.cadastro()
            novosUsuarios.append(alguem)
            iniciar()
        elif int(entrada.get()) == 3:
            principal.destroy()
            os.system('clear')
            definirEvento()
            iniciar()
        elif int(entrada.get()) == 4:
            principal.destroy()
            os.system('clear')
            exibirEvento()
            iniciar()
        elif int(entrada.get()) == 5:
            principal.destroy()
            os.system('clear')
            exibirCalendar()
            iniciar()
        elif int(entrada.get()) == 6:
            pass
        else:
            print('digite um numero de 1 a 6')

    botao = Button(principal, text='enviar', command=btclick)
    botao.place(x=70, y=200)
    principal.mainloop()

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


# Retornar ao inciar
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
# Start
iniciar()