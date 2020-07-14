def jumpingOnClouds(c):
    i = count_jumps = 0
    length = len(c)

    while i < length - 1:
        if i < length - 2 and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        count_jumps += 1

    print( count_jumps)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = 7

    c = [0, 0, 1, 0, 0, 1, 0]

    result = jumpingOnClouds(c)

    #fptr.write(str(result) + '\n')

    #fptr.close()
