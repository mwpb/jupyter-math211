def swapRows(A, i, j):
    """Swaps the ith and jth rows of A."""
    ithRow = A[i]
    jthRow = A[j]
    A[i] = jthRow
    A[j] = ithRow
    return A

def addMultiple(A, i, n, j):
    """Adds n times the ith row of A to the jth row of A."""
    for k in range(0,len(A[i])):
        A[j][k] = A[j][k] + n*A[i][k]
        
def scalarMultiply(A, i, n):
    """Multiplies the ith row of A by n."""
    for j in range(0,len(A[i])):
        A[i][j] = n*A[i][j]
    return A