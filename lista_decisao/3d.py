a = int(input("Insira o valor a: "))
b = int(input("Insira o valor b: "))
c = int(input("Insira o valor c: "))

total = 0

if a == b == c:
    pass
else:
    if a != b and a != c:
        total += a
    if b != a and b != c:
        total += b
    if c != a and c != b:
        total += c

# Leio três variáveis 'a', 'b', 'c'
# Atribuo ao 'total' o valor 0 como padrão
# Se todos os valores forem iguais, o total permanece 0
# Caso contrário, somo ao 'total' apenas os valores únicos

print(f"Soma {total}")
