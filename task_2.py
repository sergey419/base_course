import matplotlib.pyplot as plt
import numpy as np
 

def hyperbola_plotter():
    x = np.arange(0.1 , 10, 0.1 )
    x1 = np.arange(-10, -0.1, 0.1)
    y = 1/x
    y1 = 1/x1

    plt.plot(x, y, label='my hyperbola')
    plt.plot(x1, y1, label='my hyperbola')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title('Hyperbola plotter')
    plt.legend()
    plt.axis('equal')
    
    plt.savefig('fig_2.png')

if __name__ =='__main__':
    hyperbola_plotter()

