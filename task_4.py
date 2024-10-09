x = int(input())
a, b = 1, 1

for i in rahge(1, x + 1):
    print(i, '=>', a)
    a, b = b, a + b
    print(x, "=>", fibonacci(x))