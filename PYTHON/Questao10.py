'''Elaborar um algoritmo que lê 3 valores a,b,c e os escreve. A seguir, encontre o maior
dos 3 valores e o escreva com a mensagem : "É o maior".'''

def maiorNumero(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        aux = n1
    elif n2 > n3:
        aux = n2
    else:
       aux = n3
    return aux

def main():
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite um número: "))
    n3 = int(input("Digite um número: "))
    print(maiorNumero(n1, n2, n3), "é o maior")
main()