#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countInstallationSequences' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def countInstallationSequences(n):
    if not n:
        return 1
    a, b = 1, 1
    for index in range(2, n+1):
        a, b = b, a+b
    return b

if __name__ == '__main__':
    n = int(input().strip())

    result = countInstallationSequences(n)

    print(result)
