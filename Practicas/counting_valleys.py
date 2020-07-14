'''Complete la función countingValleys en el editor a continuación. Debe devolver un número 
entero que denote el número de valles que atravesó Gary.

countingValleys tiene los siguientes parámetros:

n : el número de pasos que da Gary
s : una cadena que describe su camino'''




nivel_mar = 0
valle=0

pasos= 12
camino='DDUUDDUDUUUD'

for i in camino:
    if i == 'U':
       nivel_mar+=1
    else:
        nivel_mar-=1
    
    if i == 'U' and nivel_mar==0:
        valle+=1

               
    
print (valle)

