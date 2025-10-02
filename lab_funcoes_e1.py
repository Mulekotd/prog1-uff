def sum_odd_even(vector):
    return sum(num for i, num in enumerate(vector) if i % 2 == 0 and num % 2 != 0)

print(sum_odd_even([1,1,3,1,8,1])  ) # resultado: 1+3 = 4
print(sum_odd_even([]) )          	 # resultado: 0
