while True:
    # Lê os valores de 'n' e 'm' (limites superiores dos somatórios)
    n = int(input("n="))
    m = int(input("m="))

    series = 0

    # Calcula a soma dupla: i varia de 1 até n e j varia de 1 até m
    for i in range(1, n+1):
        for j in range(1, m+1):
            # Acumula cada termo da série conforme a fórmula
            series += ((i ** 2) * j) / ((3 ** i) * ((j * (3 ** i)) + (i * (3 ** j))))

    print(f"saitama = {series}")
    
    # Pergunta se o usuário quer repetir a operação
    print("Quer repetir a operação? (1 - Sim, 2 - Não)")
    retry = input()

    # Caso a resposta seja diferente de 1, quebra o loop
    if retry != "1":
        break
