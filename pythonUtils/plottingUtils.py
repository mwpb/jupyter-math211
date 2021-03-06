import matplotlib.pyplot as plt
import math
from sympy import latex, Matrix
from IPython.display import display, Markdown, Math, Latex
from mpmath import mp
import numpy as np
from .elimination import roundMatrix
import matplotlib.patches as patches

def plotColumns(A):
    zero = [0,0]
    sumvector = [A[0][0]+A[0][1], A[1][0]+A[1][1]]
    xmax = max(zero[0], sumvector[0], A[0][0], A[0][1])+0.5
    xmin = min(zero[0], sumvector[0], A[0][0], A[0][1])-0.5
    ymax = max(zero[1], sumvector[1], A[1][0], A[1][1])+0.5
    ymin = min(zero[1], sumvector[1], A[1][0], A[1][1])-0.5
    maximum = max(xmax, ymax)+min(ymin, xmin)
    style="Simple,tail_width=0.5,head_width=4,head_length=8"

    ax = plt.axes()
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.add_patch(plt.Polygon([[0,0], [A[0][0],A[1][0]], [A[0][0]+A[0][1], A[1][0]+A[1][1]], [A[0][1], A[1][1]]], color='palegreen' , zorder = 2))
    #ax.add_patch(patches.FancyArrowPatch([A[0][0]/2,A[1][0]/2], [A[0][1]/2,A[1][1]/2],connectionstyle="arc3,rad=.5", arrowstyle=style, color="k", zorder=3))
    ax.arrow(0, 0, A[0][0], A[1][0], head_width=maximum/20, fc='b', ec='b', length_includes_head = True, zorder = 3)
    ax.arrow(0, 0, A[0][1], A[1][1], head_width=maximum/20, fc='r', ec='r', length_includes_head = True, zorder = 3)
    plt.grid(zorder = 0)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.savefig('test.png')
    plt.show()

def plotVectors(A):
    xs = [v[2] for v in A]+[0]
    ys = [v[3] for v in A]+[0]
    xmax = max(xs)+0.5
    xmin = min(xs)-0.5
    ymax = max(ys)+0.5
    ymin = min(ys)-0.5
    maximum = max(xmax, ymax)+min(ymin, xmin)
#    style="Simple,tail_width=0.5,head_width=4,head_length=8"
    ax = plt.axes()
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    for v in A:
        if len(v) == 6:
            al = 0.0
        else:
            al = 1.0
        ax.arrow(v[0], v[1], v[2]-v[0], v[3]-v[1], head_width=maximum/20, fc=v[4], ec=v[4], length_includes_head = True, zorder = 3, alpha = al)
    plt.grid(zorder = 0)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.savefig('test.svg')
    plt.show()

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

def plot3dVectors(A):
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2)
    ax.set_zlim(0, 2)
    for v in A:
        a = Arrow3D([0,v[0]],[0,v[1]],[0,v[2]] , mutation_scale=20, 
                    lw=3, arrowstyle="-|>", color=v[3])
        ax.add_artist(a)

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