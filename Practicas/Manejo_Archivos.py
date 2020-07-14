from io import open

archivo_texto=open("archivo.txt", "r")

archivo_texto.seek(len(archivo_texto.read())/2)

print (archivo_texto.read())

# r es para leer, w es para escribir, a es append que es leer y escribir
