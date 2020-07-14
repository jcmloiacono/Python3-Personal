''' script que encuentra la diferencia entre numeros que hay desde el mayor hasta el menor en una lista. Ejemplo INPUT : 3 \n 1 2 5'''


class Difference:
    def __init__(self, a):
        self.__elements = a
    
    def computeDifference(self):
        self.maximumDifference = max(self.__elements) - min(self.__elements)

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

