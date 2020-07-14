import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    hora = (s[:2])
    minuto = s[3:5]
    segundo = s[6:8]
    am_pm = s[8:]
    result = ''
    

    if am_pm == 'PM':
        hora = int(hora)
        if hora != 12:
            hora +=12
            if hora == 24:
                hora = '00'
    else:
        if hora == '12':
            hora = '00'

    
    hora = str(hora)
    #result=str(hora)+':'+minuto+':'+segundo
    result=(hora+':'+minuto+':'+segundo)
    return (result)

if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    #f.write(result + '\n')

    #f.close()