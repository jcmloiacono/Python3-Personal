import math
import sys

# Escriba un programa que pida un código HSL de color y devuelva el código RGB correspondiente.

#CONBINACION DE COLORES HSL

print ("CONVERTIDOR HSL a RGB")
print('Introduzca las componentes HSL:')

matiz_H = float(input("Matiz (entero de 0 a 360):   "))
saturacion_S = float(input("Saturación (decimal de 0 a 1):   "))
luminocidad_L = float(input("Luminocidad (decimal de 0 a 1):   "))


#COMBINACION DE COLORES RGB

# Caculo_Croma

u = abs(2 * luminocidad_L-1)
v = 1 - u
c = v * saturacion_S

float(u)
float(v)
float(c)

h2 = matiz_H / 60

# Calculo_X

y = (h2%2)-1
z = 1 - abs(y)
x = c * z

float(y)
float(z)
float(x)

h3 = math.ceil(h2)

# Cálculo de r1, g1, b1:

if h3  == 1:
    r1 = c
    g1 = x
    b1 = 0
elif h3 == 2:
    r1 = x
    g1 = c
    b1 = 0
elif h3 == 3:
    r1 = 0
    g1 = c
    b1 = x
elif h3 == 4:
    r1 = 0
    g1 = x
    b1 = c
elif h3 == 5:
    r1 = x
    g1 = 0
    b1 = c
elif h3 == 6:
    r1 = c
    g1 = 0
    b1 = x
else:
    r1 = 0
    g1 = 0
    b1 = 0

if r1 <= 0:
    print ('Matiz incorrecto. Inténtelo de nuevo.')
else:
    float(r1)
    float(g1)
    float(b1)

    m = (luminocidad_L - (c / 2))

    rojo_R = r1 + m
    verde_G = g1 + m
    azul_B = b1 + m

    rojo_R = math.ceil(rojo_R * 255 )
    verde_G = math.ceil(verde_G * 255)
    azul_B = math.ceil(azul_B * 255 )

    print ('El color es: R {} , G {}, B {}'.format(rojo_R, verde_G, azul_B))

