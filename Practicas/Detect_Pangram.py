import string

def is_pangram(s):
    cont=0
    s= set(s.lower())
    abc = string.ascii_lowercase
    for i in abc:
        if i in s:
            cont+=1
    
    if len(abc) == cont:
        print (True)
    else:
        print (False)


pangram = "The quick, brown fox jumps over the lazy dog!"
is_pangram2(pangram)



