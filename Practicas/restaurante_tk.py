import sqlite3 
from tkinter import *


# raiz del sistema

root = Tk()
root.title("Pizzeria Don Iacono - Menu")
root. resizable(0,0)
root.config(bd=25, relief="raised")

Label(root, text="   Pizzeria Don Iacono   ", fg="darkgreen", font=("Times New Roman", 28, "bold italic")).pack()
Label(root, text="Menu del dia", fg="green", font=("Times New Roman", 23, "bold italic")).pack()

# Separacion de titulos y categorias
Label(root, text="").pack()

conexion = sqlite3.connect("restaurante.db")
cursor =conexion.cursor()

# Buscar las categorias y platos de la Base de datos

categorias = cursor.execute("SELECT * FROM categoria").fetchall()
for categoria in categorias:
	Label(root, text=categoria[1], fg="black", font=("Times New Roman", 20, "bold italic")).pack()

	platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
	for plato in platos:
		Label(root, text=plato[1], fg="gray", font=("Verdana", 15, "italic")).pack()

	#Separacion entre las categorias
	Label(root, text="").pack()

conexion.close()

# Precios del Menu
Label(root, text="12$ (IVA Incl.)", fg="darkgreen", font=("Verdana", 18, "bold italic")).pack(side="right") 
root.mainloop()
