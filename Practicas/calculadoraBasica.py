from _decimal import DivisionByZero

## CALCULADORA EN CONSOLA ###

oper1=0
oper2=0
resultado=0
tipo=0
pregunta=0

   
def suma ():
    resultado=oper1+oper2
    print ("El Resultado de la Suma es: ", resultado)
    
def resta():
    resultado=oper1-oper2
    print ("El Resultado de la Resta es: ", resultado)
 
def multiplicacion():
    resultado=oper1*oper2
    print("El Resultado de la Multiplicacion es: ", resultado)
  
def division():
    resultado=oper1/oper2
    print("El resultado de la Division es: ", resultado)
   
    
    
while True:
    try: 
        oper1= int(input("Ingrese el Primer Numero: "))
        oper2= int(input("Ingrese el Segundo Numero:"))
        print ("Que tipo de operacion desea realizar:\n""1.- Suma \n" "2.- Resta \n" "3.- Multiplicacion \n" "4.- Division")
        tipo= str(input("Introduzca una de las siguientes Opciones: "))
        
    

        if tipo == "1":
            suma()
            
        elif tipo == "2":
            resta()
            
        elif tipo == "3":
            multiplicacion()
            
        elif tipo == "4":
            division()
 
        else:
            print("Has Ingresado una opcion no permitada")
    except ZeroDivisionError:
        print ("No es posible realizar divisiones entre Cero '0'")
    except:
        print("Error!!!")    
        tipo ="?"
    finally:
        print("Gracias por Usar Nuestro programa, Lo intentaremos de Nuevo")
