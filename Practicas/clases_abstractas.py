from abc import ABCMeta, abstractmethod

class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(self): pass
        

class MyBook(Book):
    def __init__(self, title, author,price):
        self.title = title
        self.author = author
        self.price = price
        
    def display(self):
        print ("Title:  ",self.title,"\nAuthor: ",self.author,"\nPrice:  ",self.price)

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()

''' explicacion de clases abstractas:
* Primero se debe importar from abc import ABCMeta abstractmethod para convertir las clases a abstractas en python
* En la clase se escribe objeto Metaclass = ABCMeta
* se crea normalmente el constructor __init__
* luego por cada metodo que se requiere que sea abstracta o poliformica se debe colocar el decorador 
   @abstractmethod (se le coloca pass porque es la que se va a poder modificar desde otra clase)
* luego se crea la proxima clase que hereda en este caso de BOOK
* por cada @abstractmethod se debe crear la funcion que la reemplazara y en esta funcion pasar los 
parametros que se quieran modificar, mostrar.. etc.


'''
    
