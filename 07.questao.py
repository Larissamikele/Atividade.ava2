numerador = int(input("Informe um número: "))
if numerador <= 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    n = 1
    soma = 0
    triangular = False
    while soma < numerador:
        soma += n
        n += 1
        if soma == numerador:
            triangular = True
            break
    if triangular:
        print(f"O número {numerador} é triangular.")
    else:
        print(f"O número {numerador} não é triangular.")
