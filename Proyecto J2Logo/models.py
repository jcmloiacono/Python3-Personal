from sqlalchemy.exc import IntegrityError
from sqlalchemy import Column, Integer, String
import db

class Keyword(db.Base):
    #Se debe llamar la funcion __tablename__ para crear la tabla de la DB
    __tablename__= 'keyword'

    # Al Crear la tabla se le pasan los atributos 
    id = Column(Integer, primary_key=True)
    keywords = Column(String, nullable=False, unique=True)
    posicion = Column(Integer, nullable=True)


    def __init__(self, keywords, posicion=None, contador =None):
    # Se inicia la clase keyword
        self.keywords=keywords
        self.posicion = posicion
        self.contador = contador

    def __repr__(self):
        return  f'Ranking({self.keywords}, {self.posicion})'

    def __str__(self):
        return f'La palabra clave {self.keywords} ranquea en la posicion {self.posicion}'

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except IntegrityError:
            #Si la palabra clave existe se hace Rollback
            #Significa que cierra la transaccion en curso y restaura la sesion limpia
            db.session.rollback()
            print ("Este registro ya existe")

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.update(self)
        db.session.commit()
    #https://kite.com/python/answers/how-to-update-existing-table-rows-in-sqlalchemy-in-python
    #https://leportella.com/tutorial-basico-sqlalchemy.html
    #https://riptutorial.com/es/sqlalchemy/example/6625/actas
    
    @staticmethod
    def get_all():
        return db.session.query(Keyword).all()
    
