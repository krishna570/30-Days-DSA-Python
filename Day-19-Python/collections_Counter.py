# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter 
n=int(input())
shose = list(map(int,input().split()))
shoe_count=Counter(shose)
customers = int(input())
money=0
for i in range(customers):
    size, price = map(int, input().split())
    if shoe_count[size] > 0:
        money += price
        shoe_count[size]-=1
print(money)
    