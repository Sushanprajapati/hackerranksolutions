!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    digi = []
    count = 0
    for d in str(n):    '''converting integer to string to split it and append to new list'''
        digi.append(int(d))
    for a in digi:
        if a == 0:
            continue
        if n%a==0:
            count+=1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
