n = int(input())
k = 1

for i in range(1, 51):
    if i % 2 == 0: # Se o índice for par, faz multiplicação
        serie = k * n
    else: # Se o índice for ímpar, faz soma
        serie = k + n

    print(serie)
    k += 4 # Incrementa k de 4 em 4 para a próxima base da série
