import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Constants
c = 1  # speed of sound (normalized)
freq0 = 1.0   # original frequency
car_start_x = -6
car_end_x = 6
car_y = -2.0  # Y-position of the road
car_speed = 0.05  # normalized car speed
max_radius = 3.5
num_frames = 200  # Increased number of frames
road_y = -2.0
person_A_x = -4
person_B_x = 4
person_y_offset = 0.5  # Offset for the people from the road
text_x_offset = 0.2    # Offset of text from the markers
max_circles = 10     # Maximum number of circles at a time

# Setup the plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-7, 7)  # Modified axis limits for smoother animation
ax.set_ylim(-5, 3)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
ax.set_facecolor('skyblue')
ax.set_title("Doppler Effect Animation")

# Add road
ax.plot([-7, 7], [road_y, road_y], color='grey', linewidth=4)
ax.plot([-7, 7], [road_y - 0.3, road_y - 0.3], color='white', linestyle='--')
ax.plot([-7, 7], [road_y + 0.3, road_y + 0.3], color='white', linestyle='--')


# Add people A and B
ax.plot(person_A_x, road_y + person_y_offset, marker="o", markersize=10, color="black")
ax.text(person_A_x + text_x_offset, road_y + person_y_offset, "A")

ax.plot(person_B_x, road_y + person_y_offset, marker="o", markersize=10, color="black")
ax.text(person_B_x + text_x_offset, road_y + person_y_offset, "B")

# Add car
car, = ax.plot([], [], marker='o', markersize=10, color='red')
wave_circles = []


def create_wavefront(center_x, center_y, radius, num_points=100):
    angles = np.linspace(0, 2 * np.pi, num_points)
    x = center_x + radius * np.cos(angles)
    y = center_y + radius * np.sin(angles)
    return x, y

# Animation function
def animate(frame):
    global wave_circles
    car_x = car_start_x + (frame / num_frames) * (car_end_x - car_start_x)
    car.set_data([car_x], [car_y])

    time = frame / 15
    v = car_speed  # Source velocity
    
    # Generate new wave circle, if space is available
    if len(wave_circles) < max_circles:
        radius = c*(time - 0)
        x,y = create_wavefront(car_x-v*time, car_y, radius)
        circle, = ax.plot(x,y, color='black', linestyle='-',fillstyle='none')
        wave_circles.append({'circle': circle, 'start_time':time})
    
    #Update the positions of existing circles
    for wave_data in wave_circles :
        circle= wave_data['circle']
        start_time=wave_data['start_time']
        radius = c*(time-start_time)
        if radius>0 and radius < max_radius:
           x,y = create_wavefront(car_x-v*start_time, car_y, radius)
           circle.set_data(x,y)

    #Remove the old circles
    circles_to_remove = []
    for wave_data in wave_circles :
        if c*(time- wave_data['start_time']) >= max_radius :
           circles_to_remove.append(wave_data)

    for circle_to_remove in circles_to_remove :
       wave_circles.remove(circle_to_remove)

    return car, *[circle_data['circle'] for circle_data in wave_circles]

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

# Save the animation as a GIF
ani.save('doppler_effect.gif', writer='pillow', fps=30)

plt.show()