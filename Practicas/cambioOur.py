from datetime import datetime

'''Tiempo militar

Desea convertir la hora de un reloj de 12 horas a un reloj de 24 horas.  Si se le da la hora en un reloj de 12 horas, 
debe mostrar la hora como aparecería en un reloj de 24 horas.

tarea:
  Determine si la hora asignada es AM o PM, luego convierta ese valor a la forma en que aparecería en un reloj de 24 horas.

  Formato de entrada:
  Una cadena que incluye el tiempo, luego un espacio y el indicador de AM o PM.

  Formato de salida:
  Una cadena que incluye la hora en formato de 24 horas (XX: XX)

  Entrada de ejemplo:
  13:15

  Salida de muestra:
  13:15'''


time = "13:22 AM"
time = time.split(':')

hora = time[0]
len(hora)
separarAMPM = time[1].split()
minuto= separarAMPM[0]
ampm= separarAMPM[1]

if len(hora) <= 1:
	hora = '0'+hora

if ampm == 'PM':
	hora = int(hora)
	hora += 12



print ("{}:{}".format(hora, minuto))
