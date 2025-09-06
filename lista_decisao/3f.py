a = int(input("Entre o valor do lado a: "))
b = int(input("Entre o valor do lado b: "))
c = int(input("Entre o valor do lado c: "))

# Desigualdade Triangular
is_triangle = (abs(b - c) < a < b + c) and (abs(a - c) < b < a + c) and (abs(a - b) < c < a + b)

# Leio três variáveis 'a', 'b', 'c'
# Verifico a condição de existência de um triângulo usando a desigualdade triangular
# Se realmente for possível formar um triângulo, analiso o tipo:
# - Se todos os lados forem iguais, é Equilátero
# - Se todos os lados forem diferentes, é Escaleno
# - Se apenas dois lados forem iguais, é Isósceles
# Caso a condição não seja atendida, exibo que não é possível formar um triângulo

if is_triangle:
    if a == b and b == c:
        print("Equilátero")
    elif a != b and b != c and a != c:
        print("Escaleno")
    elif a == b or b == c or a == c:
        print("Isóceles")
else:
    print("Não forma um triângulo")
