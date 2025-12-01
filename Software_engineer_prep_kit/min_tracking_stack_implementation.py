#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'processCouponStackOperations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def processCouponStackOperations(operations):
    stack = []
    result = []
    min_stack = []
    
    for op in operations:
        if op[:4] == 'push':
            num = int(op.split(' ')[1])
            stack.append(num)
            if not min_stack or num <= min_stack[-1]:
                min_stack.append(num)
        elif stack:
            if op == 'pop':
                temp = stack.pop()
                if temp == min_stack[-1]:
                    min_stack.pop()
            elif op == 'top':
                result.append(stack[-1])
            elif op == 'getMin':
                result.append(min_stack[-1])
    return result
                

if __name__ == '__main__':
    operations_count = int(input().strip())

    operations = []

    for _ in range(operations_count):
        operations_item = input()
        operations.append(operations_item)

    result = processCouponStackOperations(operations)

    print('\n'.join(map(str, result)))
