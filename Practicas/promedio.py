cont =0
calificacion=0
resultado=0
while cont < 10:
    cont +=1
    calificacion = int(input("Ingresa una calificación:"))
    resultado +=calificacion

resultado = resultado/10
print(resultado)