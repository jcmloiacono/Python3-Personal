mi_lista = [10, 20, 20, 10, 10, 30, 50, 10, 20]
pares = 0
for num in set(mi_lista):
    pares += mi_lista.count(num) // 2

print(pares)