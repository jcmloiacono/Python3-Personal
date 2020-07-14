import pickle
from V40_Serializar_Objeto import * 


fichero_Apertura= open("losCoches","rb")

misCoches=pickle.load(fichero_Apertura)

fichero_Apertura.close()

for c in misCoches:
    print (c.estado())
