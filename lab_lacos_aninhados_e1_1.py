n = int(input("n = "))

x, y, z = 2, 5, 8

if n >= 1:
    print(x)
if n >= 2:
    print(y)
if n >= 3:
    print(z)

i = 3

while i < n:
    next_num = z - (x + y)
    print(next_num)

    x, y, z = y, z, next_num
    i += 1
