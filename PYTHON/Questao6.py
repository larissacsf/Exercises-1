'''Faça um algoritmo que leia o tempo de duração de um evento em uma fábrica expressa
em segundos e mostre-o expresso em horas, minutos e segundos.'''

def segundosHoras(segundos):
    horas = segundos / 3.600
    return horas
def segundosMinutos(segundos):
    minutos = segundos / 60
    return minutos

def main():
    segundos = int(input("Tempo do evento em segundos: "))
    print("O evento teve duraão de ", segundosHoras(segundos), "hr", segundosMinutos(segundos), "mim", segundos, "s")
main()
