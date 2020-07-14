palabra = str(input("Introduce una frase :"))
palabra = palabra.upper().split(' ')
print (' '.join(sorted(palabra)))
