# questão 13 dot
#Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
#S = 1 + 1⁄2 + 1/3 + 1⁄4 + 1/5 + 1/N.
def formular_S(num):
    if type(num) != int or num <= 0:
        return Exception

    s = 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/num
    return round(s,2)

assert formular_S(5) == 2.48

assert formular_S('a') == Exception

assert formular_S(-2) == Exception

assert formular_S(3.0) == Exception

print('Teste tudo OK! da questão 13 da lista 1')