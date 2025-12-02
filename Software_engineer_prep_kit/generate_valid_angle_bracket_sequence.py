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
    
    def backtracker(string, open_count, close_count):
        if len(string) == 2*n:
            result.append(string)
            return
        if open_count < n:
            backtracker(string + '<', open_count + 1, close_count)
        if close_count < open_count:
            backtracker(string + '>', open_count, close_count + 1)
    
    backtracker('', 0, 0)
    return result

if __name__ == '__main__':
    n = int(input().strip())

    result = generateAngleBracketSequences(n)

    print('\n'.join(result))
