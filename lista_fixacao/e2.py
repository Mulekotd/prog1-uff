total = 0
n = 0

while True:
    num = int(input())

    if num == 0:
        break

    total += num    
    n += 1

if n == 0:
    print("Nenhum número foi enviado.")
else:
    avg = total / n
    print(f"Média aritmética: {avg}")
