from tkinter import *

raiz= Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

minombre=StringVar()

nombreLabel=Label(miFrame, text="Nombre: ").grid(row=0, column=0, sticky="e", padx="5", pady="5")
apellidoLabel=Label(miFrame, text="Apellido: ").grid(row=1, column=0, sticky="e", padx="5", pady="5")
edadLabel=Label(miFrame, text="Edad: ").grid(row=2, column=0, sticky="e", padx="5", pady="5")
passwordLabel=Label(miFrame, text="Password: ").grid(row=3, column=0, sticky="e", padx="5", pady="5")

comentariosLabel=Label(miFrame, text="Comentarios: ").grid(row=4, column=0, sticky="e", padx="5", pady="5")


cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, padx="5", pady="5")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1, padx="5", pady="5")

cuadroEdad=Entry(miFrame)
cuadroEdad.grid(row=2, column=1, padx="5", pady="5")

cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=3, column=1, padx="5", pady="5")
cuadroPassword.config(show="*")

textoComentario=Text(miFrame, width=25, height=5)
textoComentario.grid(row=4, column=1, padx="5", pady="5")


scrollvert=Scrollbar(miFrame, command=textoComentario.yview)
scrollvert.grid(row=4, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollvert.set)

def codigoBoton():
    
    minombre.set("Jean Carlo")
    

botonenvio=Button(raiz, text="Enviar", command=codigoBoton)
botonenvio.pack()







raiz.mainloop()

