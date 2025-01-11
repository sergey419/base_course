import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Создаем фигуру и оси
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(0, 10)

# Функция для генерации волновой поверхности
def wave_surface(t):
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2) - t)  # Уравнение волны
    return X, Y, Z

# Функция обновления для анимации
def update(t):
    ax.clear()
    X, Y, Z = wave_surface(t)
    ax.plot_surface(X, Y, Z, cmap='viridis')

# Создание анимации
ani = FuncAnimation(fig, update, frames=np.linspace(0, 20, 100), repeat=True)

# Сохранение анимации в формате GIF
ani.save('tsunami_animation.gif', writer='pillow')
plt.show()