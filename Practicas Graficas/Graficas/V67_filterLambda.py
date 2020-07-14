# '''
# Created on 6 nov. 2019
# 
# @author: jean
# '''
# 
# ## USANDO PALABRAS RESERVADAS LIST, FILTER Y LAMBDA
# 
# numeros=[10,23,65,24,12,763,34,123,750]
# 
# print (list(filter(lambda listaNumero: listaNumero % 2==0, numeros)))


class Empleados():
    
    def __init__(self, nombre, cargo, salario):
        
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        
        return "{} Que Trabaja como {} y tiene un salario de {} $".format(self.nombre, self.cargo, self.salario)
    
    

listaEmpleados=[
    
    Empleados("Jose Manuel", "Director", 3500),
    Empleados("Ana Monse", "Jefe", 3200),
    Empleados("Jose Antonio", "Tecnico", 2800),
    Empleados("Mario Ramirez", "Motorizado", 1500),
    Empleados("Manuel Gonzalez", "Motorizado", 1500),
    
    ] 


salariosAltos=filter(lambda empleado: empleado.salario>3000, listaEmpleados)

for empleadoSalario in salariosAltos:
    print(empleadoSalario)