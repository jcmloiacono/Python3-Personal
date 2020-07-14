cadena = input() 
print ("Deja Vu" if any(cadena.count(l)>1 for l in cadena) else "Unique")

