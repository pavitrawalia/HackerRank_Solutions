

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b,n):
    sum1=0
    for i in range(n):
        if i!=k:
            sum1+=bill[i]
        else:
            pass 
    if b-(sum1//2)==0:
        print "Bon Appetit"
    else:
        print b-(sum1//2)    


if __name__ == '__main__':
    nk = raw_input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = map(int, raw_input().rstrip().split())

    b = int(raw_input().strip())

    bonAppetit(bill, k, b,n)
