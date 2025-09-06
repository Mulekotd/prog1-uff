import random

d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
d3 = random.randint(1, 6)

max_value = d1
min_value = d1

if d2 > max_value:
    max_value = d2
if d3 > max_value:
    max_value = d3

if d2 < min_value:
    min_value = d2
if d3 < min_value:
    min_value = d3

print(f"Primeiro Dado {d1}")
print(f"Segundo Dado {d2}")
print(f"Terceiro Dado {d3}")

# Caso 1: três consecutivos
if max_value - min_value == 2 and (d1 != d2 and d2 != d3 and d1 != d3):
    print("Soma =", d1 + d2 + d3)
else:
    # Caso 2: números iguais
    if d1 == d2 and d1 != d3:
        print("Multiplicação =", d1 * d2)
    elif d1 == d3 and d1 != d2:
        print("Multiplicação =", d1 * d3)
    elif d2 == d3 and d2 != d1:
        print("Multiplicação =", d2 * d3)
    elif d1 == d2 == d3:
        print("Multiplicação =", d1 * d2 * d3)  # todos iguais
    else:
        # Caso 3: nenhum válido
        print("não deu")
