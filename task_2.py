
import numpy as np
h = 100
alpha = 45
beta = 35
gravity_constant = 9,8
V=(((gravity_constant*h*np.tan(beta)**2)/(2*np.cos(alpha)**2)*(1 -np.tan(beta)*np.tan(alpha))))**0.5
print(V)



