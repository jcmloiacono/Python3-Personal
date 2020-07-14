def area_triangulo(base, altura):
     
    return (base*altura)/2
 
 
triangulo1=area_triangulo(5, 8)
 
triangulo2=area_triangulo(6,2)
 
print(triangulo1)
print(triangulo2)
 
print ("==============EJEMPLO1================")

 
area_triangulo=lambda base,altura: (base*altura)/2
 
print (area_triangulo(7,5))
 
print(area_triangulo(6,4))

print ("================EJEMPLO2======================") 

al_cubo= lambda numero:numero**3

print(al_cubo(13))

print ("==========EJEMPLO3=====================")

destacar_valor=lambda comision: "¡{}! €".format(comision)

comision_Ana=15585

print(destacar_valor(comision_Ana))
