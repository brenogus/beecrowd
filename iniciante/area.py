# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

PI = 3.14159

dados = list(map(float, input().split()))
a = dados[0]
b = dados[1]
c = dados[2]

elementos = {'TRIANGULO' : (a * c) / 2,
              'CIRCULO' : PI * (c ** 2),
              'TRAPEZIO' : ((a + b) * c) / 2,
              'QUADRADO' : b ** 2,
              'RETANGULO' : a * b
            }

for key,value in elementos.items():
    print(f'{key}: {round(value,3):.3f}')