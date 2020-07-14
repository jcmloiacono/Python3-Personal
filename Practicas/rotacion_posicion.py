def rotLeft (a,d):
    print ( a[d:] + a[:d])

def rotRight(a,d):
    result = rotLeft(a, -d)

if __name__ == "__main__":

    nd = [1, 2, 3, 4, 5]
    #nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    #a = list(map(int, input().rstrip().split()))
    a = [1, 2, 3, 4, 5]
    #result = rotLeft(a, d)
    result = rotRight(a, 1)
    
    