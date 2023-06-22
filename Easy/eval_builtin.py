x, correct_result = map(int, input().split())
expression = input()
my_result = eval(expression)
print(my_result == correct_result)