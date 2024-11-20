import matplotlib.pyplot as plt
import numpy as np

def giperbola_plotter(k=1):
    x = np.arange(0.1, 10, 0.1)
    y = k/x

    x1 = np.arrange(-10, -0.1, 0.1)
    y1 = k/x1

    plt.plot(x, y)
    plt.plot(x1, y1)
    plt.xlabel('coord - x')
    plt.xlabel('coord - y')
    plt.xlabel('coord - x1')
    plt.xlabel('coord - y1')
    

    plt.savefig('fig_3.png')

if __name__ == '__main__':
    




