def split_and_join(line):
    l = line.split()
    result = '-'.join(l)
    return result
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)