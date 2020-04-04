'''O cardápio de uma lancheria é o seguinte: Especificação Código Preço
Especificação  Código  Preço
Cachorro quente  100   1,20
Bauru simples    101   1,30
Bauru com ovo    102   1,50
Hambúrger        103   1,20
Cheeseburguer    104   1,30
Refrigerante     105   1,00
Escrever um algoritmo que leia o código do item pedido, a quantidade e calcule o valor a ser
pago por aquele lanche. Considere que a cada execução somente será calculado um item.'''


cardapio = {00 : 1.20, 101 : 1.30, 102 : 1.50, 103 : 1.20, 104 : 1.30, 105 : 1.00 }

def codigoCardapio(codigo):
    cod = cardapio[codigo]
    return cod

def calcValor(codigo, quantidade):
    valor = quantidade * cardapio[codigo]
    return valor

def main():
    print("100 - Cachorro quente | 101 - Bauru simples\n102 - Bauru com ovo | 103 - Hambúrger\n104 - Cheeseburguer | 105 - Refrigerante")
    codigo_Lanche = int(input("Digite o código do lanche que deseja comprar: "))
    quant_Lanche = int(input("Qual a quantidade que deseja comprar: "))
    print("Valor total: R$ ", calcValor(codigo_Lanche, quant_Lanche))

main()