import copy
import os
import math
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
from pythonUtils.elementaryOperations import swapRows, addMultiple, scalarMultiply

def eliminationStep(A):
    row = 0
    col = 0
    steps = [copy.deepcopy(A)]
    pivots = []
    while row < len(A) and col < len(A[0]):
        largestRow = row
        if A[row][col] == 0:
            current = 0
            for i in range(row+1, len(A)):
                if abs(A[i][col]) > current:
                    largestRow = i
                    current = abs(A[i][col])
        if A[largestRow][col] == 0:
                col += 1
        else:
            swapRows(A, largestRow, row)
            scalarMultiply(A, row, (1/A[row][col]))
            steps.append(copy.deepcopy(A))
            for i in range(row+1, len(A)):
                addMultiple(A, row, -A[i][col], i)
            pivots.append([row, col])
            steps.append(copy.deepcopy(A))
            row += 1
            col += 1
    return pivots, steps

def backSubstitution(A, pivots, steps):
    for pivot in pivots:
        row = pivot[0]
        col = pivot[1]
        for i in range(0, row):
            addMultiple(A, row, -A[i][col], i)
    steps.append(copy.deepcopy(A))
    return steps

def roundMatrix(A):
    for i in range(0,len(A)):
        for j in range (0, len(A[0])):
            A[i][j] = round(A[i][j], 4)
            if math.isclose(A[i][j], int(A[i][j])):
                A[i][j] = int(A[i][j])

def rref(A):
    pivots, steps = eliminationStep(A)
    steps = backSubstitution(A, pivots, steps)
    for step in steps:
        roundMatrix(step)
    return steps