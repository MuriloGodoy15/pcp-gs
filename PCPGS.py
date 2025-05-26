while True:
    temp = int(input("DIgite a temp em graus Celsius: "))
    temps = []
    temps.append(temp)

    umid = int(input("DIgite a umid em %: "))
    umids = []
    umids.append(umid)

    precipt = int(input("Digite a precipatação em mm: "))
    precipts = []
    precipts.append(precipt)

    if temp >= 40 or temp <= 5:
        print("alerta de temp crítica")
        alertas += 1

    if umid <= 20 or umid >= 80:
        print("alerta de umid crítica")
        alertas += 1

    if precipt >= 80:
        print("alerta de precipitação crítica")
        alertas += 1

import random

# Cria uma matriz 2x5 com valores simulados de temp (2 semanas, 5 dias)
temps = [[random.randint(10, 40) for _ in range(5)] for _ in range(2)]

# Mostra a matriz de temps
for semana, dias in enumerate(temps, start=1):
    print(f"Semana {semana}: {dias}")

# Mostra a maior e menor temp por semana
for i, semana in enumerate(temps, start=1):
    maior = max(semana)
    menor = min(semana)
    print(f"Semana {i} - Maior temp: {maior}°C, Menor temp: {menor}°C")