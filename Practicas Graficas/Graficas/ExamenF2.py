### ENUNCIADO PARA EJECUTAR PROGRAMA
# ''' Mi amigo Jorge desea realizar una fiesta vip; pero el año anterior una persona se coló 
# utilizando el mismo nombre de otra. Y por eso Jorgue decidió este año que el portero pidiera 
# número de documento. Pero es muy difícil para este hombre estar comprobando uno por uno los 
# números, entonces entramos nosotros a hacer la magia del programador!!
# 
# Mensaje del pedido de Jorge!
# 
# El programa deberá permitirle al portero ingresar el número de documento de quien intente entrar
#  y comprobar si existe en su lista, y una vez que se le dio un PERMITIDO ENTRAR debe mostrar cuántas 
#  personas restan entrar. Si la persona no está en la lista debe informar a seguridad!
#  
# '''
# 

PPr=0
Res=0
 
JorgeLista={

'Manuel':419,
'Josefina':410,
'Tomas':411,
'Jean Carlo':412,
'Sharon':413,
'Shantal':414,
'Karina':415,
'Samuel':416,
'Jose':417,
'Tito':418,
'Carlos':421,
'Andrea':420,
'Sabrina':423,
'Antonella':424
}

ListaIngresados={}
 
for (k) in iter(JorgeLista.items()):
    PPr = PPr + 1
  
     
while True:
    try:
        dni= int(input("Introduzca Su Id:"))
        for(k, v) in iter(JorgeLista.items()):
            if v == dni and PPr != 0:
                PPr= PPr-1
                print(("Bienvenido") , (k),  (" a la Fiesta de Jorge"))
                print(("Quedan por Ingresar: "), (PPr), ("invitados"))
                ListaIngresados[k]=dni
                del JorgeLista[k]
                break
                
        if PPr<=0:
            
            print("Todos los Invitados estan en la Fiesta.. No hay mas accesos")
        
          
        if v != dni:
            
            ### CREO QUE ACA PUDIESE BUSCAR EN EL DICCIONARIO SI YA INGRESO ###
            print ("Usted no es Invitado de la fiesta o Ya Ingreso!!!.. Seguridad!!")
    except:
        print("No ha Ingresado una Identificacion Valida")
         


