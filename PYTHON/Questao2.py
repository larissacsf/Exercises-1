'''Escreva um algoritmo que leia três números inteiros e positivos (A, B, C) e calcule a
seguinte expressão: D = R + S / 2 onde R = (A+B)² e S = (B+C)²'''


import math
def calcNumeros(a, b, c):
    r = math.pow((a + b), 2)
    s = math.pow((b + c), 2)
    d = (r + s) / 2
    return d

def main():
    a = int(input("Primeiro número: "))
    b = int(input("Segundo número: "))
    c = int(input("Terceiro número: "))
    print("Resultado: ", calcNumeros(a,b,c))

main()