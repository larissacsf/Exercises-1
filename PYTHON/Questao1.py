'''Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer no
plano, P(x1,y1) e P(x2,y2), escreva a distância entre eles.'''


import math
def distanciaDoisPontos(x1, x2, y1, y2):
    d1 = math.pow((x2 - x1), 2)
    d2 = math.pow((y2-y1), 2)
    d3 = d1 + d2
    r = math.sqrt(d3)
    return r

def main():
    x1 = int(input("X1: "))
    x2 = int(input("X2: "))
    y1 = int(input("Y1: "))
    y2 = int(input("Y2: "))

    print(distanciaDoisPontos(x1,x2,y1,y2))

main()