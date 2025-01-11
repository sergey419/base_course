import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from mpl_toolkits.mplot3d import Axes3D
import os

# Constants
fig_width = 8
fig_height = 8
frame_interval = 50
animation_duration = 300
velocity_ratio = 1.5
x_pos = 0
y_pos = 0
z_pos = 0 # object z position at the start


def mach_cone_3d(velocity_ratio, time, x_pos, y_pos, z_pos):
    """Calculates the coordinates for a 3D mach cone.

    Args:
        velocity_ratio: The ratio of object velocity to the speed of sound.
        time: The time duration since the object started moving.
        x_pos: The initial x position of the object.
        y_pos: The initial y position of the object.
        z_pos: The initial z position of the object

    Returns:
        A tuple of x, y, and z coordinates for the cone.
    """
    mach_angle = np.arcsin(1 / velocity_ratio)

    # Calculate the position of the apex of the mach cone
    x_apex = x_pos + velocity_ratio * time
    y_apex = y_pos
    z_apex = z_pos

    # Calculate the coordinates at the circumference of the cone
    num_points = 50
    theta = np.linspace(0, 2*np.pi, num_points)
    x = x_apex + time * np.cos(np.pi - mach_angle) + time * np.sin(mach_angle)*np.cos(theta)
    y = y_apex + time * np.sin(mach_angle)*np.sin(theta)
    z = z_apex + time * np.sin(mach_angle) * np.cos(theta)

    # Create points for the lateral surface
    x_side = np.linspace(x_apex, x_apex + time * np.cos(np.pi - mach_angle), num_points)
    y_side = y_apex * np.ones(num_points)
    z_side = z_apex * np.ones(num_points)

    return x_apex, y_apex, z_apex, x, y, z, x_side, y_side, z_side


def update(frame):
    ax.clear()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Mach Cone')
    ax.set_aspect('auto') # set aspect ratio automatically

    # Get coordinates of cone and object
    x_apex, y_apex, z_apex, x, y, z, x_side, y_side, z_side = mach_cone_3d(velocity_ratio, frame, x_pos, y_pos, z_pos)

    # Plot the position of the object that produces the mach cone
    ax.scatter(x_apex, y_apex, z_apex, marker='o', s=30, color='black')

    # Plot cone surface
    ax.plot_surface(x.reshape(50,1), y.reshape(50,1), z.reshape(50,1), alpha = 0.6, color='gray')

    # Plot lines from the object to the surface of the cone
    for i in range(len(x_side)):
        ax.plot([x_apex, x_side[i]], [y_apex, y_side[i]], [z_apex, z_side[i]], color="gray", linestyle="--")

    # Set x and y limits
    ax.set_xlim(x_pos - frame, x_pos + (velocity_ratio + 1) * frame)
    ax.set_ylim(y_pos - 2 * frame, y_pos + 2 * frame)
    ax.set_zlim(z_pos - 2 * frame, z_pos + 2 * frame)

    #Plot sound waves
    num_wave_circles = 3
    for i in range(num_wave_circles):
        theta = np.linspace(0, 2*np.pi, 50)
        x = x_pos +  (i*frame/num_wave_circles) * np.cos(theta)
        y = y_pos + (i*frame/num_wave_circles) * np.sin(theta)
        z = z_pos * np.ones(len(x))
        ax.plot(x,y,z, color="gray", linestyle="--")

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
    ani.save("mach_cone_animation_3d.gif", writer=writer, dpi=200)
    print("Animation saved to mach_cone_animation_3d.gif")
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
    with open("mach_cone_animation_3d.py", "w") as f:
        f.write(script_code)
    print("Script saved to mach_cone_animation_3d.py")
except Exception as e:
    print(f"Error saving script: {e}")
    exit()

plt.show()