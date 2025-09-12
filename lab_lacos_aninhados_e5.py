n = int(input("Digite n: "))
n3 = n ** 3
first = 1

print(f"n3 = {n3}")
print("consecutivos =")

while True:
    total = 0
    count = 0
    current = first
    
    # soma n ímpares consecutivos
    while count < n:
        total += current
        current += 2
        count += 1
    
    if total == n3:
        # imprime a sequência
        for k in range(n):
            print(first + 2 * k)
        break
    
    first += 2
