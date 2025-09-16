n = int(input("Quantos números você quer digitar? "))

prev = int(input())
crescent = True # Assume que está em ordem crescente

for i in range(2, n+1):
    curr = int(input())
    
    if curr < prev: # Se quebrar a ordem
        crescent = False
    
    prev = curr # Atual vira o anterior na próxima iteração

if crescent:
    print("Os números estão em ordem crescente.")
else:
    print("Os números não estão em ordem crescente.")
