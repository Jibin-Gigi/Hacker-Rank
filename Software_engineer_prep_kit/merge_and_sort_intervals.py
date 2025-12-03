#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mergeHighDefinitionIntervals' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
#

def mergeHighDefinitionIntervals(intervals):
    result = []
    intervals.sort(key = lambda x: x[0])
    
    if not intervals:
        return []
      
    result = [intervals[0]]
    
    for val in intervals[1:]:
        first = result[-1]
        if first[1] >= val[0]:
            first[1] = max(first[1], val[1])
        else:
            result.append(val)
    
    return result

if __name__ == '__main__':
    intervals_rows = int(input().strip())
    intervals_columns = int(input().strip())

    intervals = []

    for _ in range(intervals_rows):
        intervals.append(list(map(int, input().rstrip().split())))

    result = mergeHighDefinitionIntervals(intervals)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
