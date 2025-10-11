n = int(input())
i = 0

# Solução com while
while i < n:
    num1, num2, num3 = map(int, input().split())
    max_num = num1

    if max_num < num2:
        max_num = num2
    if max_num < num3:
        max_num = num3
    
    print(f"Maior valor: {max_num}")

    i += 1

# Solução com for
for _ in range(n):
    num1, num2, num3 = map(int, input().split())
    max_num = num1

    if max_num < num2:
        max_num = num2
    if max_num < num3:
        max_num = num3
    
    print(f"Maior valor: {max_num}")
