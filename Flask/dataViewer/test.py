# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the squares function below.
def squares(a, b):

    count = 0
    for n in range(a,b+1):
        for m in range(1,100001):
            dm = m**2
            if dm > b: break
            elif dm >= a: count +=1
        return count

        if math.remainder(sr,1) == 0: count += 1
    return count

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)
        print(result)

#        fptr.write(str(result) + '\n')

#    fptr.close()






