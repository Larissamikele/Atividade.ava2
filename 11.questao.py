frase = input("Digite a frase a ser criptografada: ")
n = int(input("Digite a chave de criptografia (n): "))

frase_criptografada = ""
for char in frase:
    if 'a' <= char <= 'z':
        nova_letra = chr(((ord(char) - ord('a') + n) % 26) + ord('a'))
        frase_criptografada += nova_letra
    elif 'A' <= char <= 'Z':
        nova_letra = chr(((ord(char) - ord('A') + n) % 26) + ord('A'))
        frase_criptografada += nova_letra
    else:
        frase_criptografada += char

print("Frase criptografada:", frase_criptografada)

frase_descriptografada = ""
for char in frase_criptografada:
    if 'a' <= char <= 'z':
        nova_letra = chr(((ord(char) - ord('a') - n) % 26) + ord('a'))
        frase_descriptografada += nova_letra
    elif 'A' <= char <= 'Z':
        nova_letra = chr(((ord(char) - ord('A') - n) % 26) + ord('A'))
        frase_descriptografada += nova_letra
    else:
        frase_descriptografada += char

print("Frase descriptografada:", frase_descriptografada)