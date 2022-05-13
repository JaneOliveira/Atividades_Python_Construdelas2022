# -*- coding: utf-8 -*-
"""
Created on Fri May 13 19:40:58 2022

@author: jane.oliveira_dp6
"""

# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.



# Crie uma instância da classe carro.


# Faça o carro "andar" utilizando os métodos da sua classe.


# Faça o carro "parar" utilizando os métodos da sua classe.

class automovel:
    def __init__(self, modelo, cor, ligado, velocidade):
        self.modelo = modelo
        self.cor = cor
        self.ligado = ligado
        self.velocidade = velocidade
        
    def liga(self):
        if(self.ligado != "ligado"):
            self.ligado = "ligado"
        print("Carro ligado")
    
    def desliga(self):
        if(self.ligado != "desligado"):
            self.ligado = "desligado"
            
        print("Carro desligado")
    
    def acelera(self):
        if(self.ligado == "ligado"):
            self.velocidade +=10
        else:
            self.ligado == "ligado"
            self.velocidade +=10
            
        print(f"Carro acelerando e andando a velocidade:{self.velocidade}")
    
    def desacelera(self):
        if(self.ligado == "ligado" and self.velocidade >10):
            self.velocidade -=10
            print(f"Carro desacelerando e andando a velocidade:{self.velocidade}")
        else:
            self.velocidade = 0
            print("Carro Parou")
            self.desliga()

def main():
    carro = automovel("corsa", "rosa", "desligado",0)
    
    carro.liga()
    carro.acelera()
    carro.acelera()
    carro.acelera()
    carro.desacelera()
    carro.desacelera()
    carro.desacelera()
    carro.desacelera()
    
    


if __name__ == '__main__':
    main()