'''Escrever um algoritmo que lê um valor em reais e calcula qual o menor número possível
de notas de 100, 50, 10, 5 e 1 em que o valor lido pode ser decomposto. Escrever o valor
lido e a relação de notas necessárias.'''

def cedulas(valor):
    n100 = int(valor / 100)
    r100 = int(valor % 100)
    n50 = int(r100 / 50)
    r50 = int(r100 % 50)
    n10 = int(r50 / 10)
    r10 = int(r50 % 10)
    n5 = int(r10 / 5)
    r5 = int(r10 % 5)
    n1 = int(r5 / 1)
    r1 = int(r5 % 1)
    if n100 > 0:
        print("Cédulas de R$100: ", n100)
    if n50 > 0:
        print("Cédulas de R$50: ", n50)
    if n10 > 0:
        print("Cédulas de R$10: ", n10)
    if n5 > 0:
        print("Cédulas de R$5: ", n5)
    else:
        print("Cédulas de R$1: ", n1)
    return ""

def main():
    valor = int(input("Digite um valor: "))
    print(cedulas(valor))

main()