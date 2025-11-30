#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findFirstOccurrence' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def findFirstOccurrence(nums, target):
    for index, num in enumerate(nums):
        if num == target:
            return index
    return -1
    
    
    # if not nums:
    #     return -1
    # try:
    #     return nums.index(target)
    # except ValueError:
    #     return -1
    
    # if target in nums:
    #     return nums.index(target)
    # return -1


if __name__ == '__main__':
    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    target = int(input().strip())

    result = findFirstOccurrence(nums, target)

    print(result)
