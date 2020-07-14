print("Letra H")
altura = int(input("Altura de la letra H: "))
anchura = int(input("Anchura de la letra H: "))
grosor = int(input("Grosor de la letra H: "))

if altura <= 0 or anchura <= 0 or grosor <= 0:
    print("Los tres valores deben ser positivos.")
elif altura <= grosor + 1:
    print("La altura debe ser al menos dos unidades mayor que el grosor.")
elif anchura <= 2 * grosor:
    print("La anchura debe ser mayor que el doble del grosor.")
elif altura % 2 != grosor % 2:
    print("La altura y el grosor deben ser ambos pares o ambos impares")
else:
    for i in range((altura - grosor) // 2):
        for j in range(grosor):
            print("* ", end="")
        for j in range(anchura - 2 * grosor):
            print("  ", end="")
        for j in range(grosor):
            print("* ", end="")
        print()

    for i in range(grosor):
        for j in range(anchura):
            print("* ", end="")
        print()

    for i in range((altura - grosor) // 2):
        for j in range(grosor):
            print("* ", end="")
        for j in range(anchura - 2 * grosor):
            print("  ", end="")
        for j in range(grosor):
            print("* ", end="")
        print()


### https://www.mclibre.org/consultar/python/ejercicios/ej-ascii-1-soluciones.html