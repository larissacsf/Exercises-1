'''Uma empresa concederá um aumento de salário aos seus funcionários, variável de
acordo com o cargo, conforme a tabela abaixo. Faça um algoritmo que leia o salário e o
cargo de um funcionário e calcule o novo salário. Se o cargo do funcionário não estiver na
tabela, ele deverá, então, receber 40% de aumento. Mostre o salário antigo, o novo salário
e a diferença.
Código  Cargo   Percentual
101     Gerente     10%
102     Engenheiro  20%
103     Técnico     30%'''

tabela_salario = {'Gerente': 10, 'Engenheiro': 20, 'Técnico': 30, 'Outros': 40 }

def codigoPreco(cargo):
    car = tabela_salario[cargo]
    return car

def calcSalarioDiferenca(cargo, salario):
    salarioDiferenca = (salario * tabela_salario[cargo]) / 100
    return salarioDiferenca

def calcSalarioAumento(cargo, salario):
    salarioAumento = salario + (salario * tabela_salario[cargo]) / 100
    return salarioAumento

def main():
    print("Gerente | Engenheiro | Técnico| Outros ")
    cargo = input("Digite seu cargo: ")
    salario = float(input("Digite o valor do salário: "))
    print("Salário Antigo: R$", salario)
    print("Novo Salário: R$", calcSalarioAumento(cargo,salario))
    print("Diferença: ", calcSalarioDiferenca(cargo,salario))


main()