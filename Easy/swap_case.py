def swap_case(s):
    l = list(s)
    for i in range(0, len(l)):
        if l[i].islower():
            l[i] = l[i].upper()
        elif l[i].isupper():
            l[i] = l[i].lower()
    result = ''.join(l)
    return result


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)