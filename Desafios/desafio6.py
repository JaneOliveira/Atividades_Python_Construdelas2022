# -*- coding: utf-8 -*-
"""
Created on Tue May  3 21:39:18 2022

@author: jane.oliveira_dp6
"""

import colorama
from colorama import Fore
from colorama import Style

# Você é a professora de Ciências e está lançando as notas das alunas.
# Você quer criar um sistema no qual suas alunas podem ver suas notas digitando o nome.
# As listas de alunas e notas se encontra abaixo. As notas podem variar de 0 a 100.
# Nessas listas, as notas estão na mesma ordem dos nomes, ou seja, a aluna no índice 4 tirou a nota no índice 4.

alunas = ['Adriana', 'Bárbara', 'Franciele', 'Laís', 'Maria', 'Nayara', 'Patrícia', 'Renata', 'Sarah', 'Thainá']
notas = [78, 57, 80, 98, 54, 89, 90, 100, 71, 85]

alunas = [aluna.lower() for aluna in alunas]

# Comece o programa perguntando o nome da aluna.
nome = input("Digite seu nome:").lower()

# Procure o nome digitado na lista de nomes e imprima uma mensagem com a nota que ela tirou.
# Notas abaixo de 60 devem ser impressas com a cor vermelha, e notas a partir de 90 devem ser
# impressas com a cor verde.
# Se o nome digitado não existir na lista, imprima uma mensagem de erro usando a cor vermelha.
try:
    index = alunas.index(nome)
    if(notas[index]<60):
        print(Fore.RED + f"Sua nota é: {notas[index]}"+Fore.RESET)
    elif(notas[index]>90):
        print(Fore.GREEN + f"Sua nota é: {notas[index]}"+Fore.RESET)
    else:
        print(f"Sua nota é: {notas[index]}")
except:
    print(Fore.RED + "O nome não se encontra na lista"+Fore.RESET)


