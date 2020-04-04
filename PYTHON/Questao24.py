'''Escrever um algoritmo que lê a hora de início de um jogo e a hora do final do jogo
(considerando apenas horas inteiras) e calcula a duração do jogo em horas, sabendo-se
que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode iniciar em um dia
e terminar no dia seguinte.'''

def tempPartida(hora_inicio, hora_final):
    if hora_inicio >= hora_final:
        tempo_jogo = (24 - hora_inicio) + hora_final
    else:
        tempo_jogo = hora_final - hora_inicio
    return tempo_jogo

def main():
    hora_inicio= int(input("Qual a hora da início do jogo? "))
    hora_final = int(input("Qual a hora do fim do jogo? "))
    print("Duração da partida: ", tempPartida(hora_inicio, hora_final),"horas")

main()