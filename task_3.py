import numpy as np
from lec_3_my_module import gravity_constant as g

t = float(input('Введите значение: '))
x0 = float(input('Введите значение: '))
y0 = float(input('Введите значение: '))
V0x = float(input('Введите значение: '))

x = x0 + V0x*t
y = y0 + V0x*t - (g*t**2)/2

coord = np.column_stack((t, x, y))
print(coord)







