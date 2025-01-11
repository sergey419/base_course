import numpy as np
import matplotlib.pyplot as plt
import os

# Constants (using approximate values)
G = 6.674e-11     # Gravitational constant (N m^2/kg^2)
M = 1.989e30     # Mass of the sun (kg)
c = 299792458    # Speed of light (m/s)
radius_impact = 695700000 # Radius of the sun (m)


def calculate_light_deflection(radius_from_center):
    """Calculates the deflection angle of a light ray.

    Args:
        radius_from_center: The distance between the light ray and the center of mass.

    Returns:
       The light deflection angle (in radians).
    """
    # Check for radius to prevent division by 0
    if radius_from_center <= 0:
        return 0

    # Calculate deflection angle using the formula a = 4GM/(r * c^2)
    deflection_angle = (4 * G * M) / (radius_from_center * c**2)
    return deflection_angle

def simulate_light_path(initial_distance, distance_range, num_points = 100):
    """Simulates the path of a light ray as it passes a massive object.

    Args:
      initial_distance: The initial distance of the ray from the center of the object.
      distance_range: The range of distances to simulate in arbitrary units,
        1 = radius of the object
      num_points: The number of steps in the simulation.

    Returns:
      A tuple containing arrays for the x positions, y positions, and angles of the light path
    """
    
    # Create an array of distance steps from -distance_range to distance_range
    x_positions = np.linspace(-distance_range,distance_range, num_points)

    # Create arrays for y position and deflection angles
    y_positions = np.zeros_like(x_positions)
    angles = np.zeros_like(x_positions)

    # Set initial y position
    current_y = initial_distance
    
    # Initialise angle
    previous_angle = 0
    
    # Perform the simulation
    for i,x in enumerate(x_positions):
      
      # Calculate the distance from center
      distance_from_center = np.sqrt(current_y**2+x**2)*radius_impact

      # Calculate deflection
      deflection_angle = calculate_light_deflection(distance_from_center)
      
      # Calculate the deflection angle relative to the previous value
      angle = previous_angle - deflection_angle
      
      # Calculate change in y from the previous position using the new angle
      delta_y = np.tan(angle) * (x_positions[i] - x_positions[i-1]) if i > 0 else 0
        
      #Update position and angle
      current_y += delta_y
      angles[i] = angle
      y_positions[i] = current_y
      previous_angle = angle
    return x_positions, y_positions, angles

def plot_light_deflection(initial_distance = 2, distance_range=3, num_points = 500):
  """Plots the trajectory of a light ray as it bends due to gravity.
    Args:
      initial_distance: Initial distance of the ray from the object in units of radius.
      distance_range: Distance to simulate in units of object radius.
      num_points: Number of points to use in the simulation.
  """
  
  # Create figure and axes
  fig, ax = plt.subplots(figsize=(8, 6))
  ax.set_xlabel("Distance (radius)")
  ax.set_ylabel("Deflection (radius)")
  ax.set_title("Light Bending Due to Gravity")
  ax.set_aspect('equal') # Set aspect ratio to be equal
  ax.grid(True)

  # Get ray deflection
  x_positions, y_positions, angles = simulate_light_path(initial_distance, distance_range, num_points)

  # Plot light path
  ax.plot(x_positions, y_positions, label='Light Path')
  ax.plot(0,0, marker="o", markersize=10, color="orange", label="Massive Object")

  # Set x limits
  ax.set_xlim(-distance_range, distance_range)
  ax.legend()

  # Attempt to save the plot to a file
  try:
      plt.savefig("light_bending.png", dpi=300, bbox_inches='tight')
      print("Plot saved to light_bending.png")
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
      with open("light_bending.py", "w") as f:
          f.write(script_code)
      print("Script saved to light_bending.py")
  except Exception as e:
      print(f"Error saving script: {e}")
      exit()

  plt.show()


plot_light_deflection()