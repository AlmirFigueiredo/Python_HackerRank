def is_palin(number):
    return str(number) == str(number)[::-1]
def check_conditions(n, l):
    if all(number > 0 for number in l):
        return any(is_palin(number) for number in l)
    else:
        return False

n = int(input())
l = list(map(int, input().split()))
print(check_conditions(n, l))
