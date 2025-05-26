#nomeando variável de alerta e condição para repetição
alertas = 0
repeticao = True 

#nomeando listas para armazenar dados
temps = []
umids = []
precipts = []

#criando função para analisar os dados
def analisar_dados(temp, umid, precipt):

    global alertas
    
    if temp >= 40 or temp <= 5:
        print("alerta de temp crítica\n")
        alertas += 1

    if umid <= 20 or umid >= 95:
        print("alerta de umid crítica\n")
        alertas += 1

    if precipt >= 80:
        print("alerta de precipitação crítica\n")
        alertas += 1
    return 0 

#iniciando bloco de repetição e entrada de dados
while repeticao == True:
    temp = int(input("DIgite a temp em graus Celsius: "))
    
    if temp != int(temp):
        print("Por favor, insira um número inteiro válido para a temperatura.")
        continue

    temps.append(temp)

    umid = int(input("\nDIgite a umid em %: "))
   
    if umid != int(umid):
        print("Por favor, insira um número inteiro válido para a umidade.")
        continue
    
    umids.append(umid)

    precipt = int(input("\nDigite a precipatação em mm: "))

    if precipt != int(precipt):
        print("Por favor, insira um número inteiro válido para a precipitação.")
        continue

    precipts.append(precipt)

    #chamando a função para analisar os dados
    analisar_dados(temp, umid, precipt)

    pergunta = input("Você deseja inserir mais dados? (s/n): ").lower()
    
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

    print("\nMaior e menor temperatura de cada semana:")
    #mostra a maior e menor temperatura de cada semana
    for i, semana in enumerate(temps_matriz, start=1):
        maior = max(semana)
        menor = min(semana)
        print(f"\nSemana {i} - Maior temp: {maior}°C, Menor temp: {menor}°C")
else:
    print("\nNão há dados suficientes para formar uma matriz 2x5 de temperaturas.")

if alertas >= 5:
    print("\nRisco alto de evento climático extremo\n")
else:
    print("\nClima sob controle")

print(f"Total de alertas: {alertas}")