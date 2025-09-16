# Lê os valores de 'a' e 'b'
a = int(input())
b = int(input())

# Algoritmo de Euclides (iterativo)
x = a
y = b

while y != 0:
    rest = x % y
    x, y = y, rest

mdc = x  # Quando y == 0, x é o mdc

if mdc == 1:
    print(f"{a} e {b} são bros!")
else:
    print(f"{a} e {b} não são bros!")
