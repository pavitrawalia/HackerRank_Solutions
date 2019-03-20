

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    arr=[]
    for i in range(len(s)):
        arr.append(ord(s[i]))
    for j in range(len(s)):
        if j<len(s)-1:
            a= abs(arr[j]-arr[j+1])
            b= abs(arr[len(s)-1-j]-arr[len(s)-1-(j+1)])
            if a==b:
                flag=0
            else:
                flag=1
                break
        else:
            pass        
    if flag==0:
        return "Funny"
    else:
        return "Not Funny"       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s =list(raw_input())
    
        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
