def quocient_sum(n: int, m: int) -> float:
    # Verifica se 'n' é positivo
    while n <= 0:
        n = int(input("Digite um valor positivo para n: "))
    
    sequence_sum = 0.0
    i = 2
    j = 3

    # Enquanto não passar dos limites
    while i <= n and j <= m:
        sequence_sum += i / j
        i += 1
        j += 2
    
    return sequence_sum


print(quocient_sum(10, 21))
