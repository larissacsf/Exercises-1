'''Escrever um algoritmo que lê o número de identificação, as 3 notas obtidas por um
aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação. Calcular a
média de aproveitamento, usando a fórmula:
MA = (Nota1 + Nota2 x 2 + Nota3 x 3 + ME )/7
● A atribuição de conceitos obedece a tabela abaixo:
Média de Aproveitamento     Conceito
    9,0                        A
    7,5 e < 9,0                B
    6,0 e < 7,5                C
    4,0 e < 6,0                D
    < 4,0                      E
O algoritmo deve escrever o número do aluno, suas notas, a média dos exercícios, a média
de aproveitamento, o conceito correspondente e a mensagem: APROVADO se o conceito
for A,B ou C e REPROVADO se o conceito for D ou E.'''


def mediaAprovetamento(cod,n1,n2,n3,me):
    ma = (n1 + n2 * 2 + n3 * 3 + me) / 7
    if ma >= 9.0:
        print("Código: ",cod)
        print("Notas: ", n1,n2,n3)
        print("Média Exercício: ",me)
        print("Média aproveitamento: ",ma)
        print("Conceito A, aluno Aprovado!")
    elif ma >= 7.5 and ma < 9.0:
        print("Código: ", cod)
        print("Notas: ", n1, n2, n3)
        print("Média Exercício: ", me)
        print("Média aproveitamento: ", ma)
        print("Conceito B, aluno Aprovado!")
    elif ma >= 6.0 and ma < 7.5:
        print("Cpodigo: ", cod)
        print("Notas: ", n1, n2, n3)
        print("Média Exercício: ", me)
        print("Média aproveitamento: ", ma)
        print("Conceito C, aluno Aprovado!")
    elif ma >= 4.0 and ma < 6.0:
        print("Código: ", cod)
        print("Notas: ", n1, n2, n3)
        print("Média Exercício: ", me)
        print("Média aproveitamento: ", ma)
        print("Conceito D, aluno Reprovado!")
    else:
        print("Código: ", cod)
        print("Notas: ", n1, n2, n3)
        print("Média Exercício: ", me)
        print("Média aproveitamento: ", ma)
        print("Conceito E, aluno Reprovado!")
    return ""



def main():
    cod = int(input("Digite seu Código: "))
    n1 = float(input("Primeira Nota: "))
    n2 = float(input("Segunda Nota: "))
    n3 = float(input("Terceira Nota: "))
    me = float(input("Média dos Exercícios: "))
    print(mediaAprovetamento(cod,n1,n2,n3,me))
main()