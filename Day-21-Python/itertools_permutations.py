# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s, r = input().split()

for p in sorted(list(permutations(s, int(r)))):
    print("".join(p))
