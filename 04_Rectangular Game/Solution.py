#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(steps):
    minx=steps[0][0]
    miny=steps[0][1]
    print(len(steps))
    for i in range(len(steps)):
        if minx>steps[i][0]:
            minx=steps[i][0]
        if miny>steps[i][1]:
            miny=steps[i][1]
    return minx*miny

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    steps = []

    for _ in range(n):
        steps.append(list(map(int, input().rstrip().split())))

    result = solve(steps)

    fptr.write(str(result) + '\n')

    fptr.close()
