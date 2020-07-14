from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'es_ES.ISO8859-15')

def formato_fecha(agno,mese, giorno):
    fecha = datetime(agno,mese,giorno)
    
    print (fecha.strftime('%d de %B del %Y'))
    


formato_fecha(2015, 5, 7)

