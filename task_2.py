import matplotlib.pyplot as plt
import numpy as np
 

def hyperbola_plotter(k=1):
    x = np.linspace(-100, 100, 100)
    y = k/x

    plt.plot(x, y)

    plt.savefig('fig_2.png')

if __name__ =='__main__':
    hyperbola_plotter()