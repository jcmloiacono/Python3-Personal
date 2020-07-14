

def sumatoria(number):
    if number == 1:
        return 1
    else:
        return number + sumatoria(number-1)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci (number1):
    if number1 <= 1:
        return 1
    else:
        return fibonacci(number1-1) + fibonacci(number1-2)
    return 1 if number1 == 1 else fibonacci(number1-1) + fibonacci(number1-2)


num = int (input("numero de la sumatiria "))
n = int ( input("numero del factorial "))
numero1 = int (input("numero del fibonacci "))

print (sumatoria(num))
print(factorial(n))
print(fibonacci(numero1))
