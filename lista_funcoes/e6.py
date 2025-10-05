def tribonacci(n: int) -> str:
    # Verifica se 'n' é positivo
    while n <= 0:
        n = int(input("Digite um valor positivo para n: "))

    seq = []

    for i in range(n):
        # Adiciona os valores base 1, 1, 2
        if i == 0 or i == 1:
            seq.append(1)
        elif i == 2:
            seq.append(2)
        else:
            seq.append(seq[i-1] + seq[i-2] + seq[i-3]) # Soma os três elementos anteriores consecutivos
        
    return ", ".join(map(str, seq))


print(tribonacci(12)) # Imprime 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504
