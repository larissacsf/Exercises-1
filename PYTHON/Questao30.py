'''O departamento que controla o índice de poluição do meio ambiente mantém 3 grupos
de indústrias que são altamente poluentes do meio ambiente. O índice de poluição aceitável
varia de 0,05 até 0,25. Se o índice sobe para 0,3 as indústrias do 1o grupo são intimadas a
suspenderem suas atividades, se o índice cresce para 0,4 as do 1o e 2o grupo são
intimadas a suspenderem suas atividades e se o índice atingir 0,5 todos os 3 grupos devem
ser notificados a paralisarem suas atividades. Escrever um algoritmo que lê o índice de
poluição medido e emite a notificação adequada aos diferentes grupos de empresas.'''

def indicePoluicao(ind):
    if ind >= 0.05 and ind <= 0.25:
        print("Índice de poluição aceitavél")
    elif ind < 0.4:
            print("Indústrias do gupo 1 devem suspeder as atividades")
    elif ind >= 0.4 and ind < 0.5:
        print("Indústrias do gupo 1 e 2 devem suspeder as atividades")
    else:
        print("Indústrias do grupo 1, 2 e 3 devem suspender as atividade")
    return ""

def main():
    ind = float(input("Índice de Poluição: "))
    print(indicePoluicao(ind))
main()