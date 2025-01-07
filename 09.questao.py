a = input("Informe a primeira string binária (composta apenas por 0 e 1): ")
b = input("Informe a segunda string binária (composta apenas por 0 e 1): ")

while len(a) != len(b) or not all(c in '01' for c in a + b):
    print("As strings devem ter o mesmo comprimento e conter apenas 0 ou 1.")
    a = input("Informe a primeira string binária (composta apenas por 0 e 1): ")
    b = input("Informe a segunda string binária (composta apenas por 0 e 1): ")

resultado_and = ""
resultado_or = ""
resultado_xor = ""

i = 0
while i < len(a):
    bit_a = int(a[i])
    bit_b = int(b[i])

    resultado_and += str(bit_a & bit_b)
    resultado_or += str(bit_a | bit_b)
    resultado_xor += str(bit_a ^ bit_b)

    i += 1

print("Resultado AND:", resultado_and)
print("Resultado OR:", resultado_or)
print("Resultado XOR:", resultado_xor)