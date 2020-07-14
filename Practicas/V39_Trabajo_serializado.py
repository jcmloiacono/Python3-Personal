import pickle
from _pickle import dump
from test.test_bytes import BytesAsStringTest

lista_nombre= ["Pedro", "Ana", "Maria", "Isabel", "Rafael"]

fichero_binario=open("lista_nombre", "wb")

pickle.dump(lista_nombre,fichero_binario)

fichero_binario.close()


fichero=open("lista_nombre", "rb")

lista=pickle.load(fichero)

print (lista)

