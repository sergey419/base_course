import matplotlib.pyplot as plt
x = [1, 5, 5, 1, 1]
y = [5, 5, 1, 1, 5]

plt.plot(x, y, color='g', label='Graf 1', marker='o', ms=5)

plt.xlabel('coord - x')
plt.ylabel('coord - y')
plt.legend()
plt.title('Base')
plt.grid()
plt.axis('equal')

plt.savefig('fig_1.png')