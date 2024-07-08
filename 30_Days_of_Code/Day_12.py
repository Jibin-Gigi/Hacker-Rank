#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []
    temp = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for row in range(4):
        for col in range(4):
            value = sum(arr[row][col:col+3]) + sum(arr[row+2][col:col+3]) +arr[row+1][col+1]
            temp.append(value)
        
    print(max(temp))
