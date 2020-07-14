from turtle import *

setup(500,500)
shape("turtle")
color("green")

def rectangulo(px, py, ancho, alto):
    penup()
    goto(px + ancho / 2 , py + alto / 2)
    seth(180) # puede ser tambien left (set heading)
    pendown()
    forward(ancho)
    left(90)
    forward(alto)
    left(90)
    forward(ancho)
    left(90)
    forward(alto)

def poligonos(px, py, radio,  lados):
    penup()
    goto(px, py - radio)
    #pendown() 
    circle(radio)
    
    angulo = 360 / lados
    vertices= []
    
    for i in range(lados):
        penup()
        goto(px,py)
        #pendown()
        
        seth(angulo*i+1)
        forward(radio)
        vertices.append(pos())
        
        # Nos posicionamos en la coordenada del primer vertice
        penup()
        goto(vertices[0])
        pendown()
        
        # y hacemos que la tortuga se mueva a cada uno de ellos
        
        for v in vertices:
            goto(v)
        
        
    goto(vertices[0])



poligonos (0,0,100,7)

#rectangulo(0,0,400,300)
#rectangulo(0,0,380,280)
#rectangulo(0,0,360,260)

mainloop()