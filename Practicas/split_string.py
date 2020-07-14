def solution(s):
    temp=''
    lista =[]
    for i in s:
        temp +=i
        if len(temp) == 2:
            lista.append(temp)
            temp =""
            
    if len(temp) == 1:
        temp += "_"
        lista.append(temp)
    
    print (lista)

import re
## EXPRESIONES REGULARES
def solution(s):
    return re.findall(".{2}", s + "_")


solution("")