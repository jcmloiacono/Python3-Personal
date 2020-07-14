from tkinter import *

root=Tk()
root.title("Sistema de Gestion")
root.geometry("600x600+400+100")
barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)

archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")


archivoEdicion=Menu(barraMenu, tearoff=0)

archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Pegar")
archivoEdicion.add_command(label="Cortar")


archivoHerramientas=Menu(barraMenu, tearoff=0)

archivoHerramientas.add_command(label="Colores")
archivoHerramientas.add_command(label="Letras Negritas")
archivoHerramientas.add_command(label="Letra Cursiva")


archivoAyuda=Menu(barraMenu, tearoff=0)

archivoAyuda.add_command(label="Acerca De..")
archivoAyuda.add_command(label="Activar Licencia")
archivoAyuda.add_command(label="Buscar Ayuda")


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramienta", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)




root.mainloop()