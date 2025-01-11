import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import os

# Constants
fig_width = 8
fig_height = 6
x_min, x_max = -10, 10
y_min, y_max = -2, 2
num_points = 20
frame_interval = 50
animation_duration = 300

# Spatial setup
x = np.linspace(x_min, x_max, num_points)

def update(frame):
    plt.cla() #Clear the previous frame
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xlabel("Position (x)")
    plt.ylabel("Field Strength")
    plt.title("Electromagnetic Wave Propagation")
    plt.grid(True)


    # Calculate E and B fields at different points, at different times
    E = np.sin(x + 0.1 * frame)  # Electric Field
    B = np.cos(x + 0.1 * frame)   # Magnetic Field


    # Plotting
    plt.plot(x, E, label='E-field', color='blue', marker='o', linestyle='-')
    plt.plot(x, B, label='B-field', color='red', marker='x', linestyle='-')
    plt.legend()

    return plt,

# Set up the figure and axes
fig = plt.figure(figsize=(fig_width, fig_height), dpi=200)

# Animation setup
ani = FuncAnimation(fig, update, frames=np.arange(animation_duration), interval=frame_interval, blit=False)


# Attempt to save the animation to a GIF file
try:
    from matplotlib.animation import PillowWriter
    writer = PillowWriter(fps=20)  # Using PillowWriter directly
    ani.save("electromagnetic_wave_propagation.gif", writer=writer, dpi=200)
    print("Animation saved to electromagnetic_wave_propagation.gif")
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
    with open("electromagnetic_wave_propagation.py", "w") as f:
        f.write(script_code)
    print("Script saved to electromagnetic_wave_propagation.py")
except Exception as e:
    print(f"Error saving script: {e}")
    exit()

plt.show()