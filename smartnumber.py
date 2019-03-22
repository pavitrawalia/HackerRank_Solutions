import math

def is_smart_number(num):
    val = int(math.sqrt(num))
    if val* val == num:
        return True
    return False

for _ in range(int(raw_input())):
    num = int(raw_input())
    ans = is_smart_number(num)
    if ans:
        print "YES"
    else:
        print "NO"



