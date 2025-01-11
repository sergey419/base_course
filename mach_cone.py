import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import os

def mach_cone(velocity_ratio, time, x_pos = 0, y_pos = 0):
    """Calculates the coordinates for a mach cone.
    
    Args:
    velocity_ratio: The ratio of object velocity to the speed of sound
    time: The time duration since the object started moving
    x_pos: The initial x position of the object
    y_pos: The initial y position of the object

    Return:
      A tuple of the x and y coordinates for the mach cone, and the position of the object.
    """

    # Calculate mach angle using arcsin
    mach_angle = np.arcsin(1 / velocity_ratio)

    # Calculate the x and y positions of the apex of the mach cone at the time `time`
    x_apex = x_pos + velocity_ratio * time
    y_apex = y_pos

    # Calculate the x and y positions of the cone in the time
    x1 = x_apex + time * np.cos(np.pi - mach_angle)
    y1 = y_apex + time * np.sin(np.pi - mach_angle)
    x2 = x_apex + time * np.cos(np.pi + mach_angle)
    y2 = y_apex + time * np.sin(np.pi + mach_angle)

    return [x_apex, y_apex], [x1,y1], [x2,y2]


def plot_mach_cone(velocity_ratio = 1.5, time_since_start = 5, x_object_pos = 0, y_object_pos = 0):
  """Plots a Mach cone with a specified velocity ratio and time, at an x and y position

    Args:
      velocity_ratio: The ratio of the object velocity to the speed of sound.
      time_since_start: The time since the object began moving.
      x_object_pos: The initial position of the object on the x axis
      y_object_pos: The initial position of the object on the y axis
    """

  # Create figure and axes
  fig, ax = plt.subplots(figsize=(8, 6))
  ax.set_aspect('equal')
  ax.set_xlabel('Distance (x)')
  ax.set_ylabel('Distance (y)')
  ax.set_title('Mach Cone')

  # Add the object
  apex, point1, point2 = mach_cone(velocity_ratio, time_since_start, x_object_pos, y_object_pos)
  ax.plot(apex[0], apex[1], marker='o', markersize=10, color="black", label='Object')
  
  # Create the Mach cone polygon
  polygon_points = np.array([apex,point1,point2])
  polygon = Polygon(polygon_points, closed=True, facecolor="gray", alpha=0.5, label = "Mach cone")
  ax.add_patch(polygon)
  ax.set_xlim(x_object_pos - time_since_start, x_object_pos + (velocity_ratio + 1) * time_since_start)
  ax.set_ylim(y_object_pos - 1 * time_since_start, y_object_pos + 1 * time_since_start)


  # Plot a circle to represent sound waves
  num_wave_circles = 3
  for i in range(num_wave_circles):
      circle = plt.Circle((x_object_pos, y_object_pos), i * time_since_start/num_wave_circles, fill=False, edgecolor = "gray", linestyle="--")
      ax.add_patch(circle)


  ax.legend()
  plt.grid(True)
  
  # Attempt to save the plot to a file
  try:
      plt.savefig("mach_cone.png", dpi=300, bbox_inches='tight')
      print("Plot saved to mach_cone.png")
  except Exception as e:
      print(f"Error saving plot to file: {e}")
      exit()
  
  # Attempt to save the script to a file
  try:
      # Get the current script's filename and read its content
      current_script_path = os.path.abspath(__file__)
      with open(current_script_path, 'r') as f:
          script_code = f.read()

      # Save the script to a new file
      with open("mach_cone.py", "w") as f:
          f.write(script_code)
      print("Script saved to mach_cone.py")
  except Exception as e:
      print(f"Error saving script: {e}")
      exit()

  plt.show()
  return

plot_mach_cone()