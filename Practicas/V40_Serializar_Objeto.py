import pickle

class Vehiculo():
    
    def __init__(self,marca, modelo):
        
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
        
    def arranca(self):
        self.enmarcha=True
        
    def acelera(self):
        self.acelera=True
        
    def frenar(self):
        self.frena=True
        
    def estado(self):
        print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelera: ", self.acelera,
             "\n Frena: ", self.frena)

coche1=Vehiculo("Mazda", "MX5")

coche2=Vehiculo("SEAT", "Leon") 
 
coche3=Vehiculo("Renault", "Megane")
  
coches=[coche1, coche2, coche3]
  
fichero=open("losCoches", "wb")

pickle.dump(coches, fichero)
  
fichero.close()
  
del (fichero)


