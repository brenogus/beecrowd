from collections import defaultdict

def insercao_dos_dados(cidades: dict, num_cidade: int):
    """
    Lê os dados de entrada da quantidade de casas por cidade.
    Para cada casa, coleta o número de pessoas e o consumo de água.
    Organiza os dados por cidade em um dicionário.

    Parâmetros:
        cidades (dict): Dicionário que mapeia número da cidade para dados das casas.
        num_cidade (int): Número da cidade atual.

    Retorna:
        dict: Dicionário atualizado com dados de todas as cidades inseridas.
    """
    while True:
        quantidade_casas = int(input())  # Lê a quantidade de casas para a cidade
        if quantidade_casas == 0:  # Sinaliza o fim da entrada
            return cidades
        lista = []
        for _ in range(quantidade_casas):
            pessoas, consumo = map(int, input().split())  # Lê número de pessoas e consumo
            lista.append((pessoas, consumo))  # Armazena como tupla
        cidades[str(num_cidade)] = lista  # Armazena a lista de casas no dicionário da cidade
        num_cidade += 1  # Passa para a próxima cidade


def agregacao_de_residencia(cidades: dict):
    """
    Para cada casa de cada cidade, calcula o consumo por pessoa
    utilizando divisão inteira (//), e armazena junto com os dados originais.

    Retorna:
        dict: Dicionário com dados agregados por residência e consumo por pessoa.
    """
    for cidade, dados in cidades.items():
        nova_lista = []
        for casa in dados:
            pessoas, consumo = casa
            consumo_por_pessoa = consumo // pessoas  # Consumo médio por pessoa (inteiro)
            nova_lista.append(((pessoas, consumo), consumo_por_pessoa))
        cidades[cidade] = nova_lista  # Substitui dados antigos pelos novos
    return cidades


def ordenacao_por_consumo_individual(cidades: dict):
    """
    Ordena os dados de cada cidade em ordem crescente do consumo por pessoa.

    Retorna:
        dict: Dicionário com os dados ordenados.
    """
    for cidade, dados in cidades.items():
        cidades[cidade] = sorted(dados, key=lambda x: x[1])  # Ordena por consumo_por_pessoa
    return cidades

def elementos_repetidos_com_indices(cidades: dict):
    """
    Identifica consumos por pessoa que se repetem e armazena os índices onde ocorrem.

    Retorna:
        dict: Mapeamento de consumo_por_pessoa para lista de índices onde aparecem.
    """
    repetidos = defaultdict(list)
    index = 0  # Índice global, considerando todas as casas de todas as cidades
    for cidade in cidades.values():
        for casa in cidade:
            consumo_por_pessoa = casa[1]
            repetidos[consumo_por_pessoa].append(index)
            index += 1
    # Filtra apenas os consumos que ocorrem mais de uma vez
    return {k: v for k, v in repetidos.items() if len(v) > 1}


def impressao_dos_dados(cidades: dict, repetidos: dict):
    """
    Exibe os dados formatados de cada cidade. Para valores de consumo por pessoa repetidos,
    soma o número de pessoas que têm esse consumo e imprime apenas uma vez.

    Parâmetros:
        cidades (dict): Dicionário com os dados das cidades.
        repetidos (dict): Dicionário de consumos por pessoa que ocorrem em múltiplas residências.
    """
    for cidade, dados in cidades.items():
        print(f'CIDADE# {cidade}:')
        consumo_total = 0
        total_pessoas = 0
        ja_impressos = set()  # Garante que consumos repetidos sejam impressos uma vez só

        # Soma o número de pessoas por consumo por pessoa
        consumo_por_pessoa_dict = defaultdict(int)
        for (pessoas, consumo), consumo_pp in dados:
            consumo_por_pessoa_dict[consumo_pp] += pessoas

        for (pessoas, consumo), consumo_pp in dados:
            if consumo_pp not in ja_impressos:
                print(f'{consumo_por_pessoa_dict[consumo_pp]}-{consumo_pp}', end=' ')
                ja_impressos.add(consumo_pp)
            consumo_total += consumo
            total_pessoas += pessoas

        # Cálculo do consumo médio, truncado para 2 casas decimais
        consumo_medio = consumo_total / total_pessoas
        consumo_medio = int(consumo_medio * 100) / 100  # Trunca e não arredonda
        print(f'\nConsumo medio: {consumo_medio:.2f} m3.\n')


if __name__ == '__main__':
    def main():
        """
        Função principal do programa: executa o fluxo de leitura, processamento e exibição dos dados.
        """
        cidades = {}
        num_cidade = 1
        cidades = insercao_dos_dados(cidades, num_cidade)               # Entrada
        cidades = agregacao_de_residencia(cidades)                      # Processamento 1
        cidades = ordenacao_por_consumo_individual(cidades)             # Processamento 2
        repetidos = elementos_repetidos_com_indices(cidades)            # Processamento 3
        impressao_dos_dados(cidades, repetidos)                         # Saída final

    main()

