# -*- coding: utf-8 -*-
"""
Created on Fri May 13 18:57:49 2022

@author: jane.oliveira
"""

import requests
import json

# Crie uma aplicação que lê na linha de comando o nome de um feitiço
# Utilize a biblioteca requests para ler o JSON disponível em
# https://construdelas.blob.core.windows.net/intro-ao-python/feiticos.json
# Converta o CSV para um dicionário cujas chaves são as palavras do cabeçalho do CSV.
# Imprima para o usuário os dados sobre o feitiço que ele solicitou.
# Se o feitiço não foi encontrado, lance uma exceção.

def create_dic():
    try:
        speels = requests.get('https://construdelas.blob.core.windows.net/intro-ao-python/feiticos.json')
        speels_json = speels.text
        speels_dic = json.loads(speels_json.lower())
        return speels_dic
    except:
        print("Sorry, a base de dados de feitiço encontra-se indiponivél no momento, tente mais tarde!")
    

def search_spell():
    input_speel = input("Digite um feitiço que queira saber as informações: ").lower()
    teste = list()
    speels_dic = create_dic()
    for key, value in speels_dic.items():
        teste.append(value)

    aux = -1
    for i in range(len(teste)):
        if teste[i]["encantamento"] == input_speel:
            aux = i
            
    if(aux != -1):
        print("\n\n\t INFORMAÇÕES \n")
        print(f"{teste[aux]}")
    else:
        print("\nSorry, feitiço não encontrado!!\n\n")


search_spell()
    
