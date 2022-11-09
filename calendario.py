from tkinter import *
from tkcalendar import Calendar
cor1 = "#993399"

def calendario():
    # Import Required Librar
   
  # Create Object
  root = Tk()
   
  # Set geometry
  root.geometry("400x400")
  root.configure(background = cor1)
   
  # Add Calendar
  cal = Calendar(root, selectmode = 'day',
                 year = 2020, month = 5,
                 day = 22)
   
  cal.pack(pady = 20)
   
  def grad_date():
      date.config(text = "Selected Date is: " + cal.get_date())
   
  # Add Button and Label
  Button(root, text = "Get Date",
         command = grad_date).pack(pady = 20)

  def bt_click():
    root.destroy()
    
  botao=Button(root, text = 'voltar', command = bt_click )
  botao.place(x=100, y = 300)
   
  date = Label(root, background= cor1, text = "")
  date.pack(pady = 20)
   
  # Execute Tkinter
  root.mainloop()