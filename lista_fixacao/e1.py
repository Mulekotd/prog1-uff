max_num = float('-inf')

while True:
    num = int(input())

    if num == 0:
        break

    if num > max_num:
        max_num = num

print(f"O maior número digitado foi {max_num}")
