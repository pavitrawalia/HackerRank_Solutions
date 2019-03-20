

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p,n):
    ar=[]
    for j in range(1,n+1):
        for i in range(n):
            if p[p[i]-1]==j:
                ar.append(i+1) 
    return ar

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    p = map(int, raw_input().rstrip().split())

    result = permutationEquation(p,n)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
