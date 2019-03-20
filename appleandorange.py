

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges,m,n):
    counta=0
    counto=0
    for i in range(m):
        apples[i]+=a
    for j in range(n):
        oranges[j]+=b
    for i in range(m):
        if apples[i]<=t and apples[i]>=s:
            counta+=1
    for j in range(n):
        if oranges[j]<=t and oranges[j]>=s:
            counto+=1        
    print counta
    print counto

if __name__ == '__main__':
    st = raw_input().split()

    s = int(st[0])

    t = int(st[1])

    ab = raw_input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = map(int, raw_input().rstrip().split())

    oranges = map(int, raw_input().rstrip().split())

    countApplesAndOranges(s, t, a, b, apples, oranges,m,n)
