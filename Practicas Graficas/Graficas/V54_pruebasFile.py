from tkinter import *
from tkinter import filedialog

root=Tk()

def abreFichero():
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="Users.jean.Desktop", filetypes=(("Ficheros de Excel","*.xlsx"),
    ("Ficheros de Texto", "*.txt"),("Todos Los Archivos", "*.*")))
    
    print(fichero)
    



Button (root, text="Abrir Fichero", command=abreFichero).pack()









root.mainloop()