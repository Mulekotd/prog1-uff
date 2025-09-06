a = int(input("Insira o valor a: "))
b = int(input("Insira o valor b: "))
c = int(input("Insira o valor c: "))

total = 0

# Caso todos sejam iguais, a soma permanece 0
if a == b == c:
    pass
else:
    if a != b and a != c:
        total += a
    if b != a and b != c:
        total += b
    if c != a and c != b:
        total += c

print(f"Soma {total}")
