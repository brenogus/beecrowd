# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

import bisect

casos_entrada = []
caso = 1

while True:
    numero_de_marmores, quantidade_chutes = map(int, input().split())

    if numero_de_marmores == 0 and quantidade_chutes == 0:
        break

    marmores = []
    for _ in range(numero_de_marmores):
        marmores.append(int(input()))

    chutes = []
    for _ in range(quantidade_chutes):
        chutes.append(int(input()))

    casos_entrada.append((caso, marmores, chutes))
    caso += 1

for numero_caso, marmores, chutes in casos_entrada:
    marmores.sort()
    print(f'CASE# {numero_caso}:')

    for chute in chutes:
        index = bisect.bisect_left(marmores, chute)
        if index < len(marmores) and marmores[index] == chute:
            print(f'{chute} found at {index + 1}')  # +1 porque a contagem começa em 1
        else:
            print(f'{chute} not found')
