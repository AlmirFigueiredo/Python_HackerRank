def solve(s):
    l = list(s)
    l[0] = l[0].upper()
    for i in range(1, len(l)):
        if l[i-1].isspace():
            l[i] = l[i].upper()
    result = ''.join(l)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
