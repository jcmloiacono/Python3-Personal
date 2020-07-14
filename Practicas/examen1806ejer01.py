'''Escriba un programa que pida tres números positivos cada vez más grandes 
y que diga qué números son múltiplos de otros.'''

print ("DETECTOR DE MÚLTIPLOS \nEscriba tres números enteros crecientes \nLe indicaré si alguno es múltiplo de otro.")

num1 = int(input("Primer número:"))

num2 = int(input("Segundo número:"))
if num2 <= num1:
    print ("Por favor, escriba números crecientes.")

num3 = int(input("Tercer número:"))

if num3 <= num1:
     print ("Por favor, escriba números crecientes.")



resul1_2 = num2 % num1 
resul3_1 = num3 % num1 
resul3_2 = num3 % num2 

if resul1_2 == 0 and  resul3_1 == 0:
    print("{} y {} son múltiplo de {}.".format(num3,num2, num1))
    
elif resul1_2 == 0 and resul3_1 != 0:
    print("{} es múltiplo de {}.".format(num2,num1))

elif resul3_1 == 0 and resul3_2 != 0:
    print("{} es múltiplo de {}.".format(num3,num1))

elif resul3_1 != 0 and resul3_2 == 0:
    print("{} es múltiplo de {}.".format(num3,num2))
else:
    print("Ningún número es múltiplo de otro.")