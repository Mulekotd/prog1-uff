arr = [int(input()) for _ in range(20)]

def modify_list(arr : list = []) -> list:
    for i, curr in enumerate(arr):
        if curr < 0:
            arr[i] = 0
        elif curr < 10:
            arr[i] = 1
        else:
            arr[i] = 2

    return arr


print(modify_list(arr))
