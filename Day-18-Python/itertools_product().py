# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product


A = list(map(int, input().split()))
B = list(map(int, input().split()))


cartesian_product = list(product(A, B))


print(*cartesian_product)
