#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maximizeNonOverlappingMeetings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY meetings as parameter.
#

def maximizeNonOverlappingMeetings(meetings):
    meetings.sort(key=lambda x: x[1])
    count = 0
    end = 0
    
    for row in meetings:
        if row[0] >= end:
            end = row[1]
            count += 1
    return count     
            

if __name__ == '__main__':
    meetings_rows = int(input().strip())
    meetings_columns = int(input().strip())

    meetings = []

    for _ in range(meetings_rows):
        meetings.append(list(map(int, input().rstrip().split())))

    result = maximizeNonOverlappingMeetings(meetings)

    print(result)
