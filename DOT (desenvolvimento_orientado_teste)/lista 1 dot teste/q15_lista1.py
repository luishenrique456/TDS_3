# questão 15 dot
#Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
#S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3)
def calcular_s(num:int)-> float:
    if type(num) != int or num <= 0:
        return Exception
    resp = 0
    for i in range(1,num+1):
        resp = (i**2+1)/(i+3)
    return round(resp,2)

assert calcular_s(5) == 3.25

assert calcular_s('a') == Exception

assert calcular_s(-1) == Exception

assert calcular_s(3.0) == Exception

print('Teste tudo OK! da questão 15 da lista 1')