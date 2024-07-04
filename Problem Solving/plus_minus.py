#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    positive_no, negative_no, zeroes = 0, 0, 0
    for item in arr:
        if item == 0:
            zeroes += 1
        elif item > 0:
            positive_no += 1
        else:
            negative_no += 1
    
    print(positive_no/n)
    print(negative_no/n)
    print(zeroes/n)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
