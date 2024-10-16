import numpy as np

a = [1, 2, 4]

b = np.array(a)

print(type(a))
print(type(b))

print(b * b)
print(b / b)
print(b - b)
print(b + b)
print(b ** 0.5)
print(b % b)

c = np.append(b, 'Good')
print(c)
