import copy
from elementaryOperations import swapRows, addMultiple, scalarMultiply

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

def rref(A):
    pivots, steps = eliminationStep(A)
    return backSubstitution(A, pivots, steps)