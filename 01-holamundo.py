from tkinter import Button
from tkinter import Label
from tkinter import Tk

app = Tk()

app.title("Aplicación grafica en Python")
etiqueta = Label(app, text="Hola Mundo")
boton = Button(app, text="OK")

etiqueta.pack()
boton.pack()
app.mainloop()
