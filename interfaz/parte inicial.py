from tkinter import *


class Parte:

    def __init__(self):
        self.ventan = Tk()
        self.ventan.title('Registro de usuario')
        self.ventan.resizable(False, False)
        self.ventan.geometry('800x800')
        self.ventan.config(bg='tomato')
        self.bienvenidolbl = Label(self.ventan, text='Registar usuario', bg='tomato', font=('Arial', 20))
        self.bienvenidolbl.place(x=300, y=50)