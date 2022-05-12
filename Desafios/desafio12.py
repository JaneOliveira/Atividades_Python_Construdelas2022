# -*- coding: utf-8 -*-
"""
Created on Thu May 12 19:31:45 2022

@author: jane.oliveira
"""

"""Desafio 12"""
# Escreva um programa que leia o arquivo "exemplo2.csv", e converta
# os registros desse CSV para o formato JSON. Escreva um arquivo de saída
# que contenha o conteúdo em JSON.

import pandas as pd
csv_data = pd.read_csv("exemplo2.csv", sep = ",")
csv_data.to_json("exemplo2.json",orient = "records")