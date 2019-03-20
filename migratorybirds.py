

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr,arr_count):
    count=[0,0,0,0,0]
    ok=[0,0,0,0,0]
    for i in range(arr_count):
        if arr[i]==1:
            count[0]+=1
            ok[0]+=1
        elif arr[i]==2:
            count[1]+=1 
            ok[1]+=1
        elif arr[i]==3:
            count[2]+=1
            ok[2]+=1
        elif arr[i]==4:
            count[3]+=1
            ok[3]+=1
        elif arr[i]==5:
            count[4]+=1
            ok[4]+=1   
        else:
            pass         
    count.sort()
    for i in range(len(count)):
        if ok[i]==count[len(count)-1]:
            return i+1
            break
        else:
            pass    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input().strip())

    arr = map(int, raw_input().rstrip().split())

    result = migratoryBirds(arr,arr_count)

    fptr.write(str(result) + '\n')

    fptr.close()
