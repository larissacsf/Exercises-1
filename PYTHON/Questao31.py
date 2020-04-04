'''Escrever um algoritmo que calcule os sucessivos valores de E usando a série abaixo e
considerando primeiro 3 termos, depois 4 termos e, por fim, 5 termos:
E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + 1 / 4!'''


def valoresSucessivos():
    e = 1 + 1 + (1/2)
    print("E com 3 termos ", e)
    e = e + (1 / 6)
    print("E com 4 termos ", e)
    e = e + (1 / 24)
    print("E com 5 termos ", e)
    return ""

def main():
    print(valoresSucessivos())

main()