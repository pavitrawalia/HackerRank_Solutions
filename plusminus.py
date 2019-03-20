
import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p=0
    g=0
    z=0
    for i in range(0,n):
        if arr[i]>0:
            p+=1
        elif arr[i]<0:
            g+=1
        else:
            z+=1
    if n!=0:
        print float(p)/n
        print float(g)/n
        print float(z)/n  
    else:
        pass                  

if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)
