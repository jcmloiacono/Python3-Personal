'''¡La nueva película "Avengers" acaba de ser lanzada! Hay mucha gente en la taquilla del cine de pie en una gran fila. Cada uno de ellos tiene una sola 100, 50o 25billete de un dólar. Un boleto de "Vengadores" cuesta 25 dollars.'''

def tickets(people):
    cash = []
    cont=len(people)
    num_key=0
    
    for i in people:
        cash.sort()
        if i == 25:
            cash.append(i)
            cont -=1
        elif i == 50:
            if 25 in cash:
                cash.append(i)
                num_key = cash.index(25)
                cash.pop(num_key)
                cont -=1
            else:
                cont+1
        elif i == 100:
            if 25 in cash and 50 in cash:
                cash.append(i)
                num_key = cash.index(25)
                cash.pop(num_key)
                num_key = cash.index(50)
                cash.pop(num_key)
                cont -=1
            elif cash.count(25) == 3 :
                cash.append(i)
                num_key = cash.index(25)
                cash.pop(num_key)
                num_key = cash.index(25)
                cash.pop(num_key)
                num_key = cash.index(25)
                cash.pop(num_key)
                cont -=1
            else:
                cont+=1  
    
    if cont == 0:
        print ("YES")
    else:
        print("NO")
    
    


#tickets([25, 100])

tickets([25, 25, 25,100])
tickets([25, 50, 25, 100, 25, 25, 50, 100, 25, 50, 25, 100, 50, 25])