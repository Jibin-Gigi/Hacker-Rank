#!/bin/python3

import sys

def sum_of_multiples(n,x):
    k = ( n - 1 ) // x
    return x * k * (k + 1) // 2
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result = sum_of_multiples(n,3) + sum_of_multiples(n,5) - sum_of_multiples(n,15)
    print(result)


'''
The formula for the sum of the first k multiples of x is given by:
    Sum =  x *  (k * ( k + 1) ) / 2
    
    where k = ( n - 1 ) / x
'''