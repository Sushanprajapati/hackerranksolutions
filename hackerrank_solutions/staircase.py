#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    height = n 
    for row in range(height):
        for s in range(height-row-1):
            print(end=' ')
        for a in range(row+1):
            print('#', end='')
        print()
if __name__ == '__main__':
    n = int(input())
    staircase(n)