#!/bin/python

import math
import os
import random
import re
import sys

# Complete the taumBday function below.
def taumBday(b, w, bc, wc, z):
    cost=0
    if b*bc>b*(z+wc):
        cost+=b*(z+wc)
    else:
        cost+=b*bc
    if w*wc>w*(z+bc):
        cost+=w*(z+bc)
    else:
        cost+=w*wc
    return cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())
    for t_itr in xrange(t):
    
        bw = raw_input().split()

        b = int(bw[0])

        w = int(bw[1])

        bcWcz = raw_input().split()

        bc = int(bcWcz[0])

        wc = int(bcWcz[1])

        z = int(bcWcz[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()
