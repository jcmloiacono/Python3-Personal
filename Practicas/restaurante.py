import sqlite3 


def crear_db():

	conexion = sqlite3.connect ("restaurante.db")
	cursor = conexion.cursor()

	try:
		cursor.execute('''CREATE TABLE categoria (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				nombre VARCHAR (100) UNIQUE NOT NULL)''')
	except sqlite3.OperationalError:
		print ("La tabla de categoria ya existe")

	else:
		print ('Se ha creado correctamente la tabla "Categoria"')

	try:	
		cursor.execute('''CREATE TABLE plato (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				nombre VARCHAR(100) UNIQUE NOT NULL,
				categoria_id INTEGER NOT NULL,
				FOREIGN KEY (categoria_id) REFERENCES categoria(id))''')
	except sqlite3.OperationalError:
		print ("La Tabla de platos ya existe")
	else:
		print ('Se ha creado correctamente la tabla "Platos"')



	conexion.close()


def agregar_categoria():
	categoria = input("Introduzca la categoria que desea ingresar:\n > ")

	conexion = sqlite3.connect ("restaurante.db")
	cursor = conexion.cursor()

	try:
		cursor.execute("INSERT INTO categoria VALUES (null, '{}')".format (categoria))
	except sqlite3.IntegrityError:
		print ("La categoria '{}' ya existe".format(categoria))
	else:
		print("La categoria '{}' creada correctamente".format(categoria))

	conexion.commit()
	conexion.close()

def agregar_plato():

	conexion = sqlite3.connect ("restaurante.db")
	cursor = conexion.cursor()

	categoria = cursor.execute("SELECT * FROM categoria").fetchall()
	print("Selecciona una categoria para añadir el plato:\n")
	for i in categoria:
		print ("[{}] {}".format(i[0], i[1] ))

	categoria_usuario = int(input("> "))

	plato = input("Introduce el nombre del nuevo plato: \n >")

	try:
		cursor.execute("INSERT INTO plato VALUES (null, '{}', {})".format (plato, categoria_usuario) )
	except sqlite3.IntegrityError:
		print ("El plato '{}' ya existe".format(plato))
	else:
		print("El plato '{}' se ha creado correctamente".format(plato))

	conexion.commit()
	conexion.close()

def mostrar_menu():

	conexion = sqlite3.connect ("restaurante.db")
	cursor = conexion.cursor()

	categorias = cursor.execute("SELECT * FROM categoria").fetchall()
	for categoria in categorias:
		print (categoria[1])
		platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
		for plato in platos:
			print("\t{}".format(plato[1]))

	conexion.close()

# CREACION DE LA BASE DE DATOS
crear_db()

# MENU DE OPCIONES DEL PROGRAMA

while True:
	print ("\nBienvenidos al gestor del restaurante")
	opcion = input("\nIntroduce una opcion:\n[1] Agregar una categoria\n[2] Agregar un plato\n[3] Mostrar Menu\n[4] Salir del programa\n\n > ")

	if opcion == "1":
		agregar_categoria()
	
	elif opcion == "2":
		agregar_plato()

	elif opcion == "3":
		mostrar_menu()
	
	elif opcion == "4":
		print("Hasta pronto...")
		break

	else:
		print("Opcion Incorrecta")
