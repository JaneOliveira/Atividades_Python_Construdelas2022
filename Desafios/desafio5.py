# -*- coding: utf-8 -*-
"""
Created on Tue May  3 21:28:11 2022

@author: jane.oliveira
"""

# Crie uma lista com 60 números começando com o valor 1 e indo até o número 60 
#(ou seja, o número 60 deve estar na lista).

lista = list(range(1,61))

# Imprima todos os itens da sua lista de índice par. Imprima o índice e o item.
ind = 0
for i in lista:
    if ind%2 == 0:
        print(f"indice: {ind}, item: {i}")
    ind+=1