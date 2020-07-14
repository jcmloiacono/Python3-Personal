from tkinter import *

ventana=Tk()
ventana.geometry("600x600+200+100")
ventana.title("Menus")

barraMenu=Menu(ventana)

mnuArchivo=Menu(barraMenu)

mnuArchivo.add_command(label="Abrir")
mnuArchivo.add_command(label="Nuevo")
mnuArchivo.add_command(label="Guardar")
mnuArchivo.add_command(label="Salir")

barraMenu.add_cascade(label="Archivo", menu=mnuArchivo)

ventana.config(menu=barraMenu)

ventana.mainloop()
