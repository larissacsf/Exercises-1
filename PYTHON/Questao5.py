'''Faça um algoritmo que leia as 3 notas de um aluno e calcule a média final deste aluno.
Considerar que a média é ponderada e que o peso das notas é: 2,3 e 5, respectivamente.'''

def calcMedia(nota1, nota2, nota3):
    media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / (2+3+5)
    return media

def main():
    nota1 = float(input("Primeira nota: "))
    nota2 = float(input("Segunda nota: "))
    nota3 = float(input("Terceira nota: "))
    print("Média: ", calcMedia(nota1, nota2, nota3))

main()
