from random import randrange

alejandro = ()
beatriz = ()

a1 = randrange(1,6)
a2 = randrange(1,6)

b1 = randrange(1,6)
b2 = randrange(1,6)

alejandro = (a1,a2)
beatriz =(b1,b2)

print(alejandro)
print(beatriz)

if alejandro == beatriz:
    print("Empate")

elif (a1 + a2) - (b1+b2) == 0:
    print ("Empate")

elif a1 - a2 == 0 or b1 - b2 == 0:
    print("Gana Beatriz")

elif b1 - a1 == 0 or b1 - a2 == 0:
    print("Gana Beatriz")

elif b2 - a1 == 0 or b2 - a2 == 0:
    print("Gana Beatriz")

elif alejandro != beatriz:
    print("Gana Alejandro")

