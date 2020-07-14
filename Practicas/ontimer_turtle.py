from turtle import *
from random import randint

# se puede hacer un juego infantil para adivinar objetos, animales.. mientras mas se acerque a la
# imagen o al parecido menor puntuacion resivira

setup(450, 200, 0, 0)
screensize(300, 150)
title("www.mclibre.org")
hideturtle()
penup()

def punto():
    global randint
    goto(randint(-225, 225), randint(-100, 100))
    dot(10, "black")
    ontimer(punto, 1000)

ontimer(punto, 1000)

mainloop()