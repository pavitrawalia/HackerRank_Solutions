

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a, n):
    count=0
    for i in range(n):
        if a[i]<=0:
            count+=1
        else:
            pass    
    if count>=k:
        return "NO"
    else:
        return "YES"            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        nk = raw_input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = map(int, raw_input().rstrip().split())

        result = angryProfessor(k, a, n)

        fptr.write(result + '\n')

    fptr.close()
