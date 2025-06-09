import sys

def truncate_2_decimals(x):
    # Trunca para 2 casas decimais sem arredondar
    return int(x * 100) / 100

def main():
    entrada = sys.stdin.read().strip().split()
    idx = 0
    cidade_num = 1

    while True:
        if idx >= len(entrada):
            break
        n = int(entrada[idx])
        idx += 1
        if n == 0:
            break

        consumo_por_pessoa = {}
        total_pessoas = 0
        total_consumo = 0

        for _ in range(n):
            pessoas = int(entrada[idx])
            consumo = int(entrada[idx+1])
            idx += 2

            cpp = consumo // pessoas
            consumo_por_pessoa[cpp] = consumo_por_pessoa.get(cpp, 0) + pessoas
            total_pessoas += pessoas
            total_consumo += consumo

        print(f"CIDADE# {cidade_num}:")
        # imprimir pares no formato pedido, sem espaço no final
        pares = [f"{consumo_por_pessoa[cpp]}-{cpp}" for cpp in sorted(consumo_por_pessoa)]
        print(" ".join(pares))
        consumo_medio = truncate_2_decimals(total_consumo / total_pessoas)
        print(f"Consumo medio: {consumo_medio:.2f} m3.\n")

        cidade_num += 1

if __name__ == "__main__":
    main()
