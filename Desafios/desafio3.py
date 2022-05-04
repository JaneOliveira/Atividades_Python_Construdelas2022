# -*- coding: utf-8 -*-
"""
Created on Tue May  3 20:44:08 2022

@author: jane.oliveira
"""

from datetime import datetime, timedelta

# Peça para o usuário digitar a data de seu próximo aniversário no formato brasileiro

data = input("Digite a data do seu proximo aniversário no formato brasileiro: Ex. 10-11-2022\n\n")
data = datetime.strptime(data, "%d-%m-%Y")
hoje = datetime.today()

tempo = data - hoje

# Imprima uma mensagem dizendo quantos dias faltam para o aniversário dele

print(f"\nFaltam apenas {tempo} para o seu aniversario.\n\n")

# Pergunte ao usuário se ele(a) gosta de aniversário e salve a resposta

gosta = input("\n\nVocê gosta de aniversario?? obs.responda sim ou nao\n").lower()

# Pergunte ao usuário se ele(a) vai fazer festa e salve a resposta

festa = input("\n\nVocê vai fazer festa?? obs.responda sim ou nao\n").lower()

# Imprima uma mensagem dizendo se o usuário vai ganhar presente ou não
# A regra é: o usuário só pode ganhar presente se gostar de aniversário e for fazer festa.
if gosta == "sim" and festa == "sim":
    print("Parabens, voce vai ganhar presente!!")
else:
    print("Que pena, voce nao vai ganhar presente!!")