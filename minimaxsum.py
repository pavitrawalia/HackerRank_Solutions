

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    print arr[0]+arr[1]+arr[2]+arr[3],
    print arr[1]+arr[2]+arr[3]+arr[4]
   

if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())

    miniMaxSum(arr)
