import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()


## UNIQUE SIRVE PARA PONER CAMPO CLAVE ADICIONAL##
miCursor.execute('''
        CREATE TABLE PRODUCTOS( 
        ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        NOMBRE_ARTICULO VARCHAR(50) UNIQUE,  
        PRECIO INTEGER,
        SECCION VARCHAR(20))     
               
''')

productos=[
    
    ("Pelota", 20, "Jugueteria"),
    ("Pantalon", 15, "Ropa"),
    ("Destornillador", 42, "Ferreteria"),
    ("Pantalones", 15, "Ropa"),
    ("Jarron", 45, "Decoracion")    
    
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)


miConexion.commit()

miConexion.close()
