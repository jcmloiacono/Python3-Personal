import pickle

# lista_nombre=["Pedro", "Ana", "Maria", "Isabel"]
#  
# fichero_binario=open("lista_nonmbre", "wb") # White Binary
#  
# pickle.dump(lista_nombre, fichero_binario)
#  
# fichero_binario.close()
#  
# del (fichero_binario)


fichero=open("lista_nonmbre", "rb") # read binary

lista=pickle.load(fichero)

print(lista)
