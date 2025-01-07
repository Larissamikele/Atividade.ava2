PALAVRA_CHAVE = "charles"
tentativas = 6
letras_erradas = []
letras_corretas = []
acertos = ["_"] * len(PALAVRA_CHAVE)

print("Bem-vindo ao jogo da forca!")
print("A palavra tem", len(PALAVRA_CHAVE), "letras.")

while tentativas > 0:
    print("\nPalavra:", " ".join(acertos))
    print("Letras erradas:", ", ".join(letras_erradas))
    print("Tentativas restantes:", tentativas)
    
    letra = input("Digite uma letra: ").lower()
    
    if letra in letras_erradas or letra in letras_corretas:
        print("Você já tentou essa letra.")
        continue
    
    if letra in PALAVRA_CHAVE:
        letras_corretas.append(letra)
        for i in range(len(PALAVRA_CHAVE)):
            if PALAVRA_CHAVE[i] == letra:
                acertos[i] = letra
        print("Uau! Você acertou a letra.")
    else:
        letras_erradas.append(letra)
        tentativas -= 1
        print("Ops! Você errou.")
    
    if "_" not in acertos:
        print("\nParabéns! Você descobriu a palavra:", PALAVRA_CHAVE)
        break
else:
    print("\nVocê foi enforcado! A palavra era:", PALAVRA_CHAVE)
