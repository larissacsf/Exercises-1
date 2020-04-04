'''Elaborar um algoritmo que lê 3 valores a,b,c e verifica se eles formam ou não um
triângulo. Supor que os valores lidos são inteiros e positivos. Caso os valores formem um
triângulo, calcular e escrever a área deste triângulo. Se não formam triângulo escrever os
valores lidos. ( se a &gt; b + c não formam triângulo algum, se a é o maior).'''

import math
def calcAreaTriagulo(a, b, c):
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area

def main():
    a = int(input("Valor de A: "))
    b = int(input("Valor de B: "))
    c = int(input("Valor de C: "))
    if a > b + c:
        print(a,b,c,"não formam um triângulo")
    else:
        print(calcAreaTriagulo(a,b,c))

main()