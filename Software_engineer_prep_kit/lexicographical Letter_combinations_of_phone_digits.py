#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minTasksToCancelForNoConflict' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING digits as parameter.
#

def minTasksToCancelForNoConflict(digits):
    keypad_mapping = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz',
        0: '0',
        1: '1'
    }
    
    # result = []
    # sequence_array = []
    
    # length = len(digits)
    
    # def combinations(index):
    #     if index == length:
    #         result.append("".join(sequence_array))
    #         return
    #     if index < length:
    #         for val in keypad_mapping[int(digits[index])]:
    #             sequence_array.append(val)
    #             combinations(index+1)
    #             sequence_array.pop()
                
    # combinations(0)
    # return result
    
    if not digits:
        return []
    
    result = ['']
    for d in digits:
        letters = keypad_mapping.get(int(d), '')
        
        new = []
        for prefix in result:
            for ch in letters:
                new.append(prefix + ch)
        result = new
    return result
        
        

if __name__ == '__main__':
    digits = input()

    result = minTasksToCancelForNoConflict(digits)

    print('\n'.join(result))
