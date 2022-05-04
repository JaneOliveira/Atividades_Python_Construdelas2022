# -*- coding: utf-8 -*-
"""
Created on Wed May  4 19:46:43 2022

@author: jane.oliveira
"""

'''Desafio 7'''
## O programa abaixo deve calcular a média dos valores digitados pelo usuário.
## No entanto, ele não está funcionando bem. Você pode consertá-lo?

def calcular_media(valores):
    soma = 0.0
    for i, valor in enumerate(valores):
        soma += valor
        i += 1
    return soma / i

continuar = True
valores = []

while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')
    if valor.lower() == 'ok':
        break
    valores.append(int(valor))

media = calcular_media(valores)
print('A média calculada para os valores {} foi de {}'.format(valores, media))
