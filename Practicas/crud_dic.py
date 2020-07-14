def agregar(nombre,edad):
    diccionario = {nombre: edad}

def leer(nombre,edad):
    pass

def actualizar(nombre,edad):
    pass

def elimnar(nombre,edad):
    pass


print ("Que deseas hacer?\n\n1.- Agregar\n2.- Leer\n3.-Actualizar\n4.-Eliminar\n5.-Salir\n")

i=False
diccionario = {}

while i == False:
    opcion = input("introduzca su opcion :")

    if opcion == '1':
        nombre= input("introduce nombre : ")
        edad= input("introduce edad :")
        
        agregar(diccionario)
        
    elif opcion =='2':
        pass
    elif opcion =='3':
        pass
    elif opcion =='4':
        pass
    elif opcion =='5':
        pass