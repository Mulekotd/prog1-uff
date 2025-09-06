a = int(input("Entre o valor do lado a: "))
b = int(input("Entre o valor do lado b: "))
c = int(input("Entre o valor do lado c: "))

# Condição de existência do triângulo
is_triangle = (abs(b - c) < a < b + c) and (abs(a - c) < b < a + c) and (abs(a - b) < c < a + b)

if is_triangle:
    if a == b and b == c:
        print("Equilátero")
    elif a != b and b != c and a != c:
        print("Escaleno")
    elif a == b or b == c or a == c:
        print("Isóceles")
else:
    print("Não forma um triângulo")
