n = int(input())
a = []
b = [0] * n # Cria o vetor B preenchido com zeros

# Preenche o vetor A com as entradas
for _ in range(n):
    num = int(input())
    a.append(num)

# Preenche o vetor B com os elementos de A invertidos
for i in range(n):
    b[n - 1 - i] = a[i]

print("Vetor A:", a)
print("Vetor B:", b)
