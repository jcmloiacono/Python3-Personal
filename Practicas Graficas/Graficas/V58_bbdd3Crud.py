import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()


miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='Ropa'")

#### READ
# productos=miCursor.fetchall()
# print(productos)

#### UPDATE

# miCursor.execute("UPDATE PRODUCTOS SET PRECIO= 30 WHERE NOMBRE_ARTICULO='Pelota'")

#### DELETE

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")




miConexion.commit()

miConexion.close()
