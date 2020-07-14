import turtle 

wn = turtle.Screen()
wn.title("Pong 1.0")
wn.bgcolor("blue")
wn.setup(width = 800, height= 600)
wn.tracer(0)

#marcador
marcador1 = 0
marcador2 = 0

#jugador 1
jugador1 = turtle.Turtle()
jugador1.speed(0)
jugador1.shape("square")
jugador1.color("black")
jugador1.penup()
jugador1.goto(-350,0)
jugador1.shapesize(stretch_wid=5,stretch_len=1)

#jugador 2
jugador2 = turtle.Turtle()
jugador2.speed(0)
jugador2.shape("square")
jugador2.color("black")
jugador2.penup()
jugador2.goto(350,0)
jugador2.shapesize(stretch_wid=5,stretch_len=1)

#pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("black")
pelota.penup()
pelota.goto(0,0)

# movimiento de la pelota
pelota.dx = 3
pelota.dy = -3

#division del tablero
division = turtle.Turtle()
division.color("White")
division.goto(0,400)
division.goto(0,-400)

# marcador
marcador = turtle.Turtle()
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0,260)
marcador.write ("Jugador 1: 0          Jugador 2: 0",align="center", font=("Courier",24,"normal"))


# funciones con el teclado

def j1_arriba():
    y = jugador1.ycor()
    y += 20
    jugador1.sety(y)

def j1_abajo():
    y = jugador1.ycor()
    y -= 20
    jugador1.sety(y)

def j2_arriba():
    y = jugador2.ycor()
    y += 20
    jugador2.sety(y)

def j2_abajo():
    y = jugador2.ycor()
    y -= 20
    jugador2.sety(y)

# conexion con teclado
wn.listen()
wn.onkeypress(j1_arriba, "w")
wn.onkeypress(j1_abajo, "s")

wn.onkeypress(j2_arriba, "Up")
wn.onkeypress(j2_abajo, "Down")




while True:
    wn.update()
    
    #movimiento en pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor()+ pelota.dy)

    # bordes del juego
    if pelota.ycor()> 290:
        pelota.dy *= -1
        
    if pelota.ycor() < -290:
        pelota.dy *= -1
    
    #bordes de punto
    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcador1 +=1
        marcador.clear()
        marcador.write ("Jugador 1: {}          Jugador 2: {}".format(marcador1,marcador2),align="center", font=("Courier",24,"normal"))
    
    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcador2 +=1
        marcador.clear()
        marcador.write ("Jugador 1: {}          Jugador 2: {}".format(marcador1,marcador2),align="center", font=("Courier",24,"normal"))
        
    if ((pelota.xcor()> 340 and pelota.xcor()< 350)
            and (pelota.ycor() < jugador2.ycor () + 50
            and pelota.ycor() > jugador2.ycor() - 50)):
        pelota.dx *= -1
    
    if ((pelota.xcor() < -340 and pelota.xcor()> -350)
            and (pelota.ycor() < jugador1.ycor () + 50
            and pelota.ycor() > jugador1.ycor() - 50)):
        pelota.dx *= -1