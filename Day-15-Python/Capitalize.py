#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
     word=s.split(" ")
     new=[]
  
     for i in word:
        if i == "":
            new.append("")
        else:
            new.append(i[0].upper() + i[1:])

     return " ".join(new)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
