from turtle import *

setup(800, 800)
screensize(600, 600)
title("Formas Graficas")
colormode(1)


# penup()
# dot(10, 1, 0, 0)  el dot dibuja un punto 10px, y los colores el colormode 1,0,0
# goto(100, 50) mover el cursor x=100 y=50..
# dot(10,0, 1, 0)
# goto(100, -50)
# pencolor(0, 0, 1)
# goto(50, -50)
# dot(10, 0, 1, 0)
# goto(0,0)
penup()
forward (100)
left(90)

pendown()
fillcolor("Green") #establece el color
begin_fill() # rellenar
forward (200)
left(90)
forward (400)
left(90)
forward(400)
left(90)
forward(400)
left(90)
forward(200)
end_fill() #rellenar





mainloop()

