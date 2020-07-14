from tkinter import *

raiz=Tk()

raiz.title("Selecciones Sus Opciones")

playa=IntVar()
montana=IntVar()
turismo=IntVar()

def opcionesviajes():
    opcionEscogida=""
    
    if(playa.get()==1):
        opcionEscogida+= "\n * Playa"
    
    if(montana.get()==1):
        opcionEscogida+= "\n * Montaña"
    
    if(turismo.get()==1):
        opcionEscogida+="\n * Turismo"
    
    textofinal.config(text=opcionEscogida)
    

foto=PhotoImage(file="w.png")
Label(raiz, image=foto).pack()

frame=Frame(raiz)
frame.pack()

Label(frame, text= "Elige Tus Opciones", width=50).pack()




Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesviajes).pack()
Checkbutton(frame, text="Montaña", variable=montana, onvalue=1, offvalue=0, command=opcionesviajes).pack()
Checkbutton(frame, text="Turismo", variable=turismo, onvalue=1, offvalue=0, command=opcionesviajes).pack()






textofinal=Label(frame)
textofinal.pack()



raiz.mainloop()