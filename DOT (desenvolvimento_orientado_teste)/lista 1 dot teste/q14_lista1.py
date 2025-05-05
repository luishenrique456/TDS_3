#questão 14 dot
#Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
#S = 1 + 1/1! + 1⁄2! + 1/3! + 1 /N!
def fatorial(num):
    if type(num) != int or num <=0:
        return Exception


    cont = 1
    for qtd in range(1,num+1):
        cont *= qtd
    return cont

def formular(num):
    if type(num) != int or num <= 0:
        return Exception
    
    s = 1 + 1/fatorial(1) + 1/fatorial(2) + 1/fatorial(3) + 1/fatorial(num)
    return round(s,2)

assert fatorial(5) == 120

assert fatorial(1) == 1

assert fatorial(2) == 2

assert fatorial(3) == 6

assert formular(5) == 2.67

# testa entrada inválida 

assert fatorial(2.3) == Exception

assert fatorial('a') == Exception

assert fatorial(-2) == Exception

assert formular('b') == Exception

assert formular(-4) == Exception

assert formular(5.0) == Exception

print('Teste tudo OK! da questão 14 da lista 1')