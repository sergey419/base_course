
# Астроида

import matplotlib.pyplot as plt
import numpy as np
t = input(('Введите значение t : '))
def astroida_plotter(R=4):
    beta = np.arange(-2*np.pi, 2*np.pi, 0.1)

    x = R * np.cos(beta)**3 * t
    y = R * np.sin(beta)**3 * t

    plt.plot(x, y, ls='-', lw=3)
    plt.axis('equal')
    plt.savefig('fig_task_1.png')

if __name__=='__main__':
    astroida_plotter()


# Циклоида


t = input(('Введите значение t : '))
def cickloida_plotter(R=4):
    alpha = np.arange(-2*np.pi, 2*np.pi, 0.1)

    x = R * (t - (np.sin(alpha)**3 * t))
    y = R * (1 - (np.cos(alpha)**3 * t))

    plt.plot(x, y, ls='-', lw=3)
    plt.axis('equal')
    plt.savefig('fig_task_2.png')

if __name__=='__main__':
    cickloida_plotter()

