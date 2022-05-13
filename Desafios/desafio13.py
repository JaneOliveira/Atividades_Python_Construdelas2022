# -*- coding: utf-8 -*-
"""
Created on Thu May 12 19:54:27 2022

@author: jane.oliveira"""

import time

# Crie um decorator que calcule o tempo de execução de uma determinada função

# Aplique seu decorator na função abaixo e veja quanto tempo a busca de um mesmo 
#valor em um set e uma lista demoram para serem executadas

def calcula_duracao(funcao):
    def timer():
        
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()
        print(f"[{funcao.__name__}] Tempo total de execução: {str(tempo_final - tempo_inicial)}")
    
    return timer

def encontrar_item(container, item):
    return item in container

@calcula_duracao
def main():
    tamanho = 1000000
    set_grande = set(range(tamanho))
    lista_grande = list(range(tamanho))
    item = 500399
    encontrar_item(set_grande, item)
    encontrar_item(lista_grande, item)

if __name__ == '__main__':
    main()
    