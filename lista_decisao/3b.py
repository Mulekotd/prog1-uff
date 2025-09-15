# Lê três variáveis 'a', 'b', 'c'
a = int(input("Insira o valor a: "))
b = int(input("Insira o valor b: "))
c = int(input("Insira o valor c: "))

# Calcula o produto, a soma e a média aritmética dos valores
prod = a * b * c 
total = a + b + c
avg = total / 3

# Verifica o maior e o menor valor entre as variáveis, realizando comparações em cascata de 'a' até 'c'
max_value = a
min_value = a

if b > max_value:
    max_value = b
if c > max_value:
    max_value = c

if b < min_value:
    min_value = b
if c < min_value:
    min_value = c

# Imprime o resultado da soma, produto, média, valor máximo e valor mínimo
print(f"\nSoma: {total}")
print(f"Produto: {prod}")
print(f"Média: {avg}")
print(f"Máximo: {max_value}")
print(f"Mínimo: {min_value}")
