#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    scoreAlice = 0
    scoreBob = 0
    array = []

    for index in range(len(a)):       #assuming that length of both a,b is same
        if a[index] > b[index]:
            scoreAlice += 1  
        if a[index] == b[index]:
            pass
        if a[index] < b[index]:
            scoreBob += 1
    array = [scoreAlice,scoreBob]
    return array 
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
