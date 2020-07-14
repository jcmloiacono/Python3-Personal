'''	•	Si  N es extraño, imprima — Weird
	•	Si N es par y está en el rango inclusivo de 2 a 5 , print Not Weird
	•	Si es par y está en el rango inclusivo de 6 to 20 , print Weird
	•	Si es par y mayor que 20 , imprimir Not Weird '''


if __name__ == '__main__':
    N = int(input())


    print('Weird' if (N % 2 == 1 or 6 <= N <= 20) else 'Not Weird')