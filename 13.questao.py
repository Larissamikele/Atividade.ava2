x_inicial = int(input("Digite a posição inicial X: "))
y_inicial = int(input("Digite a posição inicial Y: "))
movimentos = input("Digite os movimentos do robô: ").lower()

x = x_inicial
y = y_inicial
movimentos_validos = []
contador_movimentos = 0

for movimento in movimentos:
    if movimento == 'u':
        y += 1
        movimentos_validos.append('C')
        contador_movimentos += 1
    elif movimento == 'd':
        y -= 1
        movimentos_validos.append('B')
        contador_movimentos += 1
    elif movimento == 'r':
        x += 1
        movimentos_validos.append('D')
        contador_movimentos += 1
    elif movimento == 'l':
        x -= 1
        movimentos_validos.append('E')
        contador_movimentos += 1
    elif movimento == 'o':
        x -= 1
        y += 1
        movimentos_validos.append('NO')
        contador_movimentos += 1
    elif movimento == 'n':
        x += 1
        y += 1
        movimentos_validos.append('NE')
        contador_movimentos += 1
    elif movimento == 'e':
        x += 1
        y -= 1
        movimentos_validos.append('SE')
        contador_movimentos += 1
    elif movimento == 'w':
        x -= 1