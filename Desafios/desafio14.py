# -*- coding: utf-8 -*-
"""
Created on Fri May 13 18:57:49 2022

@author: jane.oliveira
"""


import sys
import requests
import json

# Crie uma aplicação que lê na linha de comando o nome de um feitiço


# Utilize a biblioteca requests para ler o JSON disponível em
# https://construdelas.blob.core.windows.net/intro-ao-python/feiticos.json


# Converta o CSV para um dicionário cujas chaves são as palavras do cabeçalho do CSV.


# Imprima para o usuário os dados sobre o feitiço que ele solicitou.
# Se o feitiço não foi encontrado, lance uma exceção.

# requisicao = requests.get('https://construdelas.blob.core.windows.net/intro-ao-python/feiticos.json')
# print(requisição.json())


try:
    page1 = requests.get('https://construdelas.blob.core.windows.net/intro-ao-python/feiticos.json', verify=False)

except requests.exceptions.ConnectionError:
    requests.status_code = "Connection refused"
