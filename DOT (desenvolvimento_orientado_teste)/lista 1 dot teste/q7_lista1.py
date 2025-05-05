# Questão 7 DOT
#Faça um programa para calcular o Fatorial de número .
#Para o cálculo do fatorial , sabemos que N! depende de (N-1)!
#este por sua vez depende de (N-2)! : e,assim por diante , até que N seja 1 ,
#Quando então tem-se que fatorial de 1 igual a 1 mesmo.
#Utilize uma função que recebe como parâmetro de entrada o número a ser calculado o fatorial,
#do tipo inteiro, e retorna o fatorial deste número , também do tipo inteiro.
def fatorial(num):
    if type(num) != int or num < 0:
        return Exception

    if num == 0:
        return 1
    if num == 1:
        return 1
    cont = 1
    for qtd in range(1,num+1):
        cont *= qtd
    return cont

assert fatorial(5) == 120

assert fatorial(0) == 1

assert fatorial(1) == 1

#testa possivel erro do user

assert fatorial('a') == Exception

assert fatorial(2.0) == Exception

assert fatorial(-4) == Exception

print('teste tudo OK! da questão 7 da lista 1')