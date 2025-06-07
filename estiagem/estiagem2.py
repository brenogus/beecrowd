from collections import defaultdict

def insercao_dos_dados():
    """
    Lê os dados de entrada do usuário sobre o consumo de água por residência em diferentes cidades.

    Estrutura esperada da entrada:
    - Um número inteiro representando a quantidade de casas de uma cidade.
    - Para cada casa: dois inteiros representando a quantidade de pessoas e o consumo total em m³.
    - Entrada é finalizada com '0'.

    Retorna:
        cidades (dict): Um dicionário onde a chave é o número da cidade (como string)
                        e o valor é uma lista de tuplas (pessoas, consumo).
    """
    cidades = {}
    num_cidade = 1
    while True:
        quantidade_casas = int(input())
        if quantidade_casas == 0:
            break
        # Lê todas as casas da cidade atual
        cidades[str(num_cidade)] = [tuple(map(int, input().split())) for _ in range(quantidade_casas)]
        num_cidade += 1
    return cidades


def agregacao_e_ordenacao(cidades):
    """
    Para cada cidade, calcula o consumo por pessoa de cada residência
    e ordena os dados pelo consumo individual.

    Atualiza cada cidade no dicionário para conter uma lista de tuplas:
        [((pessoas, consumo), consumo_por_pessoa), ...]

    Args:
        cidades (dict): Dicionário com dados originais (pessoas, consumo).

    Retorna:
        dict: O mesmo dicionário com os dados agregados e ordenados.
    """
    for cidade, dados in cidades.items():
        # Calcula consumo por pessoa e ordena
        cidades[cidade] = sorted(
            [((p, c), c // p) for p, c in dados],  # Armazena cada casa com consumo por pessoa
            key=lambda x: x[1]                     # Ordena pelo consumo por pessoa
        )
    return cidades


def impressao_dos_dados(cidades):
    """
    Imprime os dados de cada cidade, agrupando casas com mesmo consumo por pessoa
    e exibindo o consumo médio da cidade.

    Args:
        cidades (dict): Dicionário com os dados transformados
                        ((pessoas, consumo), consumo_por_pessoa).
    """
    for cidade, dados in cidades.items():
        print(f'CIDADE# {cidade}:')
        consumo_total = 0
        total_pessoas = 0
        agrupados = defaultdict(int)

        # Agrupa a quantidade de pessoas por consumo por pessoa
        for (pessoas, consumo), consumo_pp in dados:
            agrupados[consumo_pp] += pessoas
            consumo_total += consumo
            total_pessoas += pessoas

        # Imprime os pares "total_pessoas-consumo_por_pessoa" ordenados
        for consumo_pp in sorted(agrupados):
            print(f'{agrupados[consumo_pp]}-{consumo_pp}', end=' ')

        # Cálculo e impressão do consumo médio com duas casas decimais
        consumo_medio = consumo_total / total_pessoas
        print(f'\nConsumo medio: {int(consumo_medio * 100) / 100:.2f} m3.\n')


def main():
    """
    Função principal que orquestra a execução:
    - Lê os dados de entrada
    - Realiza agregação e ordenação
    - Imprime os dados finais formatados
    """
    cidades = insercao_dos_dados()
    cidades = agregacao_e_ordenacao(cidades)
    impressao_dos_dados(cidades)


if __name__ == '__main__':
    main()
