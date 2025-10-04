def normalize(grades):
    max_num = max(grades)
    min_num = min(grades)
    
    diff = max_num - min_num

    if diff == 0:
        return [0.0 for _ in grades] # Evita divisão por zero

    return [(grade - min_num) / diff for grade in grades]


print(normalize([50, 70, 100, 80, 60, 90]))  # [0.0, 0.4, 1.0, 0.6, 0.2, 0.8]
print(normalize([10, 20, 30, 40, 50, 60]))   # [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
print(normalize([30, 90]))                   # [0.0, 1.0]
