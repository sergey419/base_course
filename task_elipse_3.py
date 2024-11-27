import matplotlib.pyplot as plt
import numpy as np


def elipse_plotter(x0=0, y0=0, dx=1, dy=1):

    x = np.arange(-2*dx + x0, 2*dx +x0, 0.01)
    y = np.arange(-2*dy + y0, 2*dy +y0, 0.01)

    X, Y = np.meshgrid(x, y)
    fxy = ((X - x0)**2)/(dx**2) + ((Y - y0)**2)/(dy**2)

    plt.contour(X, Y, fxy, levels=[1])

    plt.savefig('fig_3.1.png')

if __name__=='__main__':
    plt.axis('equal')
    plt.grid()
    elipse_plotter()


