#!/bin/python3

import math
import os
import random
import re
import sys


def to_binary(n):
    binary = 0
    while n >= 1:
        binary = (binary * 10) + n % 2
        n //= 2
    return binary
    
def consecutive_ones(n):
    num_string = str(to_binary(n))
    max_count = 0
    current_count = 0
    
    for digit in num_string:
        if digit == '1':
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0
    
    return max_count
        
    
            
if __name__ == '__main__':
    n = int(input().strip())
    print(consecutive_ones(n))
