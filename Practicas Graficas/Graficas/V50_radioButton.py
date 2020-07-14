from tkinter import *


raiz=Tk()

varOption=IntVar()


def imprimir ():
    
    #print(varOption.get())
    
    if varOption.get()==1:
        etiqueta.config(text="Su Opcion es: Masculino")
    
    elif varOption.get()==2:
        etiqueta.config(text="Su Opcion es: Femenino")
    
    else:
        etiqueta.config(text="Su Opcion es: Empresa")
    
Label(raiz, text="Escoja su Opcion: ").pack()



Radiobutton(raiz, text="Masculino", variable=varOption, value=1, command=imprimir)
Radiobutton.grid(row=0, column=0)
Radiobutton.pack()


Radiobutton(raiz, text="Femenino", variable=varOption, value=2, command=imprimir).pack()

Radiobutton(raiz, text="Empresa", variable=varOption, value=3, command=imprimir).pack()


etiqueta=Label(raiz)

etiqueta.pack()












raiz.mainloop()