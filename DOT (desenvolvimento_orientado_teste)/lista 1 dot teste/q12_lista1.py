# questão 12 dot
#Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor.
def somatorio(num):
    if type(num) != int or num <= 0:
        return Exception

    cont = 0
    for i in range(num+1):
        cont += i

    return cont

assert somatorio(5) == 15

assert somatorio('a') == Exception

assert somatorio(4.0) == Exception

assert somatorio(-1) == Exception

print('teste tudo Ok! da questão 12 da lista 1')