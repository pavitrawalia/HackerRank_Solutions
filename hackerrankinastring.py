#!/bin/python

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    a=['h','a','c','k','e','r','r','a','n','k']
    count=0
    p=0
    for j in range(10):
        for i in range(p,(len(s))):
            if a[j]==s[i]:
                count+=1
                p=i+1
                break
            else:
                pass
                
    if count==10:
        return "YES"
    else:
        return "NO"    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
