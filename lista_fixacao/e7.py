num = int(input("N="))
is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

print(f"{num} não é primo") if not is_prime else print(f"{num} é primo")
