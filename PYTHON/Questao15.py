'''Faça um algoritmo que leia um nº inteiro e mostre uma mensagem indicando se este
número é par ou ímpar, e se é positivo ou negativo.'''

def numeroParouIMpar(n):
    if n % 2 == 0:
        print(n,"é par")
    else:
        print(n,"é ímpar")
    return ""

def numeroPositivoouNegativo(n):
    if n >= 0:
        print(n, "positivo")
    else:
        print(n, "é negativo")
    return ""

def main():
    n = int(input("Digite um número: "))
    print(numeroParouIMpar(n), numeroPositivoouNegativo(n))

main()