# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

segundos = int(input())
horas = int((segundos / 3600))
minutos = int((segundos % 3600) / 60) 
segundos = int((segundos % 3600) % 60)

print(f'{horas}:{minutos}:{segundos}')
