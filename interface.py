from tkinter import*

cor1 = "#993399"

principal = Tk()
principal.title("BEM VINDO AO SEU PLANNER")
principal.configure( background = cor1)
principal.geometry("700x500+200+200")
label1 = Label(text = "1 - LOGIN \n  2 - CADASTRO \n   3 - DEFINIR EVENTO \n        4 - EXIBIR AGENDAMENTO DO EVENTO \n   5 - EXIBIR CALENDARIO \n       6 - INFORMAÇÕES DE USUÁRIO \n-->  ", background = cor1)

label1.place(x = '5', y = '10')

entrada = Entry(principal)
entrada.place( x = '70', y = '140')

  
