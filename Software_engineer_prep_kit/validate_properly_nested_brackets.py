#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'areBracketsProperlyMatched' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code_snippet as parameter.
#

def areBracketsProperlyMatched(code_snippet):
    stack = []
    bracket_mapping = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    
    for ch in code_snippet:
        if ch in bracket_mapping.values():
            stack.append(ch)
        elif ch in bracket_mapping:
            if not stack or stack[-1] != bracket_mapping[ch]:
                return 0
            stack.pop()
    return not stack
            

if __name__ == '__main__':
    code_snippet = input()

    result = areBracketsProperlyMatched(code_snippet)

    print(int(result))
