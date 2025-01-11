import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Constants
num_frames = 200
earth_radius = 2
rocket_x_start = 4
rocket_y_start = 2
rocket_speed = 0.03
grid_x_start = 8
grid_y_start = 0
max_grid_scale = 3

# Setup the plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-1, 12)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("Time Dilation Animation")

# Draw Earths
earth1 = plt.Circle((0, 0.5), earth_radius, color='skyblue')
earth2 = plt.Circle((0, -2.5), earth_radius, color='skyblue')
ax.add_patch(earth1)
ax.add_patch(earth2)

# Draw Rockets
rocket1, = ax.plot([], [], marker='>', markersize=15, color='grey')
rocket2, = ax.plot([], [], marker='>', markersize=15, color='grey')

# Draw Clocks
clock1, = ax.plot([], [], marker='o', markersize=10, color='black')
clock2, = ax.plot([], [], marker='o', markersize=10, color='black')
rocket_clock1, = ax.plot([], [], marker='o', markersize=10, color='black')
rocket_clock2, = ax.plot([], [], marker='o', markersize=10, color='black')

# Draw People
person1, = ax.plot([],[],marker="o",markersize=5,color = 'orange')
person2, = ax.plot([],[],marker="o",markersize=5,color = 'orange')
rocket_person1, = ax.plot([],[],marker="o",markersize=5,color = 'orange')
rocket_person2, = ax.plot([],[],marker="o",markersize=5,color = 'orange')


# Draw Grid
grid, = ax.plot([], [], marker='o', linestyle='-', markersize = 4, color='blue',alpha =0.6)
grid_x = np.array([])
grid_y = np.array([])
grid_points = np.array([])

def create_grid_points(scale, center_x, center_y):
    global grid_points
    
    grid_x = []
    grid_y = []
    for i in range(-3,4):
        for j in range(-3,4):
            for k in range(-3,4):
                 grid_x.append(scale*i + center_x)
                 grid_y.append(scale*j + center_y)
    
    grid_points = np.array(list(zip(grid_x, grid_y)))
    
    return grid_x,grid_y
    

def create_grid_lines(scale, center_x, center_y):
    x_lines = np.array([])
    y_lines = np.array([])
    
    x_lines = []
    y_lines = []

    for i in range(-3,4):
            for j in range(-3,4):
                x_lines.append([scale*i + center_x, scale*i+center_x])
                y_lines.append([scale*j+center_y-scale*3, scale*j+center_y+scale*3])
                x_lines.append([scale*j+center_x-scale*3, scale*j+center_x+scale*3])
                y_lines.append([scale*i+center_y, scale*i+center_y])
    x_lines = np.array(x_lines)
    y_lines = np.array(y_lines)

    return x_lines, y_lines


def animate(frame):
    
    rocket1_x = rocket_x_start + frame * rocket_speed
    rocket1_y = rocket_y_start
    rocket2_x = rocket_x_start + frame * rocket_speed
    rocket2_y = -rocket_y_start
    
    # Update rocket position
    rocket1.set_data(rocket1_x,rocket1_y)
    rocket2.set_data(rocket2_x, rocket2_y)

    # Update Person and Clock Positions
    clock1.set_data(0,0.5)
    clock2.set_data(0,-2.5)
    
    person1.set_data(0+earth_radius,0.5)
    person2.set_data(0+earth_radius,-2.5)
    
    rocket_clock1.set_data(rocket1_x, rocket1_y-0.5)
    rocket_clock2.set_data(rocket2_x, rocket2_y-0.5)
    rocket_person1.set_data(rocket1_x, rocket1_y+0.5)
    rocket_person2.set_data(rocket2_x, rocket2_y+0.5)

    # Update Grid
    scale = 1+ (np.sin(frame*0.05)*max_grid_scale)
    x, y = create_grid_points(scale,grid_x_start,grid_y_start)
    
    lines_x,lines_y = create_grid_lines(scale, grid_x_start,grid_y_start)
    grid.set_data(x,y)

    for i in range(len(lines_x)):
        ax.plot(lines_x[i], lines_y[i], color='blue', alpha =0.6, linewidth = 1.0)
    
    return rocket1, rocket2, clock1, clock2, rocket_clock1, rocket_clock2,person1,person2,rocket_person1,rocket_person2, grid,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

# Save the animation as a GIF
ani.save('time_dilation.gif', writer='pillow', fps=30)

plt.show()