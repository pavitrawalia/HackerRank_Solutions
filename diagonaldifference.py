
import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    pd=0
    sd=0
    for i in range(0,n):
        for j in range(0,n):
            if i==j:
                pd+=arr[i][j]

    for i in range(0,n):
        for j in range(0,n):
            if i+j==n-1:
                sd+=arr[i][j]
