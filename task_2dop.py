a = 4
b = 10
c = 6

if a < b + c or b < a + c or c < b + a:
    print('Такой треугольник существует')
else:
    print('Такого треуголтника не существует')
if a == b or b == c or a == c:
    print('Треугольник равнобедренный')
else:
    print('Треугольник не равнобедренный')
if a == b == c:
    print('Треугольник равносторонний')
else:
    print('треугольник не равносторонний')
if a != b != c:
    print('Треугольник разносторонний')