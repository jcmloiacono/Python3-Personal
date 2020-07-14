from bs4 import BeautifulSoup
from lxml import etree
from models import Keyword
import requests
import db

def info_variables():
    pass
    ''' LISTA DE VARIABLES UTILIZADAS
    list_menu    (Variable Tipo Lista del a funcion Cargar_keywords, mostrar_keywords)
    text         (Variable Tipo String del a funcion Cargar_keywords, mostrar_keywords)
    keywords     (Variable Tipo Lista del a funcion Cargar_keywords, ) 
    option       (Variable de inicio de programa para seleccionar opcion)
    kw           (Palabra Clave que Introducira el usuario, sirve para introducir y buscar)
    dominio      (Dominio donde el usuario desea buscar la informacion)
    position     (Devolvera el resultado del posicionamiento en el dominio)
    url          (Variable de la funcion Compueba_Keywords)
    resp         (Response del request)
    stop         (Variable solo para darle continuidad al mostrar por pantalla la lista mayor a 20)'''


def agregar_keywords(kw):
    with open('keywords.txt', 'a+') as file:
        file.writelines("\n"+"\n{}".format(kw))


def carga_keywords():
    # aqui se va a abrir el archivo txt y se metera en la base de datos
    contador = 0
    try:
        with open('keywords.txt') as file:
            for line in file:
                line = line.replace('\n','').lower()
                if line != "":
                    keywords = Keyword(line)
                    keywords.save()
                    
                    # aqui voy a llamar a comprobar y me retorna la posicion
                    contador +=1
                    key = Keyword(line, 12)
                    key.update()

    except FileNotFoundError:
        print ("No se encuentra Fichero keywords.txt")

    return Keyword.get_all()

def mostrar_keywords():
    # mostrara palabras claves que se encuentren en el archivo Txt
    keywords = []


    with open('keywords.txt') as file:
        for line in file:
            line = line.replace('\n','')
            if line != "":
                keywords.append(line)

    return keywords


def comprueba_keywords(kw):
    
    #Solicitamos el dominio con la palabra clave que se desea comprobar
    print ("La palabra clave a buscar es: ",kw)
    dominio = input("Introduzca el sitio web donde desea Buscar: ")
    
    # Compueba si la palabra clave se encuentra en google y luego comprobara su posicion
    url = 'https://www.google.com/search?q={}&start=start'.format(kw)
    response = requests.get(url)
    
    #Verifico si la conexion esta activa, osea =200
    if response.status_code != 200:
        print ("Ha ocurrido un error con la conexion!!")
    else:
        print ("Conexion establecida...")
        
        soup = BeautifulSoup(response.text, 'html.parser')
        div_principal = soup.find('div', {'id': 'main'})
        data = div_principal.find_all('div', {'class', 'ZINbbc xpd O9g5cc uUPGi'})
        #data = soup.find_all('div', class_= 'ZINbbc xpd O9g5cc uUPGi')
        cont = 1
        for d in data:
            if dominio not in str(d):
                cont+=1
            else:
                return cont


def keywords_como_lista_de_valores():
    pass

def menu(option):
    #carga las palabras claves iniciar el programa
    keywords = Keyword.get_all()
    dominio="google.com"

    #Mostrara al Usuario el menu de Opciones a escoger
    if option == "1":
        kw = input("Introduzca la palabra clave que desea agregar: ")
        keywords = agregar_keywords(kw)
        print ("Se ha cargado la palabra clave...")
    
    elif option == "2":
        carga_keywords()
    
    elif option == "3":
        keywords = mostrar_keywords()
        if (len(keywords)) > 20: # En caso de que la lista sea mayor a 20 palabras claves
            cont = 0
            for i, j in enumerate(keywords,1):
                if cont <= 19:
                    print (i, j)
                    cont +=1
                else:
                    stop = input ("Presione cualquier tecla para continuar")
                cont = 0
        elif (len(keywords)) < 20: # En caso de que la lista sea menor a 20 palabras claves
            for i, j in enumerate(keywords,1):
                print (i, j)

                
    elif option =="4":
        kw = input("Introduzca la palabra clave que desea buscar: ")
        position = comprueba_keywords(kw)
        if  position == None or position >= 100:
            print ("La palabra clave {} para el dominio {} se encuentra en la posicion {}\n".format(kw,dominio, "+100"))
        else:
            print ("La palabra clave {} para el dominio {} se encuentra en la posicion {}\n".format(kw,dominio, position))
            


    # Se verifica si el usuario no ha introducido una opcion correcta


if __name__ == "__main__":
    #Creando base de datos en caso de que no exista 
    db.Base.metadata.create_all(db.engine)

    # Bucle para el menu donde el usuario coloque su opcion
    i=True
    while i == True:

        print("")
        print("")
        print( "          **  ***   *******  **    **")
        print( "          **  **    **        **  **")
        print( "          ** **     *****       **")
        print( "          **  **    **          **")
        print( "          **  ****  *******     **")
        print("")
        print("")
        print( "**       **  *********  *******   ********    *********")
        print( "**       **  **     **  **    **  **     **   **")
        print( "**   **  **  **     **  ******    **      **  *********")
        print( "**   **  **  **     **  **   **   **     **           **")
        print( "***********  *********  **     ** *******     **********")
        
        # El usuario debera entroducir valores 0,1,2 ò 3
        option = input("\nSeleccione una Opcion:\n [1] – Incluir palabras clave\n [2] – Cargar a BBDD las Keywords\n [3] – Mostrar palabras clave\n [4] - Comprobar palabras clave\n [0] – Salir\n")
        if option.isdigit() == False or option <"0" or option >="5":
            print ("\033[31;48m","No introdujo una opcion valida")
            print ("\033[0;0m")
        elif option == "0":
            print("Hasta Pronto!!\n")
        
            i = False
        else:
            menu(option)
