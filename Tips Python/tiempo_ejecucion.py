# Tiempo de ejecución en segundos de un script
 
import time
 
inicio = time.time()
 
# Tu código, por ejemplo:
x = 0
for i in range(1000000):
    x += i
 
fin = time.time()
tiempo_total = fin - inicio
 
print(f'El tiempo de ejecución es {tiempo_total}')
