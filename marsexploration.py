#!/bin/python

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    count=0
    for i in range(0,len(s),3):
        if s[i]=='S':
            pass
        else:
           count+=1
        if s[i+1]=='O':
            pass
        else:
            count+=1
        if s[i+2]=='S':
            pass
        else:
            count+=1
                          
    return count            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
