from tkinter import  *

raiz=Tk()

raiz.title("Primera Ventana")

#raiz.resizable(False, True)

raiz.iconbitmap("gato.ico")

#raiz.geometry("650x350")

raiz.config(bg="orange")

miFrame=Frame()

miFrame.pack(fill="y", expand="true")

miFrame.config(bg="red")

miFrame.config(bd="35")

miFrame.config(relief="sunken")

miFrame.config(cursor="pirate")

miFrame.config(width="650", height="350")

raiz.mainloop()

