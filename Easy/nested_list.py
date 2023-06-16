n = int(input())
main_list = [[input(), float(input())] for i in range(n)]
numbers_list = [main_list[i][1] for i in range(n)]
sorted_numbers = sorted(numbers_list)
min_value = sorted_numbers[0]
second_min_value = None
for j in range(1, n):
    if sorted_numbers[j] == min_value:
        continue
    else:
        second_min_value = sorted_numbers[j]
        break
names = []
for j in range(0, n):
    if numbers_list[j] == second_min_value:
        names.append(main_list[j][0])
names.sort()
for name in names:
    print(name)
        

