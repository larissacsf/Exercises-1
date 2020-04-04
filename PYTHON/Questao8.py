'''Um sistema de equações lineares do tipo: ax+by=c e dx+ey=f,pode ser resolvido segundo mostrado abaixo:
X = ce - bf / ae - bd e Y = af - cd / ae - bd.
Escreva um algoritmo que lê os coeficientes a,b,c,d ,e e f e calcular e mostrar os valores X e Y.'''

def calcLinearX(a, b, c, d, e , f):
    x = ((c * e) - (b * f))/ ((a * e) - (b * d))
    return x

def calcLinearY(a, b, c, d, e, f):
    y = ((a * f) - (c * d)) / ((a * e) - (b * d))
    return y

def main():
    a = int(input("Dgite o valor de A: "))
    b = int(input("Dgite o valor de B: "))
    c = int(input("Dgite o valor de C: "))
    d = int(input("Dgite o valor de D: "))
    e = int(input("Dgite o valor de E: "))
    f = int(input("Dgite o valor de F: "))

    print("Valor de X: ", calcLinearX(a, b, c, d, e, f))
    print("Valor de Y: ", calcLinearX(a, b, c, d, e, f))

main()



