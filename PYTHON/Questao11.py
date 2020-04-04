'''Elaborar um algoritmo que lê 2 valores a e b e os escreve com a mensagem: "São
múltiplos" ou "Não são múltiplos".'''

def multiplos(a, b):
    if a % b == 0 or b % a == 0:
        print("São múltiplos")
    else:
        print("Não são múltiplos")
    return ""
def main():
    a = int(input("Valor de A: "))
    b = int(input("Valor de B: "))
    print(multiplos(a,b))


main()