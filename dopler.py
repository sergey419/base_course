import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import os

# Constants
fig_width = 8
fig_height = 6
x_min, x_max = -10, 10
y_min, y_max = -2, 2
num_points = 500
frame_interval = 50
animation_duration = 300
wave_speed = 1.0
source_speed = 0.5

def doppler_effect(time, source_x, source_speed, wave_speed, frequency_hz = 1):
    """Simulates the doppler effect.

    Args:
        time: the time from the start of the simulation
        source_x: the x position of the wave source
        source_speed: the speed of the source
        wave_speed: the speed of the wave
        frequency_hz: the source frequency

    Returns:
      a tuple of the x positions, and wave positions for each value of x
    """
    # Calculate frequency using time and the formula
    wave_frequency_hz = frequency_hz * (wave_speed - source_speed) / wave_speed
    wave_frequency_rad = 2*np.pi*wave_frequency_hz

    # Create the x axis
    x = np.linspace(x_min, x_max, num_points)

    # Calculate the wave position in space
    y = np.sin(wave_frequency_rad * (x - source_x) / wave_speed)

    return x, y

def update(frame):
    ax.clear()
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xlabel('Position (x)')
    ax.set_ylabel('Wave Amplitude')
    ax.set_title('Doppler Effect')
    ax.grid(True)

    # Calculate source position
    source_x = -source_speed * frame
    x, y = doppler_effect(frame, source_x, source_speed, wave_speed)

    # Plot the wave
    ax.plot(x, y, color='blue')

    # Plot the source
    ax.plot(source_x, 0, marker='o', markersize=10, color='red', label="Source")

    ax.legend()
    return ax,

# Set up the figure and axes
fig = plt.figure(figsize=(fig_width, fig_height), dpi=200)
ax = fig.add_subplot(111)


# Animation setup
ani = FuncAnimation(fig, update, frames=np.arange(animation_duration), interval=frame_interval, blit=False)

# Attempt to save the animation to a GIF file
try:
    from matplotlib.animation import PillowWriter
    writer = PillowWriter(fps=20)  # Using PillowWriter directly
    ani.save("doppler_effect.gif", writer=writer, dpi=200)
    print("Animation saved to doppler_effect.gif")
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
    with open("doppler_effect.py", "w") as f:
        f.write(script_code)
    print("Script saved to doppler_effect.py")
except Exception as e:
    print(f"Error saving script: {e}")
    exit()

plt.show()