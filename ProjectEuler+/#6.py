#!/bin/python3

import sys

def sum_square_difference(n):
    num_sum, square_sum = 0, 0
    
    for i in range(1, n+1):
        num_sum += i
        square_sum += i**2
        
    return abs(square_sum - (num_sum ** 2))

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum_square_difference(n))
