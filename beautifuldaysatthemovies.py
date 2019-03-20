
import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    count=0
    for i in range(i,j+1):
        b="".join(reversed(str(i)))
        if abs(i-int(b))%k==0 and type(abs(i-int(b))/k)==type(2):
            count+=1
        else:
            pass    
    return count        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = raw_input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
