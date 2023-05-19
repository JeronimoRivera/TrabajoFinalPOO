from tkinter import *


class Registrar:
    def __init__(self):
        self.ventanas = Tk()
        self.ventanas.title('Registro de usuario')
        self.ventanas.resizable(False, False)
        self.ventanas.geometry ('800x800')
        self.ventanas.config(bg='tomato')
        self.bienvenidolbl = Label(self.ventanas, text='Registar usuario', bg='tomato', font=('Arial', 20))
        self.bienvenidolbl.place(x=300, y=50)


        self.logo = PhotoImage(file='compra.png')
        Label(self.ventanas, image=self.logo).place(x=200, y=125)

        self.registrar_usuario = Label(self.ventanas, text='Registrar', bg='tomato', font=('Arial', 14))
        self.registrar_usuario.place(x=365, y=360)

        self.nombre = Label(self.ventanas, text='Nombre', font=('Arial', 10))
        self.nombre.place(x=280, y=420)
        self.nombre = Entry(self.ventanas)
        self.nombre.place(x=345, y=420)

        self.identificacion = Label(self.ventanas, text='ID', font=('Arial', 10))
        self.identificacion.place(x=315, y=460)
        self.identificacion = Entry(self.ventanas)
        self.identificacion.place(x=345, y=460)

        self.celular = Label(self.ventanas, text='Celular', font=('Arial', 10))
        self.celular.place(x=290, y=500)
        self.celular = Entry(self.ventanas)
        self.celular.place(x=345, y=500)

        #boton

        self.boton1 = Button(self.ventanas, text='Crear cuenta')
        self.boton1.config(font=('Arial', 10), command=self.volver)
        self.boton1.place(x=364, y=540)

        self.ventanas.mainloop()

    def volver(self):
        self.ventanas.destroy()
        from interfaz.interfazinicial import Bienvenida
        Bienvenida()
