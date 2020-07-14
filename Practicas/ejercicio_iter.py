a= [1,2,3,4,5,6,7]
g = iter(a)
next(g)

for num in g:
    print(num)
    next(g)
    next(g)
    
    
ac = 8
b = 3

#a,b = b,a
print(ac)


def generator(n):
    i=n
    while i >= 0:
        if i %3 == 0:
            yield i*i
        i -=1

for k in generator(6):
    print (k, sep='', end='')