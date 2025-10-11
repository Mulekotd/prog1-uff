num = int(input())
last_prime = None

for i in range(2, num):
    is_prime = True

    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        last_prime = i

print(f"O maior primo menor que {num} é {last_prime}")
