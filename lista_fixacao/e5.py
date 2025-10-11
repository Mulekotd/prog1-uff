num = int(input("N="))

while num < 2 or num > 9:
    num = int(input("N="))

for i in range(10):
    index = i + 1
    print(f"{num}x{index} = {num * index}", end="; ")
