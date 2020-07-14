from tkinter import *

root=Tk()

miFrame=Frame(root, width=800, height=800)

miFrame.pack()

miImagen=PhotoImage(file="giphy.gif")

Label(miFrame, image=miImagen).place(x=100, y=200)



root.mainloop()