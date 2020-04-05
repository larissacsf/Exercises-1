def jogo():
    T = int(input("Quntas vezes deseja jogar: "))
    if T > 100:
        print("O número de tentativas é entre 1 e 100")
    else:
        for i in range(T):
            regras = {'tesoura': ('papel', 'lagarto'), 'pedra': ('lagarto', 'tesoura'), 'papel': ('pedra', 'Spock'),
                      'lagarto': ('Spock', 'papel'), 'Spock': ('tesoura', 'pedra')}

            print("Pedra | Papel | Tesoura | Lagarto | Spock")
            raj, sheldon = input("Escolha uma das opções acima, sabendo que Sheldon é o primeiro jogador "
                                 "e Raj o segundo: ").split(' ')

            if raj == sheldon:
                print("Caso #{0}: Novamente".format(i + 1))
            elif raj in regras[sheldon]:
                print("Caso #{0}: Raj trapaceou!".format(i + 1))
            else:
                print("Caso #{0}: Bazinga".format(i + 1))


def main():

    jogo()


main()
