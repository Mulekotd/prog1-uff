a = int(input("Insira o valor a: "))
b = int(input("Insira o valor b: "))
c = int(input("Insira o valor c: "))

total = a + b + c

if (a + b == c) or (b + c == a) or (c + a == b):
    print("soma")
elif (a * b == c) or (b * c == a) or (c * a == b):
    print("multi")
else:
    print("par" if total % 2 == 0 else "impar")
