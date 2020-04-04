'''Calcule a média aritmética das 3 notas de um aluno e mostre, além do valor da média,
uma mensagem de "Aprovado", caso a média seja igual ou superior a 6, ou a mensagem
"Reprovado", caso contrário.'''

def calcMedia(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if  media >= 6:
        print("Aprovado")
    else:
        print("Reprovado")
    return media

def main():
    nota1 = float(input("Primeira nota: "))
    nota2 = float(input("Segunda nota: "))
    nota3 = float(input("Terceira nota: "))
    print("Média: ", calcMedia(nota1, nota2, nota3))

main()