from tkinter import *
from tkinter import messagebox

from interfaz.entrada import Parte
from interfaz.registrar import Registrar


class Bienvenida:
    def __init__(self):
        self.ventana=Tk()
        self.ventana.title('Compraventa')
        self.ventana.resizable(False, False)
        self.ventana.geometry('800x800')
        self.ventana.config(bg='gray')
        self.bienvenidolbl = Label(self.ventana, text='BIENVENIDO A LA COMPRAVENTA DE MOTOS',bg='tomato' , font=('Arial', 20))
        self.bienvenidolbl.place(x=100, y=50)

        self.logo = PhotoImage(file='compra.png')
        Label(self.ventana, image=self.logo).place(x=200, y=125)

        #iniciar sesion

        self.registrar_usuario = Label(self.ventana, text='Iniciar sesion',bg='tomato' , font=('Arial', 14))
        self.registrar_usuario.place(x=345, y=360)

        self.nombre = Label(self.ventana, text='Nombre', font=('Arial', 10))
        self.nombre.place(x=280, y=420)
        self.nombre = Entry(self.ventana)
        self.nombre.place(x=345, y=420)

        self.identificacion = Label(self.ventana, text='ID', font=('Arial', 10))
        self.identificacion.place(x=315, y=460)
        self.identificacion = Entry(self.ventana)
        self.identificacion.place(x=345, y=460)

        self.identificacion = Label(self.ventana, text='¿No tienes cuenta?', font=('Arial', 10))
        self.identificacion.place(x=344, y=570)

        # botones

        self.boton1 = Button(self.ventana, text='Ingresar')
        self.boton1.config(font=('Arial',10), command=self.entrada)
        self.boton1.place(x=373, y=510)

        self.boton = Button(self.ventana, text='Registrarme')
        self.boton.config(font=('Arial', 11), command=self.registrar)
        self.boton.place(x=358, y=605)

        self.ventana.mainloop()


    def entrada(self):
        self.barra = self.nombre.get()
        if not self.nombre.get():
            messagebox.showerror('Error','Colocar el nombre de usuario')
        elif len(self.barra)>0 and len(self.barra)<4:
            messagebox.showerror('Error','El nombre de usuario debe ser de mas de 4 caracteres')



    def registrar(self):
        self.ventana.destroy()
        Registrar()

    def entrada(self):
        self.ventana.destroy()
        Parte()



Bienvenida()
