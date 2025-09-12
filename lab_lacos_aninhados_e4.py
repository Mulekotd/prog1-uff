n = int(input("n="))
m = int(input("m="))

series = 0

for i in range(1, n):
    for j in range(1, m):
        series += ((i ** 2) * j) / ((3 ** i) * ((j * (3 ** i)) + (i * (3 ** j))))

print(f"saitama = {series}")
