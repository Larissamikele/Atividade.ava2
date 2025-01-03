def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a


a = int(input("Informe o primeiro valor: "))
b = int(input("Informe o segundo valor: "))


resultado = mdc(a, b)
print(f"O máximo divisor comum (MDC) de {a} e {b} é {resultado}")
