import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor()

######## ESTA COMENTADO PARA EVITAR ERROR AL CREAR BBDD #########
'''# CREAR TABLA======================
miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

 LLENAR TABLA=====================
miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

 INCLUIR VARIOS PRODUCTOS CON UNA TUPLA====================
 variosProductos=[
     
     ("Camiseta", 10, "Deportes"),
     ("Jarron", 90, "Ceramicas"),
     ("Camion", 20, "Juguetes")
     
       
     ]
 
 miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", variosProductos)
'''

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall()

for producto in variosProductos:
    print("El Nombre del Articulo: ", producto[0], "Seccion: ", producto[2])


miConexion.commit()

miConexion.close()
