import matplotlib.pyplot as plt
import numpy as np

def circle_plotter(R=3):
    alpha = np.arange(-2*np.pi, 2*np.pi, 0.1)  # Параметр
 
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)

    plt.plot(x, y, ls='--', lw=3)
    plt.axis('equal')
    plt.savefig('fig_1.png')
 
if __name__ == '__main__':
    circle_plotter()




# АНИМАЦИЯ                                          

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
# Создание пространства и подпространства для анимации
fig, ax = plt.subplots()
 
# Объект анимации
anim_object, = plt.plot([], [], '-', lw=2)
 
x, y = [], [] # Координаты объекта анимации
frames_interval = np.linspace(0, 2*np.pi, 100)
 
ax.set_xlim(0, 2*np.pi) # Пределы изменения переменной Х
ax.set_ylim(-1, 1) # Пределы изменения переменной У
 
# Функция подстановки параметра в объект анимации
def update(frame):
    x.append(frame) # Расчет координаты Х
    y.append(np.sin(frame)) # Расчет координаты У
    
    # Передача координат объекту анимации
    anim_object.set_data(x, y)
 
    return anim_object
 
 
ani = FuncAnimation(fig, # Вызов пространства для анимации
                    update, # Вызов функции подстановки координат
                    frames=frames_interval, # Интервал значений
                    interval=50) # Интервал между кадрами,
                                 # по умолчанию 200 милисекунд
 
ani.save('animation_1.gif', writer="pillow")




# АНИМАЦИЯ СТАНДАРТНЫХ ОБЪЕКТОВ

	
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
 
 
def circle_move(R, angle_vel, time):
    alpha = angle_vel * np.pi / 180 * time
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
    return x, y
 
 
fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')
ball_line, = plt.plot([], [], '-', color='r', label='Ball')
 
frames = 180
coords = np.zeros((frames, 2))
 
 
def animate(i):
    coords[i] = circle_move(R=2, angle_vel=1, time=i)
    ball.set_data([coords[i][0]], [coords[i][1]])
    ball_line.set_data(coords[:i, 0], coords[:i, 1])
    return ball, ball_line
 
 
edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
ani = FuncAnimation(fig, animate, frames=frames, interval=30)
ani.save('animation_2.gif', writer="pillow") 



# АНИМАЦИЯ НЕСТАНДАРТНЫХ ОБЪЕКТОВ

	
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
 
 
def circle_move(R, vx0, vy0, time):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = np.arange(0, 2*np.pi, 0.6)
    x = x0 + R*np.cos(alpha)
    y = y0 + R*np.sin(alpha)
    return x, y
 
 
fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')
 
 
def animate(i):
    ball.set_data(circle_move(R=0.5, vx0=0.01, vy0=0.01, time=i))
    return ball
 
 
edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
ani = FuncAnimation(fig, animate, frames=100, interval=30)
ani.save('animation_3.gif', writer="pillow")








