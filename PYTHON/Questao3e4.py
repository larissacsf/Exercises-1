'''Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e
mostre-a expressa apenas em dias. Faça um algoritmo que leia a idade de uma pessoa expressa em dias e mostre-a
expressa em anos, meses e dias'''

def idadeMeses(idade):
    quantMeses = idade * 12
    return quantMeses

def idadeDias(idade):
    quantDias = idadeMeses(idade) * 30
    return quantDias


def main():
    '''Questão 3
    idade = int(input("Digite sua idade: "))
    print("Sua idade em dias é : ", idadeDias(idade))'''

    idade = int(input("Digite sua idade: "))
    print("Sua idade em dias é : ", idadeDias(idade))
    print("Sua idade em meses é: ", idadeMeses(idade))
    print("Sua idade em anos é: ", idade)


main()


