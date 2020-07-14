cadena = "samm"
repetidas = 0
contador = 0

for i in cadena:
    if cadena.count(i) > 1:
        repetidas +=1
    else:
        contador +=1

if repetidas >= 1:
    print ("Deja Vu")
else:
    print ("Unique")