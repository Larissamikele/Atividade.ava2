mensagem = input("Digite a mensagem: ")
chave = input("Digite a chave: ")

alfabeto = "abcdefghijklmnopqrstuvwxyz"

chave_expandida = ""
indice_chave = 0
while len(chave_expandida) < len(mensagem):
    for letra in mensagem:
        if letra.lower() in alfabeto:
            chave_expandida += chave[indice_chave % len(chave)]
            indice_chave += 1
        else:
            chave_expandida += letra

mensagem_criptografada = ""
i = 0
while i < len(mensagem):
    letra = mensagem[i]
    if letra.lower() in alfabeto:
        base = alfabeto.upper() if letra.isupper() else alfabeto

        posicao_letra = 0
        j = 0
        while j < len(base):
            if base[j] == letra:
                posicao_letra = j
                break
            j += 1

        posicao_chave = 0
        k = 0
        while k < len(alfabeto):
            if alfabeto[k] == chave_expandida[i].lower():
                posicao_chave = k
                break
            k += 1

        nova_posicao = (posicao_letra + posicao_chave) % 26
        mensagem_criptografada += base[nova_posicao]
    else:
        mensagem_criptografada += letra
    i += 1

mensagem_descriptografada = ""
i = 0
while i < len(mensagem_criptografada):
    letra = mensagem_criptografada[i]
    if letra.lower() in alfabeto:
        base = alfabeto.upper() if letra.isupper() else alfabeto

        posicao_letra = 0
        j = 0
        while j < len(base):
            if base[j] == letra:
                posicao_letra = j
                break
            j += 1

        posicao_chave = 0
        k = 0
        while k < len(alfabeto):
            if alfabeto[k] == chave_expandida[i].lower():
                posicao_chave = k
                break
            k += 1

        nova_posicao = (posicao_letra - posicao_chave) % 26
        mensagem_descriptografada += base[nova_posicao]
    else:
        mensagem_descriptografada += letra
    i += 1

print("Mensagem criptografada:", mensagem_criptografada)
print("Mensagem descriptografada:", mensagem_descriptografada)
