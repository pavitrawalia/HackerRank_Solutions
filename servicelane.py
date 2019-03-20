

import math
import os
import random
import re
import sys

# Complete the serviceLane function below.
def serviceLane(n, cases,width,t):
    f=[]
    for i in range(0,t):
        a=cases[i][0]
        b=cases[i][1]
        g=[]
        for j in range(a,b+1):
            g.append(width[j])
        print min(g)

#result 
nt=raw_input().split(" ")
n = int(nt[0])

t = int(nt[1])

width = map(int, raw_input().rstrip().split())

cases = []

for _ in xrange(t):
    cases.append(map(int, raw_input().rstrip().split()))

serviceLane(n, cases,width,t)
