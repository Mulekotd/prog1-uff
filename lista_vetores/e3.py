lista_a = list(map(int, input().split()))

n = len(lista_a)
ultimo_indice = n - 1

# (a) Inverte os valores de A
for i in range(n // 2):
    lista_a[i], lista_a[ultimo_indice - i] = lista_a[ultimo_indice - i], lista_a[i] # Swap dos valores

# Inicializa a lista B como uma cópia de A
lista_b = lista_a.copy()

# (b) Monta vetor de fatorial
for i, valor in enumerate(lista_b):
    if valor < 0: # Se o valor for negativo, retorna ele mesmo
        lista_b[i] = valor
        continue # Continua o loop

    # Caso-base: fatorial(0) = 1
    fatorial = 1

    for j in range(valor):
        fatorial *= j + 1

    lista_b[i] = fatorial

print(lista_b) # (c) Imprime a lista de fatorial
