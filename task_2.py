n = 10
b1 = 1
q = 3
g_prog = [b1]
for _ in range(n - 1):
    g_prog.append(g_prog[-1] * q)
print(*g_prog)
print(sum(g_prog))
