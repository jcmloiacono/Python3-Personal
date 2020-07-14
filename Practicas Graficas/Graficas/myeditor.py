from tkinter import *
from tkinter import filedialog
from io import open

ruta = "" # La Utilizaremos para almacenar la ruta del fichero

root = Tk()
root.title ('Mi Editor de Texto')

def nuevo():
    global ruta
    mensaje.set("Nuevo Fichero")
    ruta =""
    texto.delete(1.0, END)
    root.title(ruta + " - Mi editor")

def abrir():
    global ruta
    mensaje.set("Abrir Fichero")
    ruta = filedialog.askopenfilename(initialdir='.', 
            filetypes=(("Fichero de Texto", "*.txt"),), # En Windows filetype, en linux filetypes
            title="Abrir un fichero de texto")
    
    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0, END)
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + " - Mi editor")
    
def guardar():
    global ruta
    if ruta != "":
        contenido = texto.get(1.0, 'end-1c')
        fichero = open (ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("El fichero se ha guardado correctamente")
    else:
        guardar_como()
    
def guardar_como():
    global ruta
    mensaje.set("Guardar Fichero Como")
    fichero = filedialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".txt")
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, 'end-1c')
        fichero = open (ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("El fichero se ha guardado correctamente")
    else:
        mensaje.set("Guardado Cancelado")
        ruta = ""

    
menubar= Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="Nuevo", command= nuevo)
filemenu.add_command(label="Abrir..", command= abrir)
filemenu.add_command(label="Guardar", command= guardar)
filemenu.add_command(label="Guardar como..", command=guardar_como)

filemenu.add_separator()

filemenu.add_command(label="Salir", command= root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")


# Caja de Texto Central

texto= Text(root)
texto.pack(fill="both", expand=5)
texto.config(bd=0, padx=6, pady=4, font=("Consolas", 12))

# Monitor Inferior

mensaje = StringVar()
mensaje.set('Bienvenido a tu Editor')
monitor= Label(root, textvar=mensaje, justify='left')
monitor.pack(side='left')

root.config(menu=menubar)
root.mainloop()