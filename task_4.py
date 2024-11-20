import numpy as np
N = int(input('Введите элемент: '))
M = int(input('Введите элемент: '))
trigonometry_array = np.zeros((N, M))
for i in range(N):
    for j in range(M):
        summ = np.sin(N * i + M *j + 1)
        if summ < 0:
            trigonometry_array[i, j] = 0
        else:
            trigonometry_array[i, j] = summ
print(trigonometry_array)

