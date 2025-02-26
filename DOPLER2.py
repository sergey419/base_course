import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Константы
c = 1  # скорость звука
freq0 = 1.0   # исходная частота
car_start_x = -6
car_y = -2.0  # Y-положение на дороге
# Рассчет расстояния которое должен проехать автомобиль
road_length = 6 - (-6)
# Регулировка скорости автомобиля и количество кадров
car_speed = 0.1  # нормализованная скорость автомобиля
max_radius = 3.5
num_frames = int(road_length / car_speed) + 10 # Вычисление количества кадров, за которые автомобиль достигнет дороги
road_y = -2.0
person_A_x = -4
person_B_x = 4
person_y_offset = 0.5  # Смещение людей от дороги
text_x_offset = 0.2    # Смещение текста от маркеров


# Настройка сюжета
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-6, 6)
ax.set_ylim(-5, 3)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
ax.set_facecolor('skyblue')
ax.set_title("Doppler Effect Animation")

# Создание дороги
ax.plot([-6, 6], [road_y, road_y], color='grey', linewidth=4)
ax.plot([-6,6],[road_y-0.3, road_y-0.3], color = 'white', linestyle='--')
ax.plot([-6,6],[road_y+0.3, road_y+0.3], color = 'white', linestyle='--')

# Создание человека А и В
ax.plot(person_A_x, road_y + person_y_offset, marker="o", markersize = 10, color="black")
ax.text(person_A_x+text_x_offset, road_y + person_y_offset, "A")

ax.plot(person_B_x, road_y + person_y_offset, marker="o", markersize = 10, color="black")
ax.text(person_B_x+text_x_offset, road_y + person_y_offset, "B")

# Создание машины
car, = ax.plot([],[],marker='o',markersize = 10, color = 'red')

# Волновые круги
wave_circles = []
wave_lines = []
for i in range(7):
    circle, = ax.plot([], [], color='black', linestyle='-',fillstyle='none')
    wave_circles.append(circle)


def create_wavefront(center_x, center_y, radius, num_points=100):
    angles = np.linspace(0, 2*np.pi, num_points)
    x = center_x - radius / 2 + radius * np.cos(angles)
    y = center_y + radius * np.sin(angles)
    return x, y

# Функция анимации
def animate(frame):
  car_x = car_start_x + frame * car_speed
  car.set_data([car_x], [car_y])  # Машина всегда в пути (car_y)
  
  time = frame/15
  v = car_speed  # Скорость источника
    
  for i, circle in enumerate(wave_circles):
    radius = c * (time - (i/freq0))
    if radius > 0 and radius < max_radius :
      lambda_wave = (2*np.pi*c/(2*np.pi*freq0))
      x,y = create_wavefront(car_x-v*(time-(i/freq0)), car_y, radius)
      circle.set_data(x,y)
    else :
       circle.set_data([],[])
  return car, *wave_circles



# Создание анимации
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

# Создание анимации как гифки
ani.save('doppler_effect.gif', writer='pillow', fps=30)

plt.show()