

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(0,n):
        p=n-i-1
        g=i+1
        if p!=0:
            p=n-i-2
            print " "*p,
        else:
            pass    
        print "#"*g,
        print "\n",
if __name__ == '__main__':
    n = int(raw_input())

    staircase(n)

