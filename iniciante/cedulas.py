# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

notas = [100,50,20,10,5,2,1]
valor = int(input())
var = valor
quantidades = []
if valor > 0 and valor < 1000000:
    for nota in notas:
        quantidade = int(valor / nota)
        valor = valor % nota
        quantidades.append(quantidade)
    respostas = zip(quantidades,notas)
    print(var)
    for resposta in respostas:
        print(f'{resposta[0]} nota(s) de R$ {resposta[1]},00')