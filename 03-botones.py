from tkinter import Button
from tkinter import Entry
from tkinter import Frame
from tkinter import Label
from tkinter import Tk

valor = None
etiqueta = None
entrada_de_texto = None


def hacer_click():
    global etiqueta
    global entrada_de_texto
    try:
        _valor = int(entrada_de_texto.get())
        _valor = _valor * 5
        etiqueta.config(text=_valor)
    except ValueError:
        etiqueta.config(text="Introduce un número!")


def crear_ventana(app):
    """
    Creación de la ventana principal
    """
    global valor
    global etiqueta
    global entrada_de_texto

    ventana = Frame(app)
    ventana.grid(column=0, row=0, padx=(50, 50), pady=(10, 10))
    ventana.columnconfigure(0, weight=1)
    ventana.rowconfigure(0, weight=1)

    etiqueta = Label(ventana, text="Valor")
    # etiqueta.grid(column=2, row=2)
    etiqueta.grid(column=2, row=2, sticky="WE")

    boton = Button(ventana, text="OK", command=hacer_click)
    boton.grid(column=1, row=1)

    valor = ""
    entrada_de_texto = Entry(ventana, width=10, textvariable=valor)
    entrada_de_texto.grid(column=2, row=1)


def main():
    """
    Función principal
    """
    app = Tk()
    app.title("Aplicación grafica en Python")

    crear_ventana(app)

    app.mainloop()


if __name__ == "__main__":
    main()
