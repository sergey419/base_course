import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Constants
c = 1  # speed of sound (normalized)
freq0 = 1.0   # original frequency
car_start_x = -6
car_y = -2.0  # Y-position of the road
car_speed = 0.05  # normalized car speed
max_radius = 3.5
num_frames = 150
road_y = -2.0
person_A_x = -4
person_B_x = 4
person_y_offset = 0.5  # Offset for the people from the road
text_x_offset = 0.2    # Offset of text from the markers


# Setup the plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-6, 6)
ax.set_ylim(-5, 3)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
ax.set_facecolor('skyblue')
ax.set_title("Doppler Effect Animation")

# Add road
ax.plot([-6, 6], [road_y, road_y], color='grey', linewidth=4)
ax.plot([-6,6],[road_y-0.3, road_y-0.3], color = 'white', linestyle='--')
ax.plot([-6,6],[road_y+0.3, road_y+0.3], color = 'white', linestyle='--')

#Add people A and B
ax.plot(person_A_x, road_y + person_y_offset, marker="o", markersize = 10, color="black")
ax.text(person_A_x+text_x_offset, road_y + person_y_offset, "A")

ax.plot(person_B_x, road_y + person_y_offset, marker="o", markersize = 10, color="black")
ax.text(person_B_x+text_x_offset, road_y + person_y_offset, "B")

# Add car
car, = ax.plot([],[],marker='o',markersize = 10, color = 'red')

# Wave circles
wave_circles = []
wave_lines = []
for i in range(7):
    circle, = ax.plot([], [], color='black', linestyle='-',fillstyle='none')
    wave_circles.append(circle)


def create_wavefront(center_x, center_y, radius, num_points=100):
    angles = np.linspace(0, 2*np.pi, num_points)
    x = center_x + radius * np.cos(angles)
    y = center_y + radius * np.sin(angles)
    return x, y

# Animation function
def animate(frame):
  car_x = car_start_x + frame * car_speed
  car.set_data([car_x], [car_y])  # Car is always on the road (car_y)
  
  time = frame/15
  v = car_speed  # Source velocity
    
  for i, circle in enumerate(wave_circles):
    radius = c * (time - (i/freq0))
    if radius > 0 and radius < max_radius :
      lambda_wave = (2*np.pi*c/(2*np.pi*freq0))
      x,y = create_wavefront(car_x-v*(time-(i/freq0)), car_y, radius)
      circle.set_data(x,y)
    else :
       circle.set_data([],[])
  return car, *wave_circles


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

# Save the animation as a GIF
ani.save('doppler_effect.gif', writer='pillow', fps=30)

plt.show()