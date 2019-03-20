

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    sum1=2
    count=2
    for i in range(1,n):
        sum1=sum1*3
        sum1=sum1//2
        count+=sum1
        
        
    return count    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
