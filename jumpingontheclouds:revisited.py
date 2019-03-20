

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e=100
    c.append(0)
    for i in range(0,n,k):
            if c[(i+k)%n]==1 :
                e-=3
            elif c[(i+k)%n]==0 :
                e-=1
            else:
                pass
    return e


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
