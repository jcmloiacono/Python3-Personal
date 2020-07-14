from sqlalchemy import create_engine
from sqlalchemy import update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Se crea el motor indicando la cadena o ubicacion de la base datos
engine = create_engine('sqlite:///keyword.sqlite')

# crea el objeto para manejar la sesion de la base de datos
Session = sessionmaker(bind=engine)
session =  Session()



# crea la clase Base de la que hereden los modelos de la aplicacion
Base = declarative_base()