valor_inicial = int(input('Digite o valor inicial da P.G.: '))
razao = float(input('Digite a razão da P.G.: '))

quantidade = int(input('Digite a quantidade de elementos (positivos) da P.G.: '))
elementos = []
soma = 0

for i in range(quantidade):
    elemento = valor_inicial * (razao ** i)
    elementos.append(elemento)
    soma += elemento

print('Elementos da P.G.:', elementos)

if razao == 1:
    print('A P.G. é constante.')
elif razao > 0:
    if razao > 1:
        print('A P.G. é crescente.')
    elif razao < 1:
        print('A P.G. é decrescente.')
elif razao < 0:
    print('A P.G. é oscilante.')

print('Soma dos elementos da P.G.:', soma)