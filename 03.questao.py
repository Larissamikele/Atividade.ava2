
n = int(input("Informe a quantidade de fatores primos: "))

numero = 2
consecutivos = []


while len(consecutivos) < n:
    fatores = set()
    num_atual = numero
    divisor = 2
    
    
    while num_atual > 1:
        while num_atual % divisor == 0:
            fatores.add(divisor)
            num_atual //= divisor
        divisor += 1
    
    
    if len(fatores) == n:
        consecutivos.append(numero)
        if len(consecutivos) > 1 and consecutivos[-1] != consecutivos[-2] + 1:
            consecutivos = [numero]  
    else:
        consecutivos = []
    
    numero += 1


print(f"Os primeiros {n} números consecutivos que possuem exatamente {n} fatore