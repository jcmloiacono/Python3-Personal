import pickle


class Persona:
    
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print ("Se ha Creado una persona nueva con el nombre de", self.nombre)
        
    
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)
    

class ListaPersonas:
    
    personas=[]
    
    def __init__(self):
        
        listaDePersonas=open("ficheroExterno", "ab+")
        listaDePersonas.seek(0)
       
        try: 
            self.personas=pickle.load(listaDePersonas)
            print("Se Cargaron {} Personas del fichero externo ".format(len(self.personas)))
        
        except:
            print ("El Fichero esta Vacio")
            
        finally:
            listaDePersonas.close()
            del(listaDePersonas) 
    
    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()
        
        
    def mostrarpersona(self):
        for p in self.personas:
            print(p)
            
    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas=open("ficheroExterno", "wb")
        pickle.dump(self.personas,listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)
    
    def mostrarInfoFicheroExterno(self):
        print("La Informacion del Fichero externo es la siguiente: ")
        for p in self.personas:
            print (p)

miLista=ListaPersonas()
persona=Persona("Ramon", "Masculino", 30)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()




