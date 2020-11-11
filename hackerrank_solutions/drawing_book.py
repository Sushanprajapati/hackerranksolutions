#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    front = int(p/2)
    if n%2!=0:
        back = int((n-p)/2)    #if number of pages is odd
    else:
        back = int((n-p+1)/2)       #if number of pages is even
    return min(front,back)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
