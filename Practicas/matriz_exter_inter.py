matriz = []
matriz2 =[]
matriz3 =[]
sumaext =0

filas = int(input("Introduzca cantidad de filas: "))
columnas = int(input("Introduzca cantidad de columnas: "))

# Se crea la matriz en cero para que luego se modifiquen los espacios
for m in range(filas):
    matriz.append([0]*columnas)

# Usuario introdice valores
for f in range(filas):
    for c in range(columnas):
        matriz[f][c]= int(input("Introduzca el valor de {},{} : ".format(f, c)))

# suma total de las columnas
for c in range(columnas):
    suma = sum([filas[c] for filas in matriz])
    matriz2.append(suma)

#suma total de las filas de la matriz
for ma in matriz:
    matriz3.append(sum(ma))
    
# suma la primera y ultima columna

sumaext = sum(matriz[columnas-1]+ matriz[0])
sumaext = matriz[0][0] + matriz[columnas-1][filas-1] + matriz[0][columnas-1] + matriz[columnas-1][0]

sumaext = (matriz3[0] + matriz3[len(matriz3)-1]) + (matriz2[0] + matriz2[len(matriz3)-1]) - sumaext


if sumaext > sum(matriz3)-sumaext:
    print ("EXTERIOR")
elif sumaext < sum(matriz3)-sumaext:
    print ("INTERIOR")
else:
    print ("NEUTRO")
