'''
Created on 31 oct. 2019

@author: jean
'''

finbucle=True
salida=0


while finbucle:
    print( " 1.- Naranja \n" ,"2.- Manzana \n", "3.- Pera")
    opcion=input("Introduzca una Opción:")
   
        
    if opcion == "1":
        print ("has escogido Naranja")
        print("\n")
        salida=input("Desea Salir? "+ "\n Si = 1 \n No = 2")
    
        if salida == "1":
            finbucle=False
        else:
            finbucle=True
                           
    elif opcion == "2":
        print("has escogio Manzana")
        print("\n")
        salida=input("Desea Salir? "+ "\n Si = 1 \n No = 2")
    
        if salida == "1":
            finbucle=False
        else:
            finbucle=True
            
    elif opcion == "3":
        print("has escogido Pera")
        print("\n")
        salida=input("Desea Salir? "+ "\n Si = 1 \n No = 2")
    
        if salida == "1":
            finbucle=False
        else:
            finbucle=True
            
    else:
        print ("No has colocado ninguna opcion")
        print("\n") 
        
    