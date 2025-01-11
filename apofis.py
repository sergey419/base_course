import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, MovieWriterRegistry
from mpl_toolkits.mplot3d import Axes3D
import os

# Constants
fig_width = 10
fig_height = 10
x_min, x_max = -15, 15
y_min, y_max = -15, 15
z_min, z_max = -15, 15
earth_radius = 6
asteroid_radius = 1.5
frame_interval = 50
animation_duration = 300


# Initial positions and velocities
earth_x = 0
earth_y = 0
earth_z = 0
asteroid_x = 12
asteroid_y = 5
asteroid_z = 5
asteroid_vx = -0.07
asteroid_vy = -0.01
asteroid_vz = -0.01

def create_sphere(ax, x, y, z, radius, color, alpha=1):
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    sphere_x = x + radius * np.outer(np.cos(u), np.sin(v))
    sphere_y = y + radius * np.outer(np.sin(u), np.sin(v))
    sphere_z = z + radius * np.outer(np.ones(np.size(u)), np.cos(v))
    sphere = ax.plot_surface(sphere_x, sphere_y, sphere_z, color=color, alpha=alpha)
    return sphere

def update(frame):
    ax.clear()
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_zlim(z_min, z_max)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_aspect('equal')


    # Update asteroid position
    global asteroid_x, asteroid_y, asteroid_z
    asteroid_x += asteroid_vx
    asteroid_y += asteroid_vy
    asteroid_z += asteroid_vz


    # Collision detection
    distance = np.sqrt((earth_x - asteroid_x)**2 + (earth_y - asteroid_y)**2 + (earth_z - asteroid_z)**2)
    if distance <= earth_radius + asteroid_radius:
        asteroid_vx = 0 # stop asteroid from moving
        asteroid_vy = 0
        asteroid_vz = 0
        asteroid_radius *= 2 #make asteroid grow on impact


    # Draw Earth and Asteroid
    create_sphere(ax, earth_x, earth_y, earth_z, earth_radius, 'blue')
    create_sphere(ax, asteroid_x, asteroid_y, asteroid_z, asteroid_radius, 'gray')


    return ax,

# Set up the figure and axes
fig = plt.figure(figsize=(fig_width, fig_height), dpi=200)
ax = fig.add_subplot(111, projection='3d')


# Animation setup
ani = FuncAnimation(fig, update, frames=np.arange(animation_duration), interval=frame_interval, blit=False)


# Attempt to save the animation to a GIF file
try:
    writer = MovieWriterRegistry.registered['ffmpeg']
    # Assign the result to a variable (ani) so that the animation is saved
    ani.save("apophis_impact.gif", writer=writer(fps=20), dpi=200)
    print("Animation saved to apophis_impact.gif")
except Exception as e:
    print(f"Error saving animation to GIF: {e}")
    exit()

# Attempt to save the script to a file
try:
    # Get the current script's filename and read its content
    current_script_path = os.path.abspath(__file__)
    with open(current_script_path, 'r') as f:
        script_code = f.read()

    # Save the script to a new file
    with open("apophis_impact.py", "w") as f:
        f.write(script_code)
    print("Script saved to apophis_impact.py")
except Exception as e:
    print(f"Error saving script: {e}")
    exit()

plt.show()