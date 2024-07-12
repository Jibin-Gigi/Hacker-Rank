#!/bin/python3

import math
import os
import random
import re
import sys

'''
They will meet if, after njumps, the positions are the same:
    x1 + n * v1 = x2 + n * v2

This can be simplified to:
    x1 - x2 = n * (v2 - v1)

'''

def kangaroo(x1, v1, x2, v2):
    if v1 != v2:
        n = (x2 - x1)/ (v1 - v2)
        if n.is_integer() and n >= 0:
            return 'YES'
    elif x1 == x2:
        return 'YES' 
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
