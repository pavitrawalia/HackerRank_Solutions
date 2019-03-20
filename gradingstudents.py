

from __future__ import print_function

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # Write your code here.
    #
    a=[]
    for i in range(len(grades)):
        if grades[i]>=38:

            if (grades[i]%10>5):
                no=int(str((grades[i]//10)+1)+"0")
                if no-grades[i]<3:
                    no=no
                else:
                    no=grades[i]
            elif (grades[i]%10<5):
                no=int(str(grades[i]//10)+"5")
                if no-grades[i]<3:
                    no=no
                else:
                    no=grades[i]
            else:
                no=grades[i]
            a.append(no)
        else:
            a.append(grades[i])    
    return a    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    grades = []

    for _ in xrange(n):
        grades_item = int(raw_input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
