

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    cma=0
    cmi=0
    maxs=scores[0]
    mins=scores[0]
    for i in range(len(scores)):
        if scores[i]>maxs:
            cma+=1
            maxs=scores[i]
        elif scores[i]<mins:
            cmi+=1
            mins=scores[i]
        else: 
            pass    
    return str(cma)+" "+str(cmi),


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    scores = map(int, raw_input().rstrip().split())

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
