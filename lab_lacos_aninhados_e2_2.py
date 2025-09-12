min_value = 1000
max_value = 1500

i = min_value

while i <= max_value:
    j = i + 1

    while j <= max_value:
        sum_i = 0
        divider = 1

        while divider < i:
            if i % divider == 0:
                sum_i += divider
            divider += 1

        sum_j = 0
        divider = 1

        while divider < j:
            if j % divider == 0:
                sum_j += divider
            divider += 1

        if sum_i == j and sum_j == i:
            print(f"{i} e {j} são amiguxos!")

        j += 1
    i += 1
