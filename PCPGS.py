#nomeando variável de alerta e condição para repetição
alertas = 0
repeticao = True 

#nomeando listas para armazenar dados
temps = []
umids = []
precipts = []

#iniciando bloco de repetição e entrada de dados
while repeticao == True:
    temp = int(input("DIgite a temp em graus Celsius: \n"))
    temps.append(temp)

    umid = int(input("DIgite a umid em %: \n"))
    umids.append(umid)

    precipt = int(input("Digite a precipatação em mm: \n"))
    precipts.append(precipt)

    if temp >= 40 or temp <= 5:
        print("alerta de temp crítica\n")
        alertas += 1

    if umid <= 20 or umid >= 80:
        print("alerta de umid crítica\n")
        alertas += 1

    if precipt >= 80:
        print("alerta de precipitação crítica\n")
        alertas += 1

    pergunta = input("Você deseja inserir mais dados? (s/n): \n").lower()
    
    if pergunta == 'n':
        repeticao = False

#definindo o número de semanas e dias       
num_semanas = 2
num_dias = 5

#criação da matriz de temperaturas
if len(temps) >= num_semanas * num_dias:
    temps_matriz = []
    idx = 0
    for _ in range(num_semanas):
        semana = []
        for _ in range(num_dias):
            semana.append(temps[idx])
            idx += 1
        temps_matriz.append(semana)

    #mostra a matriz de temperaturas
    for semana, dias in enumerate(temps_matriz, start=1):
        print(f"Semana {semana}: {dias}")

    print("\nMaior e menor temperatura de cada semana:\n")
    #mostra a maior e menor temperatura de cada semana
    for i, semana in enumerate(temps_matriz, start=1):
        maior = max(semana)
        menor = min(semana)
        print(f"Semana {i} - Maior temp: {maior}°C, Menor temp: {menor}°C\n")
else:
    print("Não há dados suficientes para formar uma matriz 2x5 de temperaturas.\n")

if alertas >= 5:
    print("Risco alto de evento climático extremo\n")
else:
    print("Clima sob controle\n")

print(f"Total de alertas: {alertas}")