#!/bin/python3

import sys
import math

def is_palindrome(string):
    return string[:] == string[::-1]
    
def check_for_product(num):
    root = int(math.sqrt(num))
    for i in range(root, 99, -1):
        if num % i == 0 and 100 <= num//i <= 999:
            return True
            
    return False
       
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    for num in range(n - 1, 10000, -1):
        if is_palindrome(str(num)) and check_for_product(num):
            print(num)
            break
            
    
    
