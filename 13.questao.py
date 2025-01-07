x_inicial, y_inicial = int(input("Digite a coordenada X inicial: ")), int(input("Digite a coordenada Y inicial: "))

x, y = x_inicial, y_inicial
movimentos = input("Digite a sequência de movimentos: ")

movimentos_validos, contagem_validos = "", 0
direcoes = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0), 'O': (-1, 1), 'N': (1, 1), 'E': (1, -1), 'W': (-1, -1)}

for movimento in movimentos:
    if movimento in direcoes:
        dx, dy = direcoes[movimento]
        x, y = x + dx, y + dy
        movimentos_validos += movimento
        contagem_validos += 1

def quadrante(x, y):
    if x > 0 and y > 0: return "I"
    if x < 0 and y > 0: return "II"
    if x < 0 and y < 0: return "III"
    if x > 0 and y < 0: return "IV"
    if x == 0 and y != 0: return "Sobre o eixo Y"
    if x != 0 and y == 0: return "Sobre o eixo X"
    return "Origem"

print(f"Posição inicial: ({x_inicial}, {y_inicial})")
print(f"Posição final: ({x}, {y})")
print(f"Quantidade de movimentos válidos: {contagem_validos}")
print(f"Movimentos válidos executados: {movimentos_validos}")
print(f"Quadrante inicial: {quadrante(x_inicial, y_inicial)}")
print(f"Quadrante final: {quadrante(x, y)}")
