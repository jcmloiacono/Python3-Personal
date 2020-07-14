### RECORRIENDO UNA LISTA CON FOR ##

cuentaLetras=0
letraBuscar="a"


nombres=['Maria', 'Jose','Manuel', 'Ramiro', 'Karina', 'Jean Carlo', 'Sharon', 'Shantal']

agendaRut={
    'Maria':'26167151-1',
    'Manuel':'26167151-2',
    'Ramiro':'26167151-3',
    'Karina':'26167151-4',
    'Jean Carlo':'26167151-5',
    'Sharon':'26167151-6',
    'Shantal':'26167151-7'   
    
    }

palabra= "La casa esta llena de cosas, con las que podemos contar"

#### BUCLE FOR PARA CONTAR CARACTERES DE CADA NOMBRE ####
for caracter in nombres:
    print ((caracter), ("La longitud es: "), (len(caracter)))
    
#### BUCLE FOR PARA IMPRIMIR DATOS EN UN DICCIONARIO DE DATOS ####

for (nombre,rut) in agendaRut.items():
    print (nombre, rut)

#### BUCLE FOR PARA BUSCAR LETRA "A" EN UNA VARIABLE ####

for letra in palabra:
    if letra == agendaRut.get('a'):
        cuentaLetras+=1
    
print("La Cantidad de Letras: ", letraBuscar, "son: ", cuentaLetras)
        