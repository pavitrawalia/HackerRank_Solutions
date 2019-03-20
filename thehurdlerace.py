

import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.
def hurdleRace(k, height,n):
    count=0
    for i in range(n):
        if height[i]>=k:
            count+=(height[i]-k)
            k=height[i]
        else:
            pass  
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = map(int, raw_input().rstrip().split())

    result = hurdleRace(k, height,n)

    fptr.write(str(result) + '\n')

    fptr.close()
