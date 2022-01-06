from myadd import add10

a = 1
b = 5
c = add10(a,b)
print(c)


x = [1, 2, 3]
y = [5, 6, 7]

z = list(map(add10, x, y))
print(z)