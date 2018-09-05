import matplotlib.pyplot as plt
import numpy as np
import math

def plot2DSystem(A):
    x = np.arange(-10, 10, 0.1)
    fig, ax = plt.subplots()
    if not math.isclose(A[0][1], 0):
        ax.plot(x, A[0][2]/A[0][1]-(A[0][0]/A[0][1])*x)
    elif not math.isclose(A[0][0], 0):
        ax.axvline(x = A[0][2]/A[0][0])        
        #plt.plot([A[0][2]/A[0][0],A[0][2]/A[0][0]],ax.get_ylim(), 'r-')
    if A[1][1] != 0:
        ax.plot(x, A[1][2]/A[1][1]-(A[1][0]/A[1][1])*x, color = 'orange')
    elif A[1][0] != 0:
        ax.axvline(x = A[1][2]/A[1][0], color = 'orange')
#        plt.plot([A[1][2]/A[1][0],A[1][2]/A[1][0]],ax.get_ylim(), 'r-')

def printM(A):
    print(np.matrix(A))
    print('\n')