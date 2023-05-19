from tkinter import *

class Parte:
    def __init__(self):
        self.ventanas = Tk()
        self.ventanas.title('RHM Compraventa de motos')
        self.ventanas.resizable(False, False)
        self.ventanas.geometry ('800x800')
        self.ventanas.config(bg='firebrick4')
        self.bienvenidolbl = Label(self.ventanas, text='RHM Compraventa de motos', bg='white', font=('Arial Black', 20))
        self.bienvenidolbl.place(x=189, y=50)

        self.logo = PhotoImage(file='compra.png')
        Label(self.ventanas, image=self.logo).place(x=200, y=125)

        self.opciones = Label(self.ventanas, text='Opciones', bg='firebrick4', font=('Segoe UI Black', 30))
        self.opciones.config(fg='white')
        self.opciones.place(x=315, y=360)



        # botones

        self.boton1 = Button(self.ventanas, text='Filtrar busqueda por categoria')
        self.boton1.config(font=('Arial', 10), width=23, height=2)
        self.boton1.place(x=310, y=460)

        self.boton2 = Button(self.ventanas, text='Mostrar catalogo global')
        self.boton2.config(font=('Arial', 10), width=23, height=2)
        self.boton2.place(x=90, y=460)

        self.boton3 = Button(self.ventanas, text='Ver carrito')
        self.boton3.config(font=('Arial', 10), width=23, height=2)
        self.boton3.place(x=530, y=460)
    #----------------------------------------------------------------------------
        self.boton4 = Button(self.ventanas, text='Agregar moto al carrito')
        self.boton4.config(font=('Arial', 10), width=23, height=2)
        self.boton4.place(x=310, y=540)

        self.boton5 = Button(self.ventanas, text='Mostrar informacion de moto')
        self.boton5.config(font=('Arial', 10), width=23, height=2)
        self.boton5.place(x=90, y=540)

        self.boton6 = Button(self.ventanas, text='Eliminar item carrito')
        self.boton6.config(font=('Arial', 10), width=23, height=2)
        self.boton6.place(x=530, y=540)
    # ----------------------------------------------------------------------------
        self.boton7 = Button(self.ventanas, text='Ver mi catalogo')
        self.boton7.config(font=('Arial', 10), width=23, height=2)
        self.boton7.place(x=310, y=620)

        self.boton8 = Button(self.ventanas, text='Comprar carrito')
        self.boton8.config(font=('Arial', 10), width=23, height=2)
        self.boton8.place(x=90, y=620)

        self.boton9 = Button(self.ventanas, text='Registrar moto')
        self.boton9.config(font=('Arial', 10),width=23, height=2)
        self.boton9.place(x=530, y=620)
    # ----------------------------------------------------------------------------
        self.salir = Button(self.ventanas, text='Salir')
        self.salir.config(font=('Arial', 10), command=self.cerrar, width=23, height=2)
        self.salir.place(x=310, y=700)

        self.ventanas.mainloop()

    def cerrar(self):
        self.ventanas.destroy()
