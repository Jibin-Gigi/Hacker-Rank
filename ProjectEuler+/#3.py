#!/bin/python3

import sys


def largest_prime_factor(n):
    largest_factor = n
    
    while n % 2 == 0:
        largest_factor = 2
        n //= 2
        
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest_factor = factor
            n //= factor
        factor += 2
        
    if n > 2:
        largest_factor = n
           
    return largest_factor
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(largest_prime_factor(n))
    
    
