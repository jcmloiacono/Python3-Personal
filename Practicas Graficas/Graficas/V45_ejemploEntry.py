from tkinter import *

raiz= Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()


nombreLabel=Label(miFrame, text="Nombre: ").grid(row=0, column=0, sticky="e", padx="5", pady="5")
apellidoLabel=Label(miFrame, text="Apellido: ").grid(row=1, column=0, sticky="e", padx="5", pady="5")
edadLabel=Label(miFrame, text="Edad: ").grid(row=2, column=0, sticky="e", padx="5", pady="5")
passwordLabel=Label(miFrame, text="Password: ").grid(row=3, column=0, sticky="e", padx="5", pady="5")


cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0, column=1, padx="5", pady="5")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1, padx="5", pady="5")

cuadroEdad=Entry(miFrame)
cuadroEdad.grid(row=2, column=1, padx="5", pady="5")

cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=3, column=1, padx="5", pady="5")
cuadroPassword.config(show="*")


raiz.mainloop()

