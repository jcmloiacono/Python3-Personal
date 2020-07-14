# def binary(num):
#     n=0
#     cont=0
#     if num[0] == "1":
#         cont+=1
#     try:
#         for i in num:
#             n+=1
#             if i == num[n]:
#                 cont +=1
#     except: IndexError
#     print (cont)


# if __name__ == "__main__":
#     num = int(input("Introduzca un Numero Entero "))
#     num= list(bin(num))
#     num.pop(0)
#     num.pop(0)
#     binary(num)


#### FORMA SIN ERRORES ####

def binary(num):
    result = len(max(num))
    print (result)


if __name__ == "__main__":
    num = int(input("Introduzca un Numero Entero "))
    num =bin(num)[2:].split('0')
    binary (num)


''' explicacion del ejercicio: dado un numero entero Base 10, convertirlo en binario Base 2
y verificar la cantidad de numeros 1 consecutivos.

** no era necesaria la funcion 
L31 > solicita al usuario ingresar numero entero
L32 > el numero entero es convertido en binario con funcion BIN y como el numero binario
      inicia con 1b... se usa [2:] para que lea los caracteres del 2 en adelante, luego se
      usa Split para eliminar todos los "0" creando una lista y separando los numeros 11 
      y 1 [11, 1, 11, 11] EJEMPLO
L33 > llamamos a la funcion
L26 > pasamos a la variable result la cantidad de veces con LEN que esta el numero max
L27 > al final imprimimos cuantos numeros 11 hay en la lista
'''