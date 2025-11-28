#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isAlphabeticPalindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code as parameter.
#

def isAlphabeticPalindrome(code):
    # alphabets = "".join(filter(lambda x: x.isalpha(), code)).lower()
    # if alphabets == "".join(reversed(alphabets)):
    #     return 1
    # return 0
    alphabets = [ch.lower() for ch in code if ch.isalpha()]
    return int(alphabets == alphabets[::-1])

if __name__ == '__main__':
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))
