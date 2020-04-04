'''Um banco concederá um crédito especial aos seus clientes, variável com o saldo médio
no último ano. Faça um algoritmo que leia o saldo médio de um cliente e calcule o valor do
crédito de acordo com a tabela abaixo. Mostre uma mensagem informando o saldo médio e
o valor do crédito.
Saldo médio    Percentual
de 0 a 200    nenhum crédito
de 201 a 400  20% do valor do saldo médio
de 401 a 600  30% do valor do saldo médio
acima de 601  40% do valor do saldo médio'''

def creditoEspecial(saldo):
        if saldo >= 0 and saldo <= 200:
            valorCredito = 0
        elif saldo >= 201 and saldo <= 400:
            valorCredito = (saldo * 20) / 100
        elif saldo >= 401 and saldo <= 600:
            valorCredito = (saldo * 30) / 100
        else:
            valorCredito = (saldo * 40) / 100
        return valorCredito

def main():
    saldo = float(input("Valor do saldo: "))
    print("Valor do crédtio: ", creditoEspecial(saldo))
    print("Saldo total: ", creditoEspecial(saldo) + saldo)


main()