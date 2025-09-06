a = int(input("Insira o valor de a: "))
b = int(input("Insira o valor de b: "))
c = int(input("Insira o valor de c: "))

if a == b and b == c:
    # Caso 1: todos iguais
    print("\nOs valores são iguais.")
elif a == b or a == c or b == c:
    # Caso 2: dois iguais
    if a == b:
        s = (a + b) - c
    elif a == c:
        s = (a + c) - b
    else:  # b == c
        s = (b + c) - a

    print("\nA resultado é:", s)
else:
    # Caso 3: todos diferentes
    if a >= b and a >= c:
        if b >= c:
            print(f"\n{a}, {b}, {c}")
        else:
            print(f"\n{a}, {c}, {b}")
    elif b >= a and b >= c:
        if a >= c:
            print(f"\n{b}, {a}, {c}")
        else:
            print(f"\n{b}, {c}, {a}")
    else:  # c é o maior
        if a >= b:
            print(f"\n{c}, {a}, {b}")
        else:
            print(f"\n{c}, {b}, {a}")
