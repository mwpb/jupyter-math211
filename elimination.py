from elementaryOperations import swapRows, addMultiple, scalarMultiply

def eliminationStep(A):
    row = 0
    col = 0
    pivots = []
    while row < len(A) and col < len(A[0]):
        largestRow = row
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
        for i in range(row+1, len(A)):
            addMultiple(A, row, -A[i][col], i)
        pivots.append([row, col])
        row += 1
        col += 1
    return pivots

def backSubstitution(A, pivots):
    for pivot in pivots:
        row = pivot[0]
        col = pivot[1]
        for i in range(0, row):
            addMultiple(A, row, -A[i][col], i)

def rref(A):
    pivots = eliminationStep(A)
    backSubstitution(A, pivots)