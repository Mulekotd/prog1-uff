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
# Caso 'a' = 'b' = 'c', o total permanece zero
# Se não, verifico a unicidade de cada variável e acumulo ao total

print(f"Soma {total}")
