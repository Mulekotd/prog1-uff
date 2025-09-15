# Lê três variáveis 'a', 'b', 'c'
a = int(input("Insira o valor a: "))
b = int(input("Insira o valor b: "))
c = int(input("Insira o valor c: "))

# Atribuí ao 'total' zero como padrão
total = 0

# Se todos os valores forem iguais, o total permanece zero
if a == b == c:
    total = 0
else: # Caso contrário, soma ao 'total' apenas os valores únicos
    if a != b and a != c:
        total += a
    if b != a and b != c:
        total += b
    if c != a and c != b:
        total += c

# Imprime a soma
print(f"Soma {total}")
