#nomeando variável de alerta e condição para repetição
alertas = 0
repeticao = True 

#nomeando listas para armazenar dados
temperaturas = []
umidades = []
precipitacoes = []

#criando função para analisar os dados
def analisar_dados(temperatura, umidade, precipitacao):

    global alertas

    if temperatura >= 40 or temperatura <= 5:
        print("Alerta de temperatura crítica\n")
        alertas += 1

    if umidade <= 20 or umidade >= 95:
        print("Alerta de umidade crítica\n")
        alertas += 1

    if precipitacao >= 80:
        print("Alerta de precipitação crítica\n")
        alertas += 1
    return 0 

#iniciando bloco de repetição e entrada de dados
while repeticao == True:
    temperatura = int(input("Digite a temperatura em graus Celsius: "))
    
    #verificando se temperatura é um número inteiro
    if temperatura != int(temperatura):
        print("Por favor, insira um número inteiro válido para a temperatura.")
        continue

    temperaturas.append(temperatura)

    #verificando se a umidade está dentro do intervalo permitido
    umidade = int(input("\nDigite a umidade em %: "))
   
    if umidade != int(umidade):
        print("Por favor, insira um número inteiro válido para a umidade.")
        continue
    
    umidades.append(umidade)

    precipitacao = int(input("\nDigite a precipitação em mm: "))

    #verificando se a precipitação está dentro do intervalo permitido
    if precipitacao != int(precipitacao):
        print("Por favor, insira um número inteiro válido para a precipitação.")
        continue

    precipitacoes.append(precipitacao)

    #chamando a função para analisar os dados
    analisar_dados(temperatura, umidade, precipitacao)

    pergunta = input("Você deseja inserir mais dados? (s/n): ").lower()
    
    if pergunta == 'n':
        repeticao = False

#definindo o número de semanas e dias       
num_semanas = 2
num_dias = 5

#criação da matriz de temperaturas
if len(temperaturas) >= num_semanas * num_dias:
    temperaturas_matriz = []
    idx = 0
    for _ in range(num_semanas):
        semana = []
        for _ in range(num_dias):
            semana.append(temperaturas[idx])
            idx += 1
        temperaturas_matriz.append(semana)

    #mostra a matriz de temperaturas
    for semana, dias in enumerate(temperaturas_matriz, start=1):
        print(f"Semana {semana}: {dias}")

    print("\nMaior e menor temperatura de cada semana:")
    #mostra a maior e menor temperatura semanal 
    for i, semana in enumerate(temperaturas_matriz, start=1):
        maior = max(semana)
        menor = min(semana)
        print(f"\nSemana {i} - Maior temperatura: {maior}°C, Menor temperatura: {menor}°C")
else:
    print("\nNão há dados suficientes para formar uma matriz 2x5 de temperaturas.")

if alertas >= 5:
    print("\nRisco alto de evento climático extremo\n")
else:
    print("\nClima sob controle")

print(f"Total de alertas: {alertas}")