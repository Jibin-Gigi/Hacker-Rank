#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'debounceTimestamps' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY timestamps
#  2. INTEGER K
#

def debounceTimestamps(timestamps, K):
    if not timestamps:
        return 0
        
    result = 1
    last = timestamps[0]
    for i in range(1, len(timestamps)):
        if timestamps[i] - last >= K:
            result += 1
            last = timestamps[i]
    return result
            
            

if __name__ == '__main__':
    timestamps_count = int(input().strip())

    timestamps = []

    for _ in range(timestamps_count):
        timestamps_item = int(input().strip())
        timestamps.append(timestamps_item)

    K = int(input().strip())

    result = debounceTimestamps(timestamps, K)

    print(result)
