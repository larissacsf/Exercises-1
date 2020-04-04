'''Um vendedor necessita de um algoritmo que calcule o preço total devido por um cliente.
O algoritmo deve receber o código de um produto e a quantidade comprada e calcular o
preço total, usando a tabela abaixo:

Código do Produto   Preço unitário
    1001                5,32
    1324                6,45
    6548                2,37
    0987                5,32
    7623                6,45'''

codigo_produto = {1001 : 5.32, 1324 : 6.45, 6548 : 2.37, 987 : 5.32, 7623 : 6.45}

def codigoPreco(codigo):
    cod = codigo_produto[codigo]
    return cod

def calcValor(codigo, quantidade):
    valor = quantidade * codigo_produto[codigo]
    return valor

def main():
    print(" 1001 - 5,32 | 1324 - 6,45 | 6548 - 2,37 | 987 - 5,32 | 7623 - 6,45  ")
    codido = int(input("Digite o código do produto que deseja calcular: "))
    quantidade = int(input("Digite a quantidade que deseja comprar: "))
    print("Proço Total: ", calcValor(codido, quantidade))


main()





