# 8) Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes
# ocorreu a letra ‘A’.
# OBS: Fazer crítica na entrada do caractere para aceitar somente letras.


def verficar_letra_A():
    cont = 0
    lista_letras = ['B','C','A','A','D']
    for i in lista_letras:
        if i == 'A':
            cont +=1
    return cont 

assert verficar_letra_A() == 2

print('teste tudo OK! da questão 8 da lista 2')