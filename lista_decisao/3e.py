a = int(input("Insira o valor a: "))
b = int(input("Insira o valor b: "))
c = int(input("Insira o valor c: "))

total = a + b + c

# Leio três variáveis 'a', 'b' e 'c'
# Depois, verifico se a soma de dois deles é igual ao terceiro. Se for, imprimo "soma"
# Se não, verifico se o produto de dois deles é igual ao terceiro. Se for, imprimo "multi"
# Caso nenhuma das condições seja atendida, somo os três valores (total) e vejo se o resultado é par ou ímpar
# Se o resto da divisão por 2 for 0, imprimo "par"
# Caso contrário, imprimo "impar"

if (a + b == c) or (b + c == a) or (c + a == b):
    print("soma")
elif (a * b == c) or (b * c == a) or (c * a == b):
    print("multi")
else:
    print("par" if total % 2 == 0 else "impar")
