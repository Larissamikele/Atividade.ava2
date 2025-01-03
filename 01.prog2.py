
massa_inicial = float(input("Digite a massa inicial do material (em gramas): "))


tempo_meia_vida = 50
massa_final = massa_inicial
tempo_total_segundos = 0


while massa_final >= 0.5:
    massa_final /= 2  
    tempo_total_segundos += tempo_meia_vida

horas = tempo_total_segundos // 3600
minutos = (tempo_total_segundos % 3600) // 60
segundos = tempo_total_segundos % 60


print("\nResultados:")
print(f"Massa inicial: {massa_inicial:.2f} g")
print(f"Massa final: {massa_final:.2f} g")
print(f"Tempo total para o decaimento: {int(horas)} horas, {int(minutos)} minutos e {int(segundos)} segundos.")


