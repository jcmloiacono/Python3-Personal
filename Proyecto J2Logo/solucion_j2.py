import requests
from bs4 import BeautifulSoup


def aparece_el_dominio(link, dominio):
    encontrado = False
    fin = link.find('&')
    pagina = link[:fin]
    if dominio in pagina:
        encontrado = True
    return encontrado


def comprueba_keywords(kw, dominio):
    continuar = True
    start = 0
    posicion = 1
    encontrado = False
    while continuar and not encontrado:
        parametros = {'q': kw, 'start': start}
        resp = requests.get(f'https://www.google.com/search', params=parametros)
        
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'lxml')
            div_principal = soup.find('div', {'id': 'main'})
            print (div_principal)
            resultados = div_principal.find_all('div', {'class', 'ZINbbc xpd O9g5cc uUPGi'})
            for res in resultados:
                if res.div and res.div.a:
                    if aparece_el_dominio(res.div.a['href'], dominio):
                        encontrado = True
                        break
                    else:
                        posicion += 1
            if not encontrado:
                footer = div_principal.find('footer')
                siguiente = footer.find('a', {'aria-label': 'Página siguiente'})
                if siguiente:
                    start += 10
                    if start == 100:
                        continuar = False
                else:
                    continuar = False
        else:
            continuar = False
    if not encontrado:
        posicion = 100
    return posicion


def carga_keywords():
    keywords = []
    try:
        with open('keywords.txt') as fichero:
            for kw in fichero:
                kw = kw.replace('\n', '')
                keywords.append(kw)
    except FileNotFoundError:
        print('No se encuentra el fichero keywords.txt')
    return keywords


def muestra_keywords(keywords):
    contador = 0
    for kw in keywords:
        print(kw)
        contador += 1
        if contador == 20:
            contador = 0
            input('Mostrar más...')


def muestra_menu():
    print('')
    print('')
    print('-------- Kwranking --------')
    print('')
    print('[1] – Importar palabras clave')
    print('[2] – Mostrar palabras clave')
    print('[3] – Comprobar palabras clave')
    print('[0] – Salir')


def run():
    keywords = []
    dominio = 'python.it'
    while True:
        muestra_menu()
        opcion = input('Selecciona una opción > ')
        opcion = int(opcion)
        if opcion == 0:
            break
        elif opcion == 1:
            keywords = carga_keywords()
        elif opcion == 2:
            muestra_keywords(keywords)
        elif opcion == 3:
            kw = input('Introduzca las palabras clave a comprobar > ')
            posicion = comprueba_keywords(kw, dominio)
            if posicion < 100:
                print(f'Las keywords {kw} se han encontrado en la posición {posicion} para el dominio {dominio}')
            else:
                print(f'De momento, las keywords {kw} no rankean para el dominio {dominio}')
        else:
            print('Opción no válida')

run()