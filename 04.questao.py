
limite = 1000000


for numero in range(2, limite):
    if numero % 2 == 0 or numero % 5 == 0:
        
        digitos = str(numero)
        
        soma_potencias = 0
        for digito in digitos:
            soma_potencias += int(digito) ** 5
            
        if soma_potencias == numero:
            print(numero)