# Lê três variáveis 'a', 'b' e 'c'
a = int(input("Insira o valor a: "))
b = int(input("Insira o valor b: "))
c = int(input("Insira o valor c: "))

# Verifica se a soma de dois deles é igual ao terceiro
if (a + b == c) or (b + c == a) or (c + a == b):
    # Se for, imprime "soma"
    print("soma")
elif (a * b == c) or (b * c == a) or (c * a == b): # Verifica se o produto de dois deles é igual ao terceiro
    # Se for, imprime "multi"
    print("multi")
else: # Caso contrário
    # Somo os três valores (total)
    total = a + b + c

    # Verifica se o resto da divisão por 2 é 0
    if total % 2 == 0:
        # Se for, imprime "par"
        print("par")
    else:
        # Caso contrário, imprime "impar"
        print("impar")
