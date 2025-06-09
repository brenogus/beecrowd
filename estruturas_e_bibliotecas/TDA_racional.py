# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

from fractions import Fraction

tamanho_testes = int(input())
expressoes = []

for i in range(tamanho_testes):
    frase = input()
    tokens = frase.split()  # Ex: ['1', '/', '2', '+', '3', '/', '4']
    n1 = int(tokens[0])
    d1 = int(tokens[2])
    operador = tokens[3]
    n2 = int(tokens[4])
    d2 = int(tokens[6])
    expressoes.append((n1, d1, operador, n2, d2))

for n1, d1, operador, n2, d2 in expressoes:
    match operador:
        case '+':
            numerador = n1 * d2 + n2 * d1
            denominador = d1 * d2
        case '-':
            numerador = n1 * d2 - n2 * d1
            denominador = d1 * d2
        case '*':
            numerador = n1 * n2
            denominador = d1 * d2
        case '/':
            numerador = n1 * d2
            denominador = n2 * d1

    # Corrigir sinal (o denominador deve ser sempre positivo)
    if denominador < 0:
        numerador *= -1
        denominador *= -1

    if numerador % denominador == 0:
        # Fração simplificada
        fracao_simplificada = Fraction(numerador, denominador)

        # Imprimir conforme o exemplo
        print(f"{numerador}/{denominador} = {fracao_simplificada}/1")
    else:
        # Fração simplificada
        fracao_simplificada = Fraction(numerador, denominador)

        # Imprimir conforme o exemplo
        print(f"{numerador}/{denominador} = {fracao_simplificada}")