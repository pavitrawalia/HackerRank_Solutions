
import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    ass=0
    bss=0
    for i in range(0,3):
        if a[i]>b[i]:
            ass+=1
        elif a[i]<b[i]:
            bss+=1
        else:
            pass      
    return [ass,bss]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = map(int, raw_input().rstrip().split())

    b = map(int, raw_input().rstrip().split())

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
