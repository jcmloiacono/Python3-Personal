from string import ascii_letters

def alphabet_position(text):
    text= text.lower()
    lista =ascii_letters[:26]
    lista2 = ""
    
    for i in text:
        cont=1
        for j in lista:
            if i != j:
                cont+=1
            elif i ==j:
                lista2+=" "+ str(cont)
    return (lista2[1:])
    

if __name__ == "__main__":

    print (alphabet_position(str(input())))