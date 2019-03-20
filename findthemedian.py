

import math
import os
import random
import re
import sys

# Complete the findMedian function below.
def findMedian(arr):
    arr.sort()
    i=(n//2)
    return arr[i]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
