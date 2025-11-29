#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'binarySearch' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def binarySearch(nums, target):
    if target in nums:
        return nums.index(target)
    return -1

if __name__ == '__main__':
    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    target = int(input().strip())

    result = binarySearch(nums, target)

    print(result)
