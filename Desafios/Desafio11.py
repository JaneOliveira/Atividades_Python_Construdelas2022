# -*- coding: utf-8 -*-
"""
Created on Thu May 12 19:06:29 2022

@author: jane.oliveira
"""

"""Desafio 11"""

# Dado um arquivo de entrada, escreva um programa que leia o conteudo do arquivo para uma string,
# e escreva um outro arquivo de saída que imprima o texto ao contrário.
# Exemplo de entrada: Oi mulheres maravilhosas do curso de Python do ConstruDelas!
# Exemplo de saída: !saleDurtsnoC od nohtyP ed\nosruc od sasohlivaram serehlum iO

arquivo = open('entrada_desafio_11.txt','r')
arq2 = open('saida_desafio_11.txt','w+')

texto = str()

for line in arquivo:
    texto +=line

texto = texto[::-1]

arq2.writelines(texto)

arquivo.close()
arq2.close()