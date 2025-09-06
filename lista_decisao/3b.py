a = int(input("Insira o valor a: "))
b = int(input("Insira o valor b: "))
c = int(input("Insira o valor c: "))

prod = a * b * c 
total = a + b + c
avg = total / 3

# Inicialmente, assumo que o maior e menor são 'a'
max_value = a
min_value = a

# Verificando o maior
if b > max_value:
    max_value = b
if c > max_value:
    max_value = c

# Verificando o menor
if b < min_value:
    min_value = b
if c < min_value:
    min_value = c

# Leio três variáveis 'a', 'b', 'c'
# Calculo o produto (*), a soma (+) e a média aritmética dos valores
# Também verifico o maior e o menor valor entre as variáveis, realizando comparações em cascata de 'a' até 'c'

print(f"\nSoma: {total}")
print(f"Produto: {prod}")
print(f"Média: {avg}")
print(f"Máximo: {max_value}")
print(f"Mínimo: {min_value}")
