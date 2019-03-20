

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    factorial = 1
 
    if n== 0:
        print 1
    else:
        for i in range(1,n+ 1):
            factorial = factorial*i
        print(factorial)

if __name__ == '__main__':
    n = int(raw_input())

    extraLongFactorials(n)
