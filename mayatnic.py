import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def animate_mathematical_pendulum(length=1, mass=1, theta0=np.pi/4, dt=1, t_end=10):
    """
    Анимирует математический маятник.

    Args:
        length: Длина нити.
        mass: Масса груза.
        theta0: Начальный угол (в радианах).
        dt: Шаг дискретизации по времени.
        t_end: Конечное время моделирования.
    """

    g = 9.81  # Ускорение свободного падения

    # Вычисление начальных условий
    theta = theta0
    theta_dot = 0  # Начальная скорость равна нулю

    t = np.arange(0, t_end, dt)
    theta_vals = [theta]
    
    # Вычисление углов для каждого момента времени
    for time in t:
        theta_ddot = -g / length * np.sin(theta)
        theta_dot += theta_ddot * dt
        theta += theta_dot * dt
        theta_vals.append(theta)

    fig, ax = plt.subplots()
    ax.set_xlim(-1.5 * length, 1.5 * length)
    ax.set_ylim(-1.5 * length, 1.5 * length)
    ax.set_aspect('equal', adjustable='box')

    line, = ax.plot([0, length * np.sin(theta_vals[0])], [0, -length * np.cos(theta_vals[0])], 'o-', lw=2, markersize=8)
    
    bob, = ax.plot(length * np.sin(theta_vals[0]), -length * np.cos(theta_vals[0]), 'ro', markersize=10)

    def update(frame):
        x = length * np.sin(theta_vals[frame])
        y = -length * np.cos(theta_vals[frame])
        line.set_data([0, x], [0, y])
        bob.set_data([x], [y])  # Исправление: оборачиваем x и y в списки
        return line, bob

    ani = animation.FuncAnimation(fig, update, frames=len(t), interval=20, blit=False)

    # Сохранение анимации как GIF
    ani.save('mathematical_pendulum.gif', writer='pillow', fps=60)

    plt.show()

# Пример использования
animate_mathematical_pendulum()