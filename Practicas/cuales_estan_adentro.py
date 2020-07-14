array1 = ["duplicates"] 
array2 = ['duplicates', 'duplicates']
r =[]



for i in array1:
    for j in array2:
        i.join (array2)
        if i.lower() in j.lower():
            r.append(i)
            break
r.sort()

print (r)


