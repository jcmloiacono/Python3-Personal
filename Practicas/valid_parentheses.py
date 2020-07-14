def valid_parentheses(string):
    cont= 0
    string2=""
    
    for s in string:
        if s == '(' or s == ')':
            string2+=s

    for i in string:
        if i == '(':
            cont+=1
        elif i == ')':
            cont-=1
    
    if string2[0] == ')' or string2[-1] == '(':
        print (False)
    elif len(string) == 0 or cont == 0:
        print (True)
    elif cont != 0:
        print (False)


valid_parentheses("() ( ( )) ( ()) ()()() ((()))")

valid_parentheses("())(")