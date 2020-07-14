def palindromo(sentencia):
    invertida = sentencia [::-1]
    invertida= invertida.replace(" ", "")
    invertida = invertida.lower()
    
    sentencia = sentencia.lower()
    sentencia = sentencia.replace(" ", "")
    if sentencia == invertida:
        print(True)
    else:
        print(False)




palindromo('Super palindromo')