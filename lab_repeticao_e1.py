n = int(input("Insira um valor para n: "))
mod = 2

while mod <= n:
    if n % mod == 0:
        print(mod)
    
    mod += 1
