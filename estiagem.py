

cidades = {}
num_cidade = 1

# Laço para definição de quantas casas e quantos litros foram gastos por casa na cidade
while True:
    quantidade_casas = int(input())
    if quantidade_casas == 0:
        break
    lista = []
    for i in range(quantidade_casas):
        frase = input()
        tokens = frase.split()
        var = (int(tokens[0]), int(tokens[1]))
        lista.append(var)
    cidades[f'{num_cidade}'] = lista
    num_cidade += 1


consumo_pessoas = []

# Laço que cria uma lista zipada entre os valores de cada residencia com o consumo por pessoa de cada residencia
for cidade, dados in cidades.items():
    for casa in dados:
        consumo_pessoas.append(int(casa[1] / casa[0]))
    cidades[f'{cidade}'] = list(zip(dados,consumo_pessoas))
    consumo_pessoas = []
    

# Laço que ordena as casas das cidades por ordem crescente de consumo por pessoa
for cidade, dados in cidades.items():
    l = sorted(dados, key= lambda x: x[1])
    cidades[f'{cidade}'] = l
    

# Laço que imprime e calcula o consumo médio da cidade
for cidade,dados in cidades.items():
    print(f'CIDADE# {cidade}:')
    consumo_total = 0
    total_pessoas = 0
    for dado in dados:
        print(f'{dado[0][0]}-{dado[1]} ',end= '')
        consumo_total += dado[0][1]
        total_pessoas += dado[0][0] 
    consumo_medio = consumo_total / total_pessoas
    consumo_medio = int(consumo_medio  * 100) / 100
    print(f'\nConsumo medio: {consumo_medio:.2f} m3.')
    print()
