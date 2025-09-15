sb = float(input("Insira o seu salário bruto: "))
sl = sb  # Valor padrão, sem desconto

if sb >= 500 and sb < 800:
    sl = sb * (1 - 0.10)
elif sb >= 800 and sb < 1000:
    sl = sb * (1 - 0.15)
elif sb >= 1000:
    sl = sb * (1 - 0.80)

print(f"Salário Líquido: R$ {sl:.2f}")
