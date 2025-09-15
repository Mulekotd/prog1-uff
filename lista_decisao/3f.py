# Lê três variáveis 'a', 'b', 'c'
a = int(input("Entre o valor do lado a: "))
b = int(input("Entre o valor do lado b: "))
c = int(input("Entre o valor do lado c: "))

# Desigualdade Triangular
is_triangle = (abs(b - c) < a < b + c) and (abs(a - c) < b < a + c) and (abs(a - b) < c < a + b)

# Verifica a condição de existência de um triângulo usando a desigualdade triangular (is_triangle)
if is_triangle:
    # Sendo possível formar um triângulo, analisa o seu tipo
    # Se todos os lados forem iguais, é Equilátero
    if a == b and b == c:
        print("Equilátero")
    elif a != b and b != c and a != c: # Se todos os lados forem diferentes, é Escaleno
        print("Escaleno")
    elif a == b or b == c or a == c: # Se apenas dois lados forem iguais, é Isósceles
        print("Isóceles")
else: # Caso contrário
    # Exibo que não é possível formar um triângulo
    print("Não forma um triângulo")
