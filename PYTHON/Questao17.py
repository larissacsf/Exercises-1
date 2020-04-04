'''Tendo como dados de entrada a altura e o sexo de uma pessoa (?M? masculino e ?F?
feminino), construa um algoritmo que calcule seu peso ideal, utilizando as seguintes
fórmulas:
- para homens: (72.7*h)-58
- para mulheres: (62.1*h)-44.7'''

def pesoIdealM(altura):
    pesoH = (72.7 * altura) - 58
    return pesoH

def pesoIdealF(altura):
    pesoM = (62.1 * altura) - 44.7
    return pesoM



def main():
    altura = float(input("Qual a sua altura: "))
    sexo = input("Qual o seu sexo? Escolha M para Masculino ou F para Faminino: ")
    if sexo.upper() == "M":
        print("Peso ideal: ",pesoIdealM(altura))
    else:
        print("Peso ideal: ",pesoIdealF(altura))

main()

