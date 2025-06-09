# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

dados = list(map(int,input().split()))
a = dados[0]
b = dados[1]
c = dados[2] 

maior = lambda x,y: (x + y + abs(x-y)) / 2
maior_ab = maior(a,b)

print(f'{int(maior(maior_ab,c))} eh o maior')