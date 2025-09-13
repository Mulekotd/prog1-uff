while True:
    n = int(input("n="))
    m = int(input("m="))

    series = 0

    # Leio os limites superiores dos somatórios (n e m)
    # Calculo a soma dupla: i varia de 1 até n e j varia de 1 até m
    for i in range(1, n+1):
        for j in range(1, m+1):
            # Acumula cada termo da série conforme a fórmula
            series += ((i ** 2) * j) / ((3 ** i) * ((j * (3 ** i)) + (i * (3 ** j))))

    print(f"saitama = {series}")
    print("Quer repetir a operação? (1 - Sim, 2 - Não)")

    retry = input()

    if retry != "1":
        break
