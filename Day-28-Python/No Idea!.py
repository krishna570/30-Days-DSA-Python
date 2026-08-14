import sys

def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
        
    # Parse sizes n and m
    n, m = map(int, input_data[0].split())
    
    # Parse the array elements
    arr = list(map(int, input_data[1].split()))
    
    # Parse sets A and B into Python sets for O(1) lookups
    set_a = set(map(int, input_data[2].split()))
    set_b = set(map(int, input_data[3].split()))
    
    # Calculate final happiness
    happiness = 0
    for num in arr:
        if num in set_a:
            happiness += 1
        elif num in set_b:
            happiness -= 1
            
    print(happiness)

if __name__ == '__main__':
    solve()
