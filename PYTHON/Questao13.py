'''Escreva um algoritmo que leia 3 números inteiros e mostre o maior deles.'''

def maiorNumero(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        maior = n1
    elif n2 >= n3:
        maior = n2
    else:
        maior = n3
    return maior

def main():
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite um número: "))
    n3 = int(input("Digite um número: "))
    print("Maior: ", maiorNumero(n1, n2, n3))
main()