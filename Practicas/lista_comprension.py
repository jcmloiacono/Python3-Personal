
num = [0,1,2,3,4,5,6,7,8]
for elemento in num: print(elemento)

s = 'Me tomaría ahora una buena ración de papas al alioli'
codigos = [ord(caracter) for caracter in s]

num = [ num*2   for i in range(10)]

print (codigos)


print (num)

factorial= 7
factorial = lambda x: x == 0 and 1 or x * factorial(x-1)
print (factorial)
