

import math
import os
import random
import re
import sys

# Complete the introTutorial function below.
def introTutorial(V, arr):
    for i in range(n):
        if arr[i]==V:
            return i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(raw_input())

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
