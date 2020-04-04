'''Escrever um algoritmo que lê:
- a percentagem do IPI a ser acrescido no valor das peças
- o código da peça 1, valor unitário da peça 1, quantidade de peças 1
- o código da peça 2, valor unitário da peça 2, quantidade de peças 2
O algoritmo deve calcular o valor total a ser pago e apresentar o resultado.
Fórmula : (valor1*quant1 + valor2*quant2)*(IPI/100 + 1)'''

valor = []
quant = []
codigo = []

def calcPeca(ipi):
    codigo.append(int(input("Qua o código da peça 1: ")))
    valor.append(float(input("Qual o valor da peça 1: ")))
    quant.append(int(input("Qual a quantidade da peça 1: ")))
    codigo.append(int(input("Qua o código da peça 2: ")))
    valor.append(float(input("Qual o valor da peça 2: ")))
    quant.append(int(input("Qaul a quantidade da peça 2: ")))

    resultado = (valor[0] * quant[0] + valor[1] * quant[1]) * (ipi /100 + 1)
    return resultado

def main():
    ipi = int(input("Qual a porcentagemd o IPI: "))
    print("Valor total a ser pago: R$ ",calcPeca(ipi))

main()