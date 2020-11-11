#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def rever(n):       //funtion to reverse the number
    rev= 0
    while(n > 0):
        a = n % 10
        rev = rev * 10 + a 
        n = n // 10
    return rev
def beautifulDays(i, j, k):
    count = 0
    for n in range(i,j+1):
        temp = n
        if abs(temp-rever(n))%k==0:
            count+=1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
