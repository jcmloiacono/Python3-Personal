'''tarea:
Cree un programa que analice a través de un enlace, extraiga y muestre la ID de video de YouTube.

Formato de entrada
Una cadena que contiene la URL de un video de YouTube. El formato de la cadena puede estar en "https://www.youtube.com/watch?v=kbxkq_w51PM" o en el formato abreviado "https://youtu.be/KMBBjzp5hdc".

Formato de salida:
Una cadena que contiene la identificación de video de YouTube extraída.

Entrada de muestra:
https://www.youtube.com/watch?v=RRW2aUSw5vU

Salida de muestra:
RWW2aUSwvU'''



def extraction_id (text):
    a=reversed(text)
    extractor =""
    cont=0
    
    for i in a:
        cont += 1
        if cont <= 11:
            extractor +=i
    print (extractor[::-1])

extraction_id("https://www.youtube.com/watch?v=kbxkq_w51PM")






