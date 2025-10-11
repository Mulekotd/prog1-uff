n = int(input())
odd_counter = 0
even_counter = 0

i = 0

# Solução com while
while i < n:
    num = int(input())

    if num % 2 == 0:
        even_counter += 1
    else:
        odd_counter += 1

    i += 1

# Solução com for
for _ in range(n):
    num = int(input())

    if num % 2 == 0:
        even_counter += 1
    else:
        odd_counter += 1

print(f"Qtd. de pares {even_counter}")
print(f"Qtd. de ímpares {odd_counter}")
