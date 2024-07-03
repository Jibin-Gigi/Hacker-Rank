#!/bin/python3

import sys


def even_fibonacci_sum(limit):
    result = 0
    a, b = 1, 2
    
    while b <= limit:
        if b % 2 == 0:
            result += b
        a, b = b, a + b
    
    return result


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(even_fibonacci_sum(n))
