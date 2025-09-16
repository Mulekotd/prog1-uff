while True:
    n = int(input("Digite o valor de n: "))

    a = 2
    b = 2
    c = 3
    d = 3

    # Imprime os 4 primeiros se n >= 4
    if n >= 1:
        print(a)
    if n >= 2:
        print(b)
    if n >= 3:
        print(c)
    if n >= 4:
        print(d)

    # Gera a partir do quinto número
    for i in range(5, n+1):
        serie = (2 * (d + c)) - (b * a)
        print(serie)
        a, b, c, d = b, c, d, serie

    retry = input("Deseja repetir o processo com outro n? (1 - Sim, 2 - Não): ")

    if retry != "1":
        break
