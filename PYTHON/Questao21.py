'''Um vendedor precisa de um algoritmo que calcule o preço total devido por um cliente. O
algoritmo deve receber o código de um produto e a quantidade comprada e calcular o preço
total, usando a tabela abaixo. Mostre uma mensagem no caso de código inválido.
    Código   Preço unitário
    'ABCD'    R$ 5,30
    'XYPK'    R$ 6,00
    'KLMP'    R$ 3,20
    'QRST'    R$ 2,50'''

codigo_preco = {'ABCD': 5.30, 'XYPK': 6.00, 'KLMP': 3.20, 'ORST': 2.50}

def codigoPreco(codigo):
    cod = codigo_preco[codigo]
    return cod

def calcValor(codigo, quantidade):
    valor = quantidade * codigo_preco[codigo]
    return valor



def main():
    print("ABCD - 5.30 | XYPK - 6.00 | KLMP - 3.20 | ORST - 2.50  ")
    codigo = (input("Digite o código do produto que deseja calcular: "))
    if codigo != codigo_preco.keys():
        print("Código Inválido! Por favor escolha um código válido")
    else:
        quantidade = int(input("Digite a quantidade que deseja comprar: "))
        print("Preço Total: ", calcValor(codigo, quantidade))


main()
