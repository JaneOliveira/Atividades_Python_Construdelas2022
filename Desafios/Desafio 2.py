# -*- coding: utf-8 -*-
"""
Created on Tue May  3 15:43:24 2022

@author: jane.oliveira
"""

"""Desafio 2"""


# 1. Pergunte ao usuário em qual cidade e o estado em que ele(a) mora

cidade, estado  = input("Digite a cidade e o estado em que voce mora (obs. Separados por virgula)\n").split(",")

# 2. Imprima uma mensagem diga a cidade em que o usuário mora. 
#    O nome da cidade deve estar todo em letras maiúsculas.
cidade = cidade.upper()
print(f"Voce mora na cidade: {cidade}")

# 3. Imprima uma mensagem diga o estado em que o usuário mora. 
#    O nome do estado deve estar todo em letras maiúsculas.
#    Utilize uma forma de formatação de string diferente da que foi usada no item 2.

i=0
teste=[]
for i in range(len(estado)):
    if ord(estado[i]) >96 and ord(estado[i]) < 123:
            teste.append(estado[i].swapcase())
estado ="".join(teste)
    
        
print(f"Voce mora no estado: {estado}")