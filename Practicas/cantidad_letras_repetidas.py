palabra = "AaBbCcDdFfHhIiJjKkLl"
palabra = palabra.lower()
palabra2 =set(palabra)  
cont=0

for i in palabra2:
    if palabra.count(i) >=2:
        cont += 1
    
print (cont)