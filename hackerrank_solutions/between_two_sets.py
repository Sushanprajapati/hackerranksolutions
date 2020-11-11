#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    count= 0
    multiple_a = []
    factors_b = []
    len_of_list= len(a+b)
    newlist=[]
    for val in range(1,101):   #creating a list of multiple of list 'a'
        for i in a:
            if val%i==0:
                multiple_a.append(val)
    for val in range(1,101):   #creating a list of factors of list 'b'
        for i in b:
            if i%val==0:
                factors_b.append(val)
    temp_list = multiple_a + factors_b  #merging two lists
    for i in temp_list:                 
        if temp_list.count(i) == len_of_list:   '''creating a new list of numbers, that are repeating and (repitition = length of totalnumber of                                                    items in given two list)'''
            newlist.append(i)
    return len(set(newlist))           #creating a set(unique numbers) and return the length of it


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()