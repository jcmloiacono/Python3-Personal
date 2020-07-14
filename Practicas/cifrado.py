from string import ascii_lowercase

# VARIABLES UTLIZADAS

llave =10
abc = ascii_lowercase
parametro= ""

'''funcion de cifrado (permite utilizar parametro ="" y variable llave = 10 en 
caso de que el usuario no lo introduzca valores y evitar error)'''

def cifrado(sentencia=parametro, llave=llave):
    resultado= ""
    parametro = sentencia.lower()
    for c in parametro:
        if c in abc:
            resultado += abc[(abc.index(c)+llave)%len(abc)]
        else:
            resultado+=c
    print( resultado )

cifrado('aasdasd', 13)