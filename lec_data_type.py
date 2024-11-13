def changer(a, b):
    a = 2
    b[0] = 'Good'

x = 10
L = [1, 2]
changer(x, L) 

print(x)
print(L)

L = [1,2]
changer(x, L[:])

print(L)



# комплексные числа
x = 3
y = 4

z = complex(x, y)
print(z)

w = complex(y, x)

print(z + w)

# Strings
s = 'hello'
print(s[0])

s[0] = 'H'

# Tuple
t = ( 1, 4, 9)
print(t)
print(t[0])
t[0] = 3

# list
l = [1, 4, 9]
l[0] = 3
print(l)

# Dict
d = {'al':4, 4:'al', 'str':'Hello'}
print(d['al'])