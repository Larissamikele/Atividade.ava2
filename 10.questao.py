num = int(input("Digite um número de até 4 dígitos: "))

if num == 0 or str(num)[0] == str(num)[1] == str(num)[2] == str(num)[3]:
    print("O número indisponivel, pois tem todos os dígitos iguais.")
else:
    iterations = 0
    while num != 6174:
        num_str = str(num).zfill(4)
        desc = ''.join(sorted(num_str, reverse=True))
        asc = ''.join(sorted(num_str))
        
        num = int(desc) - int(asc)
        iterations += 1
        
        print(desc + " - " + asc + " = " + str(num))
    
    print("Nº de Iterações:", iterations)

