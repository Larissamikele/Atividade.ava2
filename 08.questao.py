numero = int(input("Informe um número positivo: "))
if numero <= 0:
    print("Insira um número positivo.")
else:
    temp = numero
    qtd_digitos = 0
    while temp > 0:
        temp //= 10
        qtd_digitos += 1

    temp = numero
    soma = 0
    while temp > 0:
        digito = temp % 10
        soma += digito ** qtd_digitos
        temp //= 10

    if soma == numero:
        print(f"O número {numero} é um número de Armstrong.")
    else:
        print(f"O número {numero} não é um número de Armstrong.")
