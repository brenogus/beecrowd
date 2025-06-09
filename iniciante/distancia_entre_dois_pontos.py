# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

p1 = list(map(float,input().split()))
p2 = list(map(float,input().split()))
x1 = p1[0]
y1 = p1[1]
x2 = p2[0]
y2 = p2[1]

distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(f'{distancia:.4f}')