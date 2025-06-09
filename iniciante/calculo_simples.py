# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

peca_1 = input().split()
peca_2 = input().split()

peca_1 = list(map(float,peca_1))
peca_2 = list(map(float,peca_2))

valor = peca_1[1] * peca_1[2] + peca_2[1] * peca_2[2]

print(f'VALOR A PAGAR: R$ {valor:.2f}') 
