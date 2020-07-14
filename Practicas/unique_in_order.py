def unique_in_order(iterable):
    result=[]
    temp = None
    
    for i in iterable:
        if i != temp:
            result.append(i)
        temp = i
        
    print (result)

unique_in_order('AAAABBBCCDAABBB') # ['A','B','C','D','A','B'])
unique_in_order('12341')
unique_in_order('AA')
unique_in_order('AAD')