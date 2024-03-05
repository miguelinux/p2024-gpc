from tkinter import Button
from tkinter import Label
from tkinter import Tk


def main():
    """
    Función principal
    """
    ventana = Tk()
    ventana.title("Aplicación grafica en Python")

    etiqueta = Label(ventana, text="Hola Mundo")
    boton = Button(ventana, text="OK")

    etiqueta.pack()
    boton.pack()

    ventana.mainloop()


if __name__ == "__main__":
    main()
