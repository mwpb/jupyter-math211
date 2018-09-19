import matplotlib.pyplot as plt
import math
from sympy import latex, Matrix
from IPython.display import display, Markdown, Math, Latex
from mpmath import mp
import numpy as np
from .elimination import roundMatrix

mp.dps = 4
def plot2DSystem(A):
    colours = ['blue', 'orange', 'green', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red'] # Run out of colours...
    x = np.arange(-10, 10, 0.1)
    fig, ax = plt.subplots()
    for i in range(0, len(A)):
        if not math.isclose(A[i][1], 0):
            ax.plot(x, A[i][2]/A[i][1]-(A[i][0]/A[i][1])*x, color = colours[i])
        elif not math.isclose(A[i][0], 0):
            ax.axvline(x = A[i][2]/A[i][0], color = colours[i])
            
def printM(A):
    roundMatrix(A)
    display((Latex(r'${'+latex(Matrix(A))+'}$')))
    print('\n')