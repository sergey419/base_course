import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from mpl_toolkits.mplot3d import Axes3D
import os

# Constants
fig_width = 10
fig_height = 10
x_min, x_max = -10, 10
y_min, y_max = -10, 10
z_min, z_max = -3, 3
num_points = 50
frame_interval = 50
animation_duration = 300
wave_speed = 0.2 # Wave speed


# Create the base grid for the surface
x = np.linspace(x_min, x_max, num_points)
y = np.linspace(y_min, y_max, num_points)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)


def update(frame):
    ax.clear()
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_zlim(z_min, z_max)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_aspect('equal')

    # Create a circular disturbance that propagates outwards
    radius = wave_speed * frame
    amplitude = np.exp(-((X**2 + Y**2) - radius**2)**2 / 100)
    Z = amplitude * np.sin(0.5*radius - np.sqrt(X**2 + Y**2))


    # Plot the surface
    ax.plot_surface(X, Y, Z, cmap='ocean')

    return ax,

# Set up the figure and axes
fig = plt.figure(figsize=(fig_width, fig_height), dpi=200)
ax = fig.add_subplot(111, projection='3d')

# Animation setup
ani = FuncAnimation(fig, update, frames=np.arange(animation_duration), interval=frame_interval, blit=False)

# Attempt to save the animation to a GIF file
try:
    from matplotlib.animation import PillowWriter
    writer = PillowWriter(fps=20)  # Using PillowWriter directly
    ani.save("tsunami_formation.gif", writer=writer, dpi=200)
    print("Animation saved to tsunami_formation.gif")
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
    with open("tsunami_formation.py", "w") as f:
        f.write(script_code)
    print("Script saved to tsunami_formation.py")
except Exception as e:
    print(f"Error saving script: {e}")
    exit()

plt.show()