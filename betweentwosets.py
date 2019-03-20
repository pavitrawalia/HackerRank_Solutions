

from __future__ import print_function

import os
import sys
from fractions import gcd
#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    #
    # Write your code here.
    #
    lc= a[0]
    gc= b[0]
    if len(a) > 1:
        for x in range(1,len(a)):
            lc=  (lc* a[x])/gcd(lc,a[x])
    if len(b) > 1:
        for x in range(1,len(b)):
            gc = gcd(gc,b[x])
    count = 0
    for x in range(lc, gc+1, lc):
        if gcd(x, gc) == x:
            count += 1
    return count
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = map(int, raw_input().rstrip().split())

    b = map(int, raw_input().rstrip().split())

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
