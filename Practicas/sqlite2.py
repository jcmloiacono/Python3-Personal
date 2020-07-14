import sqlite3

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

cursor.execute('''
	CREATE TABLE usuarios (
		dni VARCHAR(9) PRIMARI KEY, 
		nombre VARCHAR (20),
		edad INTEGER,
		email VARCHAR (40)
)
	''')


usuario = [
	('Mario', 55, 'masrio@gmasil.com'),
	('Mercedes', 52, 'mercedes@gmail.com'),
	('Fanco', 22, 'franco@gmnasm.com')
	('Juan', 19, 'juan@gmail.com')
]

conexion.commit()
conexion.close()