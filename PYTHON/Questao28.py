'''Escrever um algoritmo que lê a hora de início e hora de término de um jogo, ambas
subdivididas em dois valores distintos : horas e minutos. Calcular e escrever a duração do
jogo, também em horas e minutos, considerando que o tempo máximo de duração de um
jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.'''

hora_inicio = []
hora_final = []

def tempPartida():
    hora_inicio.append(int(input("Informe o horário inicial: ")))
    hora_inicio.append(int(input("Informe os minutos inciais: ")))
    hora_final.append(int(input("Informe o horário final: ")))
    hora_final.append(int(input("Informe os minutos finais:  ")))

    hora_duracao = hora_final[0] - hora_inicio[0]
    minutos_duracao = hora_final[1] - hora_final[0]
    if hora_duracao < 0:
        hora_duracao = hora_duracao + 24
    if minutos_duracao < 0:
        minutos_duracao = minutos_duracao + 60
        hora_duracao = hora_duracao - 1
    print("Duração: ", hora_duracao, "horas e", minutos_duracao, "minutos")
    return ""

def main():
    print(tempPartida())
main()