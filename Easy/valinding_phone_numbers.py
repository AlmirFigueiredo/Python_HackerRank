n = int(input())
numbers = []
results = []
for i in range(n):
    numbers.append(input())
for j in range(0, n):
    number = numbers[j]
    if (number[0] == '7' or number[0] == '8' or number[0] == '9') and (len(number) == 10) and (number.isnumeric()):
        results.append('YES')
    else:
        results.append('NO') 
for result in results:
    print(result)

