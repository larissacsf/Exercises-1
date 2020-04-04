'''O custo ao consumidor de um carro novo é a soma do custo de fábrica com a
percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a
percentagem do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo que
leia o custo de fábrica de um carro e escreva o custo ao consumidor.'''

def calcCusto(custoFabrica):
    porcentagemDistribuidor = (custoFabrica * 28) / 100
    porcentagemImpostos = (custoFabrica * 45) / 100
    return custoFabrica + porcentagemDistribuidor + porcentagemImpostos

def main():
    custoFabrica = float(input("Qual o custo de fábrica: R$ "))
    print("Custo final ao consumidor: R$ ",calcCusto(custoFabrica) )

main()