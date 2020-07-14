array1 = [None]  
array2 = [121, 361, 361, 361, 14641, 20736, 20736, 25921]

if None in array1 or None in array2:
    print (False)
else:
    array1 = list(map(lambda x: x ** 2,array1))
    array1.sort()
    array2.sort()

    print (True if array1 == array2 else False)

