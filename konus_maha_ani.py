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
z_pos = 0

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

    # Create coordinates on the circumference of the cone
    num_points = 50
    theta = np.linspace(0, 2*np.pi, num_points)
    x_circle = x_apex + time * np.cos(np.pi - mach_angle) + time * np.sin(mach_angle)*np.cos(theta)
    y_circle = y_apex + time * np.sin(mach_angle)*np.sin(theta)
    z_circle = z_apex + time * np.sin(mach_angle) * np.cos(theta)

    # Create the sides of the cone with lines from the apex of the cone to the circle
    x_points = np.concatenate(([x_apex],x_circle))
    y_points = np.concatenate(([y_apex],y_circle))
    z_points = np.concatenate(([z_apex],z_circle))
    
    return x_apex, y_apex, z_apex, x_points, y_points, z_points, x_circle, y_circle, z_circle


def update(frame):
    ax.clear()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Mach Cone')
    ax.set_aspect('auto') # set aspect ratio automatically

    # Get coordinates of cone and object
    x_apex, y_apex, z_apex, x_points, y_points, z_points, x_circle, y_circle, z_circle = mach_cone_3d(velocity_ratio, frame, x_pos, y_pos, z_pos)

    # Plot the position of the object that produces the mach cone
    ax.scatter(x_apex, y_apex, z_apex, marker='o', s=30, color='black')

    # Plot the cone as a triangulated surface
    ax.plot_trisurf(x_points, y_points, z_points, color="gray", alpha = 0.6)
    
    #Plot sound waves
    num_wave_circles = 3
    for i in range(num_wave_circles):
        theta = np.linspace(0, 2*np.pi, 50)
        x = x_pos +  (i*frame/num_wave_circles) * np.cos(theta)
        y = y_pos + (i*frame/num_wave_circles) * np.sin(theta)
        z = z_pos * np.ones(len(x))
        ax.plot(x,y,z, color="gray", linestyle="--")
        
    # Set x and y limits
    ax.set_xlim(x_pos - frame, x_pos + (velocity_ratio + 1) * frame)
    ax.set_ylim(y_pos - 2 * frame, y_pos + 2 * frame)
    ax.set_zlim(z_pos - 2 * frame, z_pos + 2 * frame)

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