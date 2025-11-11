def pivot(v: list[int], p: int) -> int:
    n = len(v)
    value = v[p]

    minors = ""
    bigger = ""

    for i in range(n-1):
        if v[i] == value:
            continue

        if v[i] < value: minors += str(v[i])
        else: bigger += str(v[i])
    
    k = 0
    for m in minors:
        v[k] = int(m)
        k += 1
    
    v[k] = value
    k += 1

    for b in bigger:
        v[k] = int(b)
        k += 1

    return v.index(value)

print(pivot([6, 3, 7, 9, 2, 8], 2))
