

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    p=n
    count=0
    while(p!=0):
        if p%10!=0 and n%(p%10)==0:
            count+=1
        else:
            pass
        p=p/10    
    return count        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
