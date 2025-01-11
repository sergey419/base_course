import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import os

# Constants
fig_width = 8
fig_height = 8
x_min, x_max = -15, 15
y_min, y_max = -15, 15
num_stars = 2000
frame_interval = 50
animation_duration = 300
galaxy_radius = 10

# Function to calculate star positions in a spiral galaxy
def spiral_galaxy(num_stars, radius, frame):
    angles = np.random.uniform(0, 2 * np.pi, num_stars)
    distances = np.random.uniform(0, radius, num_stars)
    spiral_factor = 0.5  # Controls the tightness of the spiral
    
    # Use the angle to calculate the position of the star in the spiral arm. Make the rotation of the arms dependent on time
    x = distances * np.cos(angles + spiral_factor * distances + 0.02 * frame)
    y = distances * np.sin(angles + spiral_factor * distances + 0.02 * frame)
    return x, y


def update(frame):
    ax.clear()
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_aspect('equal')
    ax.set_xticks([]) #Remove ticks
    ax.set_yticks([])


    x, y = spiral_galaxy(num_stars, galaxy_radius, frame)

    # Plot the stars
    ax.scatter(x, y, s=1, c='white', alpha=0.8)  # s = star size, c = color


    return ax,

# Set up the figure and axes
fig = plt.figure(figsize=(fig_width, fig_height), dpi=200, facecolor='black')
ax = fig.add_subplot(111, facecolor='black')


# Animation setup
ani = FuncAnimation(fig, update, frames=np.arange(animation_duration), interval=frame_interval, blit=False)


# Attempt to save the animation to a GIF file
try:
    from matplotlib.animation import PillowWriter
    writer = PillowWriter(fps=20)  # Using PillowWriter directly
    ani.save("spiral_galaxy.gif", writer=writer, dpi=200)
    print("Animation saved to spiral_galaxy.gif")
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
    with open("spiral_galaxy.py", "w") as f:
        f.write(script_code)
    print("Script saved to spiral_galaxy.py")
except Exception as e:
    print(f"Error saving script: {e}")
    exit()

plt.show()