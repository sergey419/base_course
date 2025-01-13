import matplotlib.pyplot as plt
import numpy as np

# Constants
c = 343    # Speed of sound (m/s)
f0 = 440.0 # Original frequency (Hz)
omega0 = 2 * np.pi * f0  # Angular frequency (rad/s)

# Velocity range (from -c to +c but not exactly -c because that results in infinite wavelength)
v = np.linspace(-c + 10, c - 10, 400) # Velocity range between -333 to 333
v= v/2

# Calculate the wavelength using the Doppler effect formula.
wavelength = omega0 / (2 * np.pi * (c - v))

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(v, wavelength, label = "λ= ω0 / (2π(c - v))" )
plt.title("Doppler Effect: Wavelength vs Source Velocity")
plt.xlabel("Source Velocity v (m/s)")
plt.ylabel("Wavelength λ (m)")
plt.grid(True)
plt.legend()

#Annotate
plt.axvline(0, color='k', linestyle='--', label='v = 0')
plt.axvline(c, color='k', linestyle='dotted', label='v = c')
plt.axvline(-c, color='k', linestyle='dotted', label='v = -c')

plt.annotate(f'c={c}m/s', xy=(c+10, 10), xytext=(c+10, 20),
            arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate(f'-c={-c}m/s', xy=(-c-10, 10), xytext=(-c-30, 20),
            arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate(f'v=0', xy=(0, 10), xytext=(10, 20),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Save the plot as a PNG image
plt.savefig('doppler_graph.png')


plt.show()
