n = int(input("n? "))

print("A")
a = [int(input(f"{i}) ")) for i in range(n)]

print("B")
b = [int(input(f"{i}) ")) for i in range(n)]

print("C")
c = [int(input(f"{i}) ")) for i in range(n)]

# Cria D já com tamanho 3*n
d = [0] * (3 * n)

i = 0  # índice para A, B e C
j = 0  # índice para D

# Preenche D alternando os elementos de A, B e C
while i < n:
    d[j] = a[i]
    d[j+1] = b[i]
    d[j+2] = c[i]

    # Avança os índices
    i += 1
    j += 3

print(f"D = {d}")
