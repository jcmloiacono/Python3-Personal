
calificaciones = [10, 10, 8, 7, 9]
alumnos = ['Eduardo', 'Fernando', 'Mariana', 'Raquel', 'Santiago']

for i, j in zip(calificaciones, alumnos):
    print ("{} tiene una calificacion de: {}".format(j, i))