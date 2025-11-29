#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isNonTrivialRotation' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def isNonTrivialRotation(s1, s2):
    if s1 == s2:
        return 0
    if s2 in s1+s1:
        return 1
    return 0
    
    # if s1 == s2:
    #     return 0
    # temp = s2[0]
    # if temp in s1:
    #     array1 = s1.split(temp, 1)
    #     l = len(array1[1]) + 1
    #     if array1[1] == s2[1:l]:
    #         return 1
    # return 0
    
    # if s1 == s2:
    #     return 0
    # count = 0
    # for ch in  s2:
    #     if ch in s1:
    #         count += 1
    # if count == len(s2):
    #     return 1    
    # return 0

if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = isNonTrivialRotation(s1, s2)

    print(int(result))
