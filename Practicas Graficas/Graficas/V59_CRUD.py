import sqlite3
from tkinter import *
from tkinter import messagebox


ventana=Tk()

### FUNCIONES ESPECIFICAS ###

def crearBD():
    miConexion=sqlite3.connect("Usuarios")
    
    miCursor=miConexion.cursor()
    
    try:
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS( 
            ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            NOMBRE VARCHAR(15),
            PASSWORD VARCHAR(50),  
            APELLIDO VARCHAR(15),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100))     
            ''')
        messagebox.showinfo("Software de Gestion", "Base de Datos Creada con Exito")
    except:
        messagebox.showwarning("¡Atención!", "Esta Base de Datos ya se ha creado")
      
def salida():
    valor=messagebox.askokcancel("Salir", "¿Seguro que desea Salir?")
    
    if valor==True:
        ventana.destroy()

def borrarCampos():
    
    datosId.set("")
    datosNom.set("")
    datosPas.set("")
    datosApe.set("")
    datosDir.set("")
    cuadroComentario.delete(1.0, END)
       
def agregarDatos():
    
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    
    datos=datosNom.get(),datosPas.get(),datosApe.get(),datosDir.get(),cuadroComentario.get("1.0", END)
    
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))
    
    
    miConexion.commit()
    messagebox.showinfo("Base de Datos", "Usuario Ingresado Con Exito")
    borrarCampos()
    
def leerDatos():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    
    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID="+ datosId.get())
    
    elUsuario=miCursor.fetchall()
    
    for usuario in elUsuario:
        
        datosId.set(usuario[0]),
        datosNom.set(usuario[1]),
        datosPas.set(usuario[2]),
        datosApe.set(usuario[3]),
        datosDir.set(usuario[4]),
        cuadroComentario.insert("1.0", usuario[5])
    
    miConexion.commit()
          
def actualizarDatos():
    
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    
    
    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE='"+ datosNom.get() +
    "',PASSWORD='"+ datosPas.get()+ 
    "',APELLIDO='"+ datosApe.get()+ 
    "',DIRECCION='"+ datosDir.get()+
    "',COMENTARIOS='" +cuadroComentario.get("1.0",END)+ 
    "' WHERE ID=" + datosId.get())
    
    miConexion.commit()
    messagebox.showinfo("Base de Datos", "Usuario Actualizado Con Exito")
    borrarCampos()
    
def eliminarDatos():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    
    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID="+ datosId.get())
    miConexion.commit()
    
    messagebox.showinfo("Base de Datos", "Usuario Eliminado con Exito")
       
def licencia():
    valor=messagebox.showinfo("SOFTSARE CRUD", "Licencia emitida al Comprador \n"  "No. 3454-22-3321")

def acerca():
    valor=messagebox.showinfo("Acerca de..", "Software de Productividad y Gestion de Datos")    


ventana.geometry("600x500+200+100")
ventana.title("Aplicación CRUD")
barraMenu=Menu(ventana)
ventana.config(menu=barraMenu, width=300, height=300)

datosId=StringVar()
datosNom=StringVar()
datosPas=StringVar()
datosApe=StringVar()
datosDir=StringVar()

ventanaDatos=Frame(ventana)
ventanaDatos.pack(fill="y", expand="True")
ventanaDatos.config(bg="black", bd="80")


## LABEL 
labelTitle = Label(ventanaDatos,text="CRUD REALIZADO EN PYTHON")

labelId=Label(ventanaDatos, text="ID Usuario:", bg="green")
labelId.grid(row=0, column=0,sticky="e", padx="5", pady="5")

labelNombre=Label(ventanaDatos, text="Nombre:", bg="green")
labelNombre.grid(row=1, column=0,sticky="e", padx="5", pady="5")

labelPassword=Label(ventanaDatos, text="Password:", bg="green")
labelPassword.grid(row=2, column=0,sticky="e", padx="5", pady="5")

labelApellido=Label(ventanaDatos, text="Apellido:", bg="green")
labelApellido.grid(row=3, column=0,sticky="e", padx="5", pady="5")

labelDireccion=Label(ventanaDatos, text="Direccion:", bg="green")
labelDireccion.grid(row=4, column=0,sticky="e", padx="5", pady="5")

labelComentario=Label(ventanaDatos,text="Comentarios", bg="green")
labelComentario.grid(row=5, column=0, sticky="e", padx="5", pady="5")

## TEXT BOX

cuadroId=Entry(ventanaDatos, textvariable=datosId)
cuadroId.grid(row=0, column=2, padx="5", pady="5")

cuadroNombre=Entry(ventanaDatos, textvariable=datosNom)
cuadroNombre.grid(row=1, column=2, padx="5", pady="5")

cuadroPassword=Entry(ventanaDatos, textvariable=datosPas)
cuadroPassword.grid(row=2, column=2, padx="5", pady="5")
cuadroPassword.config(show="*")

cuadroApellido=Entry(ventanaDatos, textvariable=datosApe)
cuadroApellido.grid(row=3, column=2,padx="5", pady="5")

cuadroDireccion=Entry(ventanaDatos, textvariable=datosDir)
cuadroDireccion.grid(row=4, column=2, padx="5", pady="5")

cuadroComentario=Text(ventanaDatos, width= 26, height=5)
cuadroComentario.grid(row=5, column=2, padx="5", pady="5")
scrollVert=Scrollbar(ventanaDatos, command=cuadroComentario.yview)
scrollVert.grid(row=5, column=3, sticky="nsew")
cuadroComentario.config(yscrollcommand=scrollVert.set)


### CREACION DE MENUS ###

mnuBBDD=Menu(barraMenu,tearoff=0)

mnuBBDD.add_command(label="Conectar", command=crearBD)
mnuBBDD.add_separator()
mnuBBDD.add_command(label="Salir", command=salida)


mnuBORRAR=Menu(barraMenu,tearoff=0)

mnuBORRAR.add_command(label="Borrar Campos",command=borrarCampos)


mnuCRUD=Menu(barraMenu,tearoff=0)

mnuCRUD.add_command(label="Crear / Create", command=agregarDatos)
mnuCRUD.add_command(label="Leer / Read", command=leerDatos)
mnuCRUD.add_command(label="Actualizar / Update", command=actualizarDatos)
mnuCRUD.add_command(label="Borrar / Delete", command=eliminarDatos)


mnuAYUDA=Menu(barraMenu,tearoff=0)

mnuAYUDA.add_command(label="Licencia", command=licencia)
mnuAYUDA.add_command(label="Acerca de..", command=acerca)

### DATOS DE LA BARRA ### 

barraMenu.add_cascade(label="BBDD", menu=mnuBBDD)
barraMenu.add_cascade(label="BORRAR", menu=mnuBORRAR)
barraMenu.add_cascade(label="CRUD", menu=mnuCRUD)
barraMenu.add_cascade(label="AYUDA", menu=mnuAYUDA)

### BOTONES EN PANTALLA ###

boton1=Button(ventanaDatos, text="CREAR", command=agregarDatos)
boton1.place(x=0, y=300, width=70, height=50)


boton2=Button(ventanaDatos, text="LEER", command=leerDatos)
boton2.place(x=75, y=300, width=70, height=50)

boton3=Button(ventanaDatos, text="UPDATE", command=actualizarDatos)
boton3.place(x=150, y=300, width=70, height=50)

boton4=Button(ventanaDatos, text="ELIMINAR", command=eliminarDatos)
boton4.place(x=225, y=300, width=70, height=50)

### CREACION DE BASE DE DATOS ###


ventana.mainloop()