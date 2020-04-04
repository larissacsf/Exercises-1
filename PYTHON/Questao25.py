'''Escrever um algoritmo que lê um conjunto de 4 valores i, a, b, c, onde i é um valor
inteiro e positivo e a, b, c, são quaisquer valores reais e os escreva. A seguir:
a) Se i=1 escrever os três valores a, b, c em ordem crescente.
b) Se i=2 escrever os três valores a, b, c em ordem decrescente.
c) Se i=3 escrever os três valores a, b, c de forma que o maior entre a, b, c fique dentre os
dois.'''

valores = []

def crescente(op):
    if op == 1:
        for i in range(0, 3):
            valores.append(int(input("Digite um valor: ")))
            valores.sort(key=int)
    return valores

def decrescente(op):
    if op == 2:
        for i in range(0, 3):
            valores.append(int(input("Digite um valor: ")))
            valores.sort(key=int, reverse=True)
    return valores

def maior(op):
    if op == 3:
        for i in range(0, 3):
            valores.append(int(input("Digite um valor: ")))
        aux = valores[1]
        valores[1] = max(valores)
        valores[2] = aux
    return valores

def main():
    op = int(input("1 - para ordem crescente | 2 - para ordem decrescente | 3 - maior número:  "))
    if op == '1':
        print(crescente(op))
    elif op == '2':
        print(decrescente(op))
    else:
        print(maior(op))

main()







