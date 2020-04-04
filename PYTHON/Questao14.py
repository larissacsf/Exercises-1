'''Escreva um algoritmo que leia o código de um aluno e suas três notas. Calcule a média
ponderada do aluno, considerando que o peso para a maior nota seja 4 e para as duas
restantes, 3. Mostre o código do aluno, suas três notas, a média calculada e uma
mensagem "APROVADO" se a média for maior ou igual a 5 e "REPROVADO" se a média
for menor que 5.'''

def calcMediaPonderada(nota1, nota2, nota3):
    if nota1 >= nota2 and nota1 >= nota3:
        maior = nota1
        soma = nota2 + nota3
    elif nota2 >= nota3:
        maior = nota2
        soma = nota1 + nota3
    else:
        maior = nota3
        soma = nota1 + nota2

    media = (maior * 4 + soma * 3) / 10
    if media >= 5:
        print("Aprovado")
    else:
        print("Reprovado")

    return media

def main():
    cod = input("Código do aluno: ")
    nota1 = float(input("Primeira nota: "))
    nota2 = float(input("Segunda nota: "))
    nota3 = float(input("Terceira nota: "))
    print("Código: ", cod, "\n", "Notas: \n", nota1, "\n", nota2, "\n", nota3)
    print("Média: ", calcMediaPonderada(nota1, nota2, nota3))


main()