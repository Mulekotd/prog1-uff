x = int(input("Número 1: "))
y = int(input("Número 2: "))

x_sum = 0
y_sum = 0

for i in range(1, x):
    if (x % i) == 0:
        x_sum += i

for j in range(1, y):
    if (y % j) == 0:
        y_sum += j

if (x_sum == y) and (y_sum == x):
    print(f"{x} e {y} são amiguxos!")
else:
    print(f"{x} e {y} não são amiguxos!")
