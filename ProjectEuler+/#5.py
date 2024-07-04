#!/bin/python3

import sys
from math import lcm

def smallest_multiple(n):
    result = 1
    for i in range(2, n+1):
        result = lcm(result, i)
    return result
      

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(smallest_multiple(n))
