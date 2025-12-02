#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'generateAngleBracketSequences' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER n as parameter.
#

def generateAngleBracketSequences(n):
    result = []
    sequence = []
    
    def backtracker(open_count, close_count):
        if len(sequence) == 2*n:
            result.append("".join(sequence))
            return
        if open_count < n:
            sequence.append('<')
            backtracker(open_count + 1, close_count)
            sequence.pop()
        if close_count < open_count:
            sequence.append('>')
            backtracker(open_count, close_count + 1)
            sequence.pop()
    
    backtracker(0, 0)
    return result

if __name__ == '__main__':
    n = int(input().strip())

    result = generateAngleBracketSequences(n)

    print('\n'.join(result))
