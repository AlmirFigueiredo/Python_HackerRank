n = int(input())
shoes = list(map(int, input().split()))
purchases = int(input())
bill = 0
for _ in range(purchases):
    purchase, price = map(int, input().split())
    if purchase in shoes:
        shoes.remove(purchase)
        bill += price
print(bill)