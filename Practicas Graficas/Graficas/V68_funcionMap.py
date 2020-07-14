from builtins import map

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
    Empleados("Manuel Gonzalez", "Motorizado", 1500)
    
    ] 

def calculoComision(empleado):
    if empleado.salario<=2800:
    
        empleado.salario=empleado.salario*1.03

    return empleado
    
comisionEmpleados=map(calculoComision, listaEmpleados)

for empleado in comisionEmpleados:
    
    print(empleado)
    
    