

import math
import os
import random
import re
import sys
import collections

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count=0
    counter=collections.Counter(ar)
    for i in range(len(counter)):
        if counter.values()[i]%2==0:
            count+=counter.values()[i]/2
        else:
            count+=(counter.values()[i]-1)/2  
    return count        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
