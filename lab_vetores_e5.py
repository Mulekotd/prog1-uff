n = int(input("n?"))

print("A")
a = [int(input(f"{i}) ")) for i in range(n)]

print("B")
b = [int(input(f"{i}) ")) for i in range(n)]

print("C")
c = [int(input(f"{i}) ")) for i in range(n)]

d = []

# Intercala os elementos de A, B e C
for i in range(n):
    d.append(a[i])  # Adiciona elemento de A
    d.append(b[i])  # Adiciona elemento de B
    d.append(c[i])  # Adiciona elemento de C

print(f"D = {d}")
