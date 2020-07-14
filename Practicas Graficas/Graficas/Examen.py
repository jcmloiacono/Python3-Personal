### ENUNCIADO PARA EJECUTAR PROGRAMA
''' Mi amigo Jorge desea realizar una fiesta vip; pero el año anterior una persona se coló 
utilizando el mismo nombre de otra. Y por eso Jorgue decidió este año que el portero pidiera 
número de documento. Pero es muy difícil para este hombre estar comprobando uno por uno los 
números, entonces entramos nosotros a hacer la magia del programador!!

Mensaje del pedido de Jorge!

El programa deberá permitirle al portero ingresar el número de documento de quien intente entrar
 y comprobar si existe en su lista, y una vez que se le dio un PERMITIDO ENTRAR debe mostrar cuántas 
 personas restan entrar. Si la persona no está en la lista debe informar a seguridad!
 
'''


totalInvitados=0
resultado=0

ListaInvitados={
    "Manuel": 101,
    "Josefina":102,
    "Tomas":103,
    "Jean Carlo":104,
    "Sharon":105,
    "Shantal":106,
    "Karina":107,
    "Samuel":108,
    "Jose":109,
    "Tito":110,
    "Carlos":111,
    "Andrea":112,
    "Sabrina":113,
    "Antonella":114
    }

for x in ListaInvitados:
    resultado+=1

revisionDePersona="Manuel"

if revisionDePersona in ListaInvitados:
    print("Bienvenidos a la Fiesta de Jorge")
    resultado-=1
    print("Restan: ", resultado, " invitados para entrar llegar a la fiesta")
else:
    print("Usted no se Encuentra en la Lista de Invitados")        
    print("Restan por Ingresar a la Fiesta: ", resultado)