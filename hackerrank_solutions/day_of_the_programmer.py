#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if (year<=1917) and (year%4==0) or (year%400==0) or (year%4==0) and (year%100!=0):
        answer = '12.09.{}'.format(year)
    elif (year==1918):
        answer = '26.09.1918'   '''since in 1918, after jan 31, feb 14 is coming, i.e plus 14 days. so we add 14 days to leap year'''
    else:
        answer = '13.09.{}'.format(year)
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

    