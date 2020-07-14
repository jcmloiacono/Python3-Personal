import sqlite3

conexion = sqlite3.connect("ejemplo.db")

cursor = conexion.cursor()

#cursor.execute("CREATE TABLE usuario (nombre VARCHAR(20), edad INTEGER, email VARCHAR(100)) ")

#cursor.execute("INSERT INTO usuario VALUES ('Hector', 26, 'moasdads@gmal.com')")

cursor.execute("SELECT * FROM usuario")

usuario =cursor.fetchone()
a,b,c = usuario
#print(c)

'''usuario = [
	('Mario', 55, 'masrio@gmasil.com'),
	('Mercedes', 52, 'mercedes@gmail.com'),
	('Fanco', 22, 'franco@gmnasm.com')
]

cursor.executemany("INSERT INTO usuario VALUES (?,?,?)", usuario)
'''
cursor.execute("SELECT * FROM usuario")

usuario = cursor.fetchall()

for i in usuario:
	print(i)

conexion.commit()
conexion.close()