#!/bin/python3


if __name__ == '__main__':
    N = int(input().strip())
    if N % 2 != 0  or ( N % 2 == 0 and N in range (6,21) ):
        print('Weird')
    if N % 2 == 0 and ( N in range(2,6) or N > 20 ):
        print('Not Weird')
