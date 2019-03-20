

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    res=[]
    ar=[]
    for p in range(len(arr)):
        ar.append(0)
    while(arr!=ar):
        for i in range(len(arr)):
            count=0
            arr=arr.sort()
            if arr[i]==0:
                count=0
            else:    
                arr[i]-=arr[0]
                count+=1
        res.append(count)           
    return (list(res))    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
