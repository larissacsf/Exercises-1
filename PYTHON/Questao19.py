'''Um usuário deseja um algoritmo onde possa escolher que tipo de média deseja calcular
a partir de 3 notas. Faça um algoritmo que leia as notas, a opção escolhida pelo usuário e
calcule a média.
19.1 -aritmética
19.2 -ponderada (3,3,4)
19.3 -harmônica'''


def calcMedia( codigo, nota1, nota2, nota3):
    if codigo == "19.1":
        media =  (nota1 + nota2 + nota3) / 3
    elif codigo == "19.2":
        media = (nota1 * 3 + nota2 * 3 + nota3 * 4) / 10
    else:
        media = 3 / (1 / nota1 + 1 / nota2 + 1 / nota3)
    return media


def main():
    print("19.1 - Média Aritmética| 19.2 - Média Ponderada | 19.3 - Média Harmônica")
    codigo = float(input("Escolhe um código de acordo com a média que deseja calcular: : "))
    n1 =  float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    print("Média: ",calcMedia(codigo, n1,n2,n3))
main()
