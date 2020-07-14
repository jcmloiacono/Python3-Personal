from itertools import combinations

num = [3,8,9,2]

for i in combinations(num, 2):
    
    print ("\033[1;48m",i) #primer grupo \033 codigo escape, segundo grupo es desde el 0 al 8
    # inician los colores 30 llega hasta el 36 poner fondo empieza desde el 40 al 47

print ("\033[0;0m")
