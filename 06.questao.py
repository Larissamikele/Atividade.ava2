
valor_inicial = int(input('Informe um valor: '))
razao = int(input('Informe a razão: '))

quantidade = int(input('Informe a quantidade de elementos da P.A: '))


pa = [] 
for i in range(quantidade):
    termo = valor_inicial + i * razao
    pa.append(termo)  

print('Os elementos da P.A são:', pa)  

if razao == 0:  
    print("A P.A. é constante.")
elif razao > 0:
    print("A P.A. é crescente.")
else:
    print("A P.A. é decrescente.")

soma_da_pa = sum(pa)  
print('A soma dos elementos da P.A é:', soma_da_pa)  
n = int(input("Digite a posição do elemento da P.A. que deseja consultar (n): "))


if n > 0:
    enesimo_termo = valor_inicial + (n - 1) * razao
    print(f"O elemento da posição {n} é:", enesimo_termo)
else:
    print("A posição deve ser um número inteiro positivo.")
