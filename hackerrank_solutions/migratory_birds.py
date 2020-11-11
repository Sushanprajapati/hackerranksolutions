#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    bird_freq = [0,0,0,0,0,0]  #since the value cannot be more than 5, we create this list 
    for i in range(len(arr)):
        bird_freq[arr[i]] += 1          #increment the value of bird_freq with one, when same element is seen in main list, other value will remain 0 
    return bird_freq.index(max(bird_freq))      #index with maximum value is returned, by default, smaller one is returned 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
